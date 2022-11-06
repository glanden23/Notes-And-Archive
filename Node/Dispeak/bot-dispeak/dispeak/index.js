//
// MAIN DEPENDENCIES
//

const discord = require('discord.js')//@12.5.3
const client = new discord.Client()
const fs = require("fs")
const db = require('quick.db')
const version = "v2.1"
const S = require('string')
const devMode = false
const cooldown = new Set()

//
// Sleep Function
//

function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
}

//
// DISCORD READY EVENT
//

client.on("ready", async () => {
    if (devMode) {
        client.channels.cache.get("899077996579799083").messages.fetch("899127759987679293")
        return;
    }

    autoSetStatus()

    //
    // EDIT MESSAGES ON STARTUP & SET EMOTES
    //

    editNotify()
    editInfo()
    editRules()
    createRoomEdit()
})

//
// SET STATUS
//

if (devMode === false){
    client.setInterval(() => {
        autoSetStatus()
    }, 600000)
}

function autoSetStatus() {
    client.user.setActivity({
        name: version,
        type: "PLAYING"
    })
}

function editNotify() {
    client.channels.cache.get("899077963763564585").messages.fetch("899095893100331008").then(async msg => {
        let embed = new discord.MessageEmbed()
        .setTitle("Server Notifications")
        .setThumbnail("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Ficons.iconarchive.com%2Ficons%2Fpaomedia%2Fsmall-n-flat%2F1024%2Fbell-icon.png&f=1&nofb=1")
        .setColor("#0000ff")
        .setDescription(fs.readFileSync("./messages/notify.txt"))
        msg.edit(embed)
        if (msg.reactions.cache.has("🔵") && msg.reactions.cache.has("🟡") && msg.reactions.cache.has("🔴")) {
            return;
        }
        msg.react("🔵")
        await sleep(1000)
        msg.react("🟡")
    })
}

function editInfo() {
    client.channels.cache.get("899077924899143750").messages.fetch("899097273055707156").then(msg => {
        let embed = new discord.MessageEmbed()
        .setTitle("Dispeak Information")
        .setThumbnail("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwebstockreview.net%2Fimages%2Finformation-clipart-information-icon-1.png&f=1&nofb=1")
        .setColor("#ffff00")
        .setDescription(fs.readFileSync("./messages/info.txt"))
        msg.edit(embed)
    })
}

function editRules() {
    client.channels.cache.get("899077924899143750").messages.fetch("899097273907175434").then(msg => {
        let embed = new discord.MessageEmbed()
        .setTitle("Dispeak Rules")
        .setThumbnail("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.pngkey.com%2Fpng%2Ffull%2F913-9133866_rules-bot-rule-bot-discord.png&f=1&nofb=1")
        .setColor("#ff0000")
        .setDescription(fs.readFileSync("./messages/rules.txt"))
        msg.edit(embed)
    })
}

//
// CREATE CHANNEL MESSAGE LOOP
//

client.setInterval(() => {
    if (devMode) {
        return;
    }
    createRoomEdit()
}, 60000)

function createRoomEdit() {
    client.channels.cache.get("899077996579799083").messages.fetch("899127759987679293").then(msg => {
        let embed = new discord.MessageEmbed()
        .setTitle(`Create Your Own Room!`)
        .setColor("#0000ff")
        .setDescription(`Click or react with a \"📎\" emote to create a room!\nCurrent Rooms: ${(client.guilds.cache.get("899074075543105557").channels.cache.array().length - 5) / 3}/165`)
        msg.edit(embed)
        if (msg.reactions.cache.has("📎")) {
            return;
        }
        msg.react("📎")
    })
}

//
// DISCORD REACTION HANDLER
//

client.on("messageReactionAdd", async (reaction, user) => {
    if (cooldown.has(user.id)) {
        return;
    }
    if (client.user.id === user.id) {
        return;
    }
    if (devMode) {
        if (client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.cache.has("899126330560507945") === false) {
            return;
        }
    }else{
        if (client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.cache.has("899126330560507945") === true) {
            return;
        }
    }
    if (reaction.emoji.name === "📎" && reaction.message.id === "899127759987679293") {
        reaction.users.remove(user.id)
        if (db.get(`room_cg_${user.id}`) != null) {
            reaction.message.channel.send(`<@${user.id}> `+"You already own a room! Please delete that room before you create a new one!").then(msg => {
                msg.delete({timeout: 10000 })
            })
            return;
        }
        if (client.guilds.cache.get("899074075543105557").members.cache.get(user.id).nickname != undefined) {
            var name = client.guilds.cache.get("899074075543105557").members.cache.get(user.id).nickname
        }else{
            var name = user.username
        }
        let cg = await reaction.message.guild.channels.create(`${name}'s Room`, {type: "category"})
        await db.set(`room_cg_${user.id}`, `${cg.id}`)
        let tc = await (await (await reaction.message.guild.channels.create(`💬┃${name}-text`, {type: "text"})).setParent(cg.id)).overwritePermissions([
            {
                id: user.id,
                allow: ["VIEW_CHANNEL", "MANAGE_MESSAGES"]
            },
            {
                id: reaction.message.guild.roles.everyone,
                deny: ["VIEW_CHANNEL"]
            }
        ])
        await db.set(`room_tc_${user.id}`, tc.id)
        let vc = await (await (await reaction.message.guild.channels.create(`🔊┃${name} VC`, {type: "voice"})).setParent(cg.id)).overwritePermissions([
            {
                id: user.id,
                allow: ["VIEW_CHANNEL"]
            },
            {
                id: reaction.message.guild.roles.everyone,
                deny: ["VIEW_CHANNEL"]
            }
        ])
        await db.set(`room_vc_${user.id}`, vc.id)
        reaction.message.channel.send(`<@${user.id}> `+"Your room has been created!").then(msg => {
            msg.delete({timeout: 10000 })
        })
        let embed = new discord.MessageEmbed()
        .setTitle("Thanks for creating a room!")
        .setColor("#0000ff")
        .setDescription(`Your new room starts out as private but this can be changed of course!\n\nIt is recommended you give <#899077924899143750> a read if you haven't already as it contains a lot of important information on how to setup your room and what rules you should be following. (especially if you decide to make it public)`)
        client.channels.cache.get(tc.id).send(embed)
    }
    if (reaction.message.id === "899095893100331008") {
        if (reaction.emoji.name === "🔵") {
            client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.add("899297619157876796")
            reaction.message.channel.send(`<@${user.id}>, you'll now be notified of bot updates.`).then(msg => {
                msg.delete({timeout: 5000})
            })
        }else if(reaction.emoji.name === "🟡") {
            client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.add("899297685675339777")
            reaction.message.channel.send(`<@${user.id}>, you'll now be notified of any downtime.`).then(msg => {
                msg.delete({timeout: 5000})
            })
        }
    }
})

client.on("messageReactionRemove", (reaction, user) => {
    if (cooldown.has(user.id)) {
        return;
    }
    if (client.user.id === user.id) {
        return;
    }
    if (devMode) {
        if (client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.cache.has("899126330560507945") === false) {
            return;
        }
    }else{
        if (client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.cache.has("899126330560507945") === true) {
            return;
        }
    }
    if (reaction.message.id === "899095893100331008") {
        if (reaction.emoji.name === "🔵") {
            client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.remove("899297619157876796")
            reaction.message.channel.send(`<@${user.id}>, you'll **no longer** be notified of bot updates.`).then(msg => {
                msg.delete({timeout: 5000})
            })
        }else if(reaction.emoji.name === "🟡") {
            client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.remove("899297685675339777")
            reaction.message.channel.send(`<@${user.id}>, you'll **no longer** be notified of any downtime.`).then(msg => {
                msg.delete({timeout: 5000})
            })
        }
    }
})

client.on("guildMemberUpdate", (olduser, newuser) => {
    if (cooldown.has(newuser.id)) {
        return;
    }
    if (devMode) {
        if (client.guilds.cache.get("899074075543105557").members.cache.get(newuser.id).roles.cache.has("899126330560507945") === false) {
            return;
        }
    }else{
        if (client.guilds.cache.get("899074075543105557").members.cache.get(newuser.id).roles.cache.has("899126330560507945") === true) {
            return;
        }
    }
    if (olduser.nickname != newuser.nickname) {
        if (db.get(`room_cg_${newuser.id}`) != null) {
            if (newuser.nickname === null) {
                client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_cg_${newuser.id}`)).setName(`${newuser.user.username}'s Room`)
            }else{
                client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_cg_${newuser.id}`)).setName(`${newuser.nickname}'s Room`)
            }
        }
    }
})

client.on("userUpdate", (olduser, newuser) => {
    if (cooldown.has(newuser.id)) {
        return;
    }
    if (devMode) {
        if (client.guilds.cache.get("899074075543105557").members.cache.get(newuser.id).roles.cache.has("899126330560507945") === false) {
            return;
        }
    }else{
        if (client.guilds.cache.get("899074075543105557").members.cache.get(user.id).roles.cache.has("899126330560507945") === true) {
            return;
        }
    }
    if (client.guilds.cache.get("899074075543105557").members.cache.get(newuser.id).nickname === null) {
        return;
    }
    if (olduser.username != newuser.username) {
        client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_cg_${newuser.id}`)).setName(`${newuser.username}'s Room`)
    }
})

//
// DISCORD COMMAND HANDLER
//

client.on("message", async (message) => {
    if (!message.content.startsWith("!") || message.author.bot) return;
    const args = message.content.slice(1).trim().split(/ +/g);
    const command = args.shift().toLowerCase();

    if (devMode) {
        if (message.member.roles.cache.has("899126330560507945") === false && message.member.roles.cache.has("899080837084086283") === false) {
            return;
        }
    }else{
        if (message.member.roles.cache.has("899126330560507945") === true || message.member.roles.cache.has("899080837084086283") === true) {
            return;
        }
    }

    //
    // Developer Commands
    //

    if (message.member.roles.cache.has("899080837084086283")) {

        //
        // Ping Commands
        //

        if (command === "updateping") {
            client.channels.cache.get("899077899938856960").send("<@&899297619157876796>").then(msg => {
                msg.delete({ timeout: 5000 })
            })
        }
        
        if (command === "downtimeping") {
            client.channels.cache.get("899077899938856960").send("<@&899297685675339777>").then(msg => {
                msg.delete({ timeout: 5000 })
            })
        }

        //
        // Update Embeds Command
        //

        if (command === "updatemessages") {
            editNotify()
            editRules()
            editInfo()
            console.log(`${message.author.tag} has updated embeds.`)
            message.channel.send("Embeds have been updated with new formatting.")
        }

        //
        // Give Admin Perms over Dispeak
        //

        if (command === "star") {
            if (message.member.roles.cache.has("899079994838511666")) {
                client.guilds.cache.get("899074075543105557").members.cache.get(message.author.id).roles.remove("899076199702212629")
                message.member.roles.remove("899079994838511666")
                console.log(`${message.author.id} has disabled star permissions.`)
                message.channel.send("Disabled star permissions in both servers...")
            }else{
                client.guilds.cache.get("899074075543105557").members.cache.get(message.author.id).roles.add("899076199702212629")
                message.member.roles.add("899079994838511666")
                console.log(`${message.author.id} has enabled star permissions.`)
                message.channel.send("Enabled star permissions in both servers...")
            }
        }
    }
    if (db.get(`room_admins_${message.channel.id}`) === null) {
        if (cooldown.has(message.author.id) || db.get(`room_tc_${message.author.id}`) != message.channel.id) {
            return;
        }else{
            var roomadmin = false
        }
    }else{
        if (db.get(`room_admins_${message.channel.id}`).includes(message.author.id) === false) {
            if (cooldown.has(message.author.id) || db.get(`room_tc_${message.author.id}`) != message.channel.id) {
                return;
            }else{
                var roomadmin = false
            }
        }else{
            var roomadmin = true
        }
    }

    //
    // Log Commands
    //

    console.log(message.author.tag+": " + message.content)

    //
    // Room Commands
    //

    if (command === "admin") {
        if (roomadmin === true) {
            return;
        }
        if (args[0] === undefined) {
            message.channel.send("Please provide a user tag! (user#0001)").then(msg => {
                msg.delete({timeout: 10000})
                message.delete({timeout: 10000})
            })
            return;
        }
        var person = message.content.slice(7)
        var user = client.users.cache.find(user => user.tag === person)
        if (user === undefined) {
            message.channel.send("Couldn't find user " + person + "!").then(msg => {
                msg.delete({timeout: 10000})
                message.delete({timeout: 10000})
            })
            return;
        }
        if (user.id === message.author.id) {
            return;
        }
        var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
        var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        if (db.get("adminp_stream_"+message.channel.id) === false) {
            var streama = false
        }else{
            var streama = true
        }
        if (db.get("adminp_sendmsg_"+message.channel.id) === false) {
            var sendmsga = false
        }else{
            var sendmsga = true
        }
        if (db.get("adminp_embedlinks_"+message.channel.id) === false) {
            var embedlinksa = false
        }else{
            var embedlinksa = true
        }
        if (db.get("adminp_attachfiles_"+message.channel.id) === false) {
            var attachfilesa = false
        }else{
            var attachfilesa = true
        }
        if (db.get("adminp_addreactions_"+message.channel.id) === false) {
            var addreactionsa = false
        }else{
            var addreactionsa = true
        }
        if (db.get("adminp_externalemotes_"+message.channel.id) === false) {
            var externalemotesa = false
        }else{
            var externalemotesa = true
        }
        if (db.get("adminp_speak_"+message.channel.id) === false) {
            var speaka = false
        }else{
            var speaka = true
        }
        if (db.get("adminp_managemessages_"+message.channel.id) === false) {
            var managemessagesa = false
        }else{
            var managemessagesa = true
        }
        if (db.get("room_admins_"+message.channel.id) === null) {
            let array = []
            array.push(user.id)
            await vc.updateOverwrite(user.id, {VIEW_CHANNEL: true, SPEAK: speaka, STREAM: streama})
            await tc.updateOverwrite(user.id, {VIEW_CHANNEL: true, SEND_MESSAGES: sendmsga, EMBED_LINKS: embedlinksa, ATTACH_FILES: attachfilesa, ADD_REACTIONS: addreactionsa, USE_EXTERNAL_EMOJIS: externalemotesa, MANAGE_MESSAGES: managemessagesa})
            db.set("room_admins_"+message.channel.id, array)
            message.channel.send(`Added ${user.tag} to admin list.`).then(msg => {
                msg.delete({timeout: 30000})
                message.delete({timeout: 30000})
            })
            return;
        }
        if (db.get("room_admins_"+message.channel.id).includes(user.id)) {
            let array = db.get("room_admins_"+message.channel.id)
            let index = array.indexOf(user.id)
            if (index === "-1") {
                message.channel.send("An error has occured.").then(msg => {
                    msg.delete({timeout: 10000})
                    message.delete({timeout: 10000})
                })
                return;
            }
            array.splice(index)
            db.set("room_admins_"+message.channel.id, array)
            message.channel.send(`Removed ${user.tag} from admin list.`).then(msg => {
                msg.delete({timeout: 10000})
                message.delete({timeout: 10000})
            })
        }else{
            let array = db.get("room_admins_"+message.channel.id)
            array.push(user.id)
            await vc.updateOverwrite(user.id, {VIEW_CHANNEL: true, SPEAK: speaka, STREAM: streama})
            await tc.updateOverwrite(user.id, {VIEW_CHANNEL: true, SEND_MESSAGES: sendmsga, EMBED_LINKS: embedlinksa, ATTACH_FILES: attachfilesa, ADD_REACTIONS: addreactionsa, USE_EXTERNAL_EMOJIS: externalemotesa, MANAGE_MESSAGES: managemessagesa})
            db.set("room_admins_"+message.channel.id, array)
            message.channel.send(`Added ${user.tag} to admin list.`).then(msg => {
                msg.delete({timeout: 30000})
                message.delete({timeout: 30000})
            })
        }
    }

    if (command === "setpermission") {
        if (roomadmin) {
            if (db.get("adminp_managepermissions_"+message.channel.id) === true) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        if (args[0] === "global") {
            if (args[1] === "stream") {
                if (args[2] === "y" || args[2] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {STREAM: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {STREAM: false})
                }
            }else if(args[1] === "send" && args[2] === "messages") {
                if (args[3] === "y" || args[3] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {SEND_MESSAGES: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {SEND_MESSAGES: false})
                }
            }else if(args[1] === "embed" && args[2] === "links") {
                if (args[3] === "y" || args[3] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {EMBED_LINKS: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {EMBED_LINKS: false})
                }
            }else if(args[1] === "attach" && args[2] === "files") {
                if (args[3] === "y" || args[3] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {ATTACH_FILES: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {ATTACH_FILES: false})
                }
            }else if(args[1] === "add" && args[2] === "reactions") {
                if (args[3] === "y" || args[3] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {ATTACH_FILES: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {ATTACH_FILES: false})
                }
            }else if(args[1] === "external" && args[2] === "emotes") {
                if (args[3] === "y" || args[3] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {USE_EXTERNAL_EMOJIS: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {USE_EXTERNAL_EMOJIS: false})
                }
            }else if(args[1] === "speak"){
                if (args[2] === "y" || args[2] === "yes") {
                    vc.updateOverwrite(message.guild.roles.everyone, {SPEAK: true})
                }else{
                    vc.updateOverwrite(message.guild.roles.everyone, {SPEAK: false})
                }
            }else{
                message.channel.send("Invalid permission. Please view a list of valid ones with \"!permissions\".").then(msg => {
                    msg.delete({ timeout: 10000 })
                    message.delete({ timeout: 10000 })
                })
                return;
            }
        }else if(args[0] === "admin") {
            if (roomadmin) {
                return;
            }
            if (args[1] === "stream") {
                if (args[2] === "y" || args[2] === "yes") {
                    db.set("adminp_stream_"+message.channel.id, true)
                }else{
                    db.set("adminp_stream_"+message.channel.id, false)
                }
            }else if(args[1] === "send" && args[2] === "messages") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_sendmsg_"+message.channel.id, true)
                }else{
                    db.set("adminp_sendmsg_"+message.channel.id, false)
                }
            }else if(args[1] === "embed" && args[2] === "links") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_embedlinks_"+message.channel.id, true)
                }else{
                    db.set("adminp_embedlinks_"+message.channel.id, false)
                }
            }else if(args[1] === "attach" && args[2] === "files") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_attachfiles_"+message.channel.id, true)
                }else{
                    db.set("adminp_attachfiles_"+message.channel.id, false)
                }
            }else if(args[1] === "add" && args[2] === "reactions") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_addreactions_"+message.channel.id, true)
                }else{
                    db.set("adminp_addreactions_"+message.channel.id, false)
                }
            }else if(args[1] === "external" && args[2] === "emotes") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_externalemotes_"+message.channel.id, true)
                }else{
                    db.set("adminp_externalemotes_"+message.channel.id, false)
                }
            }else if(args[1] === "speak"){
                if (args[2] === "y" || args[2] === "yes") {
                    db.set("adminp_speak_"+message.channel.id, true)
                }else{
                    db.set("adminp_speak_"+message.channel.id, false)
                }
            }else if(args[1] === "manage" && args[2] === "members") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_managemembers_"+message.channel.id, true)
                }else{
                    db.set("adminp_managemembers_"+message.channel.id, false)
                }
            }else if(args[1] === "manage" && args[2] === "permissions") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_managepermissions_"+message.channel.id, true)
                }else{
                    db.set("adminp_managepermissions_"+message.channel.id, false)
                }
            }else if(args[1] === "manage" && args[2] === "messages") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_managemessages_"+message.channel.id, true)
                }else{
                    db.set("adminp_managemessages_"+message.channel.id, false)
                }
            }else if(args[1] === "manage" && args[2] === "settings") {
                if (args[3] === "y" || args[3] === "yes") {
                    db.set("adminp_managesettings_"+message.channel.id, true)
                }else{
                    db.set("adminp_managesettings_"+message.channel.id, false)
                }
            }else{
                message.channel.send("Invalid permission. Please view a list of valid ones with \"!permissions\".").then(msg => {
                    msg.delete({ timeout: 10000 })
                    message.delete({ timeout: 10000 })
                })
                return;
            }
        }else{
            message.channel.send("Invalid group. Did you mean \"Global\"?").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        if (args[0] === "admin") {
            if (db.get("room_admins_"+message.channel.id) === null) {
                return;
            }
            if (db.get("adminp_stream_"+message.channel.id) === false) {
                var streama = false
            }else{
                var streama = true
            }
            if (db.get("adminp_sendmsg_"+message.channel.id) === false) {
                var sendmsga = false
            }else{
                var sendmsga = true
            }
            if (db.get("adminp_embedlinks_"+message.channel.id) === false) {
                var embedlinksa = false
            }else{
                var embedlinksa = true
            }
            if (db.get("adminp_attachfiles_"+message.channel.id) === false) {
                var attachfilesa = false
            }else{
                var attachfilesa = true
            }
            if (db.get("adminp_addreactions_"+message.channel.id) === false) {
                var addreactionsa = false
            }else{
                var addreactionsa = true
            }
            if (db.get("adminp_externalemotes_"+message.channel.id) === false) {
                var externalemotesa = false
            }else{
                var externalemotesa = true
            }
            if (db.get("adminp_speak_"+message.channel.id) === false) {
                var speaka = false
            }else{
                var speaka = true
            }
            if (db.get("adminp_managemessages_"+message.channel.id) === false) {
                var managemessagesa = false
            }else{
                var managemessagesa = true
            }
            let adminlist = db.get("room_admins_"+message.channel.id)
            adminlist.forEach(async user => {
                await vc.updateOverwrite(user, {VIEW_CHANNEL: true, SPEAK: speaka, STREAM: streama})
                await tc.updateOverwrite(user, {VIEW_CHANNEL: true, SEND_MESSAGES: sendmsga, EMBED_LINKS: embedlinksa, ATTACH_FILES: attachfilesa, ADD_REACTIONS: addreactionsa, USE_EXTERNAL_EMOJIS: externalemotesa, MANAGE_MESSAGES: managemembersa})
            })
        }
        message.react("✅")
        message.delete({ timeout: 30000 })
    }

    if (command === "permissions") {
        if (roomadmin) {
            if (db.get("adminp_managepermissions_"+message.channel.id) === true) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        if(vc.permissionsFor(message.guild.roles.everyone).has("STREAM")){
            var stream = ":white_check_mark:"
        }else{
            var stream = ":x:"
        }
        if(tc.permissionsFor(message.guild.roles.everyone).has("SEND_MESSAGES")){
            var sendmsg = ":white_check_mark:"
        }else{
            var sendmsg = ":x:"
        }
        if(tc.permissionsFor(message.guild.roles.everyone).has("EMBED_LINKS")){
            var embedlinks = ":white_check_mark:"
        }else{
            var embedlinks = ":x:"
        }
        if(tc.permissionsFor(message.guild.roles.everyone).has("ATTACH_FILES")){
            var attachfiles = ":white_check_mark:"
        }else{
            var attachfiles = ":x:"
        }
        if(tc.permissionsFor(message.guild.roles.everyone).has("ADD_REACTIONS")){
            var addreactions = ":white_check_mark:"
        }else{
            var addreactions = ":x:"
        }
        if(tc.permissionsFor(message.guild.roles.everyone).has("USE_EXTERNAL_EMOJIS")){
            var externalemotes = ":white_check_mark:"
        }else{
            var externalemotes = ":x:"
        }
        if(vc.permissionsFor(message.guild.roles.everyone).has("SPEAK")){
            var speak = ":white_check_mark:"
        }else{
            var speak = ":x:"
        }
        if (db.get("adminp_stream_"+message.channel.id) === false) {
            var streama = ":x:"
        }else{
            var streama = ":white_check_mark:"
        }
        if (db.get("adminp_sendmsg_"+message.channel.id) === false) {
            var sendmsga = ":x:"
        }else{
            var sendmsga = ":white_check_mark:"
        }
        if (db.get("adminp_embedlinks_"+message.channel.id) === false) {
            var embedlinksa = ":x:"
        }else{
            var embedlinksa = ":white_check_mark:"
        }
        if (db.get("adminp_attachfiles_"+message.channel.id) === false) {
            var attachfilesa = ":x:"
        }else{
            var attachfilesa = ":white_check_mark:"
        }
        if (db.get("adminp_addreactions_"+message.channel.id) === false) {
            var addreactionsa = ":x:"
        }else{
            var addreactionsa = ":white_check_mark:"
        }
        if (db.get("adminp_externalemotes_"+message.channel.id) === false) {
            var externalemotesa = ":x:"
        }else{
            var externalemotesa = ":white_check_mark:"
        }
        if (db.get("adminp_speak_"+message.channel.id) === false) {
            var speaka = ":x:"
        }else{
            var speaka = ":white_check_mark:"
        }
        if (db.get("adminp_managemembers_"+message.channel.id) === false) {
            var managemembersa = ":x:"
        }else{
            var managemembersa = ":white_check_mark:"
        }
        if (db.get("adminp_managepermissions_"+message.channel.id) === true) {
            var managepermissionsa = ":white_check_mark:"
        }else{
            var managepermissionsa = ":x:"
        }
        if (db.get("adminp_managemessages_"+message.channel.id) === false) {
            var managemessagesa = ":x:"
        }else{
            var managemessagesa = ":white_check_mark:"
        }
        if (db.get("adminp_managesettings_"+message.channel.id) === true) {
            var managesettingsa = ":white_check_mark:"
        }else{
            var managesettingsa = ":x:"
        }
        if (db.get("room_admins_"+message.channel.id) === null) {
            var admins = "None."
        }else{
            let adminlist = db.get("room_admins_"+message.channel.id)
            var admins = []
            adminlist.forEach(admin => {
                admins.push(client.users.cache.get(admin).tag)
            })
            var admins = admins.join(", ")
        }
        let embed = new discord.MessageEmbed()
        .setAuthor("Room Permissions | " + message.author.tag, message.author.avatarURL())
        .setThumbnail("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_341049.png&f=1&nofb=1")
        .addField("Global Permissions:", `Stream: ${stream}\nSend Messages: ${sendmsg}\nEmbed Links: ${embedlinks}\nAttach Files: ${attachfiles}\nAdd Reactions: ${addreactions}\nExternal Emotes: ${externalemotes}\nSpeak: ${speak}`, true)
        .addField("Admin Permissions:", `Stream: ${streama}\nSend Messages: ${sendmsga}\nEmbed Links: ${embedlinksa}\nAttach Files: ${attachfilesa}\nAdd Reactions: ${addreactionsa}\nExternal Emotes: ${externalemotesa}\nSpeak: ${speaka}\nManage Members: ${managemembersa}\nManage Permissions: ${managepermissionsa}\nManage Messages: ${managemessagesa}\nManage Settings: ${managesettingsa}`, true)
        .addField("Admins:", admins)
        .setColor("#808080")
        .setFooter("Set permissions with \"!setpermission (group) (permission) (y/n)\"")
        message.channel.send(embed).then(msg => {
            msg.delete({timeout: 60000})
            message.delete({timeout: 60000})
        })
    }

    if (command === "visibility") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) === true) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        if (tc.permissionsFor(message.guild.roles.everyone).has("VIEW_CHANNEL")) {
            await tc.updateOverwrite(message.guild.roles.everyone, {VIEW_CHANNEL: false})
            await vc.updateOverwrite(message.guild.roles.everyone, {VIEW_CHANNEL: false})
            message.channel.send("Success, channel has been set to private!").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }else{
            await tc.updateOverwrite(message.guild.roles.everyone, {VIEW_CHANNEL: true})
            await vc.updateOverwrite(message.guild.roles.everyone, {VIEW_CHANNEL: true})
            message.channel.send("Success, channel has been set to public!").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }
    }

    if (command === "settings") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) === true) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        if (tc.topic === null) {
            var topic = "None."
        }else{
            var topic = tc.topic
        }
        if (tc.permissionsFor(message.guild.roles.everyone).has("VIEW_CHANNEL")) {
            var channeltype = "Public"
        }else{
            var channeltype = "Private"
        }
        if (tc.nsfw) {
            var nsfw = "Yes"
        }else{
            var nsfw = "No"
        }
        let embed = new discord.MessageEmbed()
        .setAuthor("Channel Settings | " + message.author.tag, message.author.avatarURL())
        .setThumbnail("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.onlinewebfonts.com%2Fsvg%2Fimg_488153.png&f=1&nofb=1")
        .setDescription("**Topic:**\n" + topic)
        .addField("Channel Name:", tc.name.slice(3), true)
        .addField("Channel Type:", channeltype, true)
        .addField("Voice Bitrate:", vc.bitrate / 1000 + " kbps", true)
        .addField("NSFW:", nsfw, true)
        .addField("Slow Mode:", tc.rateLimitPerUser+" seconds", true)
        .setFooter("View permissions with \"!permissions\".")
        .setColor("#808080")
        message.channel.send(embed).then(msg => {
            msg.delete({ timeout: 60000 })
            message.delete({ timeout: 60000 })
        })
    }

    if (command === "purge") {
        if (roomadmin) {
            if (db.get("adminp_managemessages_"+message.channel.id) === false) {
                return;
            }
        }
        if (args[0] === undefined || isNaN(args[0])) {
            message.channel.send("Didn't provide a valid amount to delete.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
        }
        await message.delete()
        await message.channel.bulkDelete(args[0])
        message.channel.send("Purged " + args[0] + " messages...").then(msg => {
            msg.delete({ timeout: 30000 })
        })
    }

    if (command === "nsfw") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) != true) {
                return;
            }
        }
        if (message.channel.nsfw) {
            await message.channel.setNSFW(false)
            message.channel.send("Channel is no longer NSFW.").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }else{
            await message.channel.setNSFW(true)
            message.channel.send("Channel is now NSFW.").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }
    }

    if (command === "slowmode") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) != true) {
                return;
            }
        }
        if (args[0] === undefined && isNaN(args[0]) === false) {
            message.channel.send("Didn't provide a valid time.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        try{
            if (args[0] > 21600) {
                message.channel.send("Can't be over 21600 seconds.").then(msg => {
                    msg.delete({ timeout: 10000 })
                    message.delete({ timeout: 10000 })
                })
                return;
            }
            await message.channel.setRateLimitPerUser(args[0])
            message.channel.send("Success, slowmode of channel has been set to " + args[0]+" seconds!").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }catch(err) {
            message.channel.send("Ran into error while setting slowmode.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            console.log(err)
            return;
        }
    }

    if (command === "topic") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) != true) {
                return;
            }
        }
        if (args[0] === undefined){
            message.channel.send("Didn't provide a valid channel topic.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        let topic = message.content.slice(command.length + 1)
        if (topic.length > 1024) {
            message.channel.send("Topic is too long...").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        try{
            await message.channel.setTopic(topic)
            message.channel.send("Success, channel topic has been set as " + topic + "!").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }catch(err) {
            message.channel.send("Ran into error while setting topic.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            console.log(err)
            return;
        }
    }

    if (command === "bitrate") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) === true) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
            }else{
                return;
            }
        }else{
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        if (args[0] === undefined || isNaN(args[0])) {
            message.channel.send("Didn't provide a valid bitrate. (8 - 96 kbps)").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        if (args[0] > 96 || args[0] < 8) {
            message.channel.send("Didn't provide a valid bitrate. (8 - 96 kbps)").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        try{
            await vc.edit({
                bitrate: args[0] * 1000
            })
            message.channel.send("Success, bitrate has been updated to " + args[0]+" kbps!").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }catch(err) {
            message.channel.send("Ran into error while setting bitrate.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            console.log(err)
            return;
        }
    }

    if (command === "rename") {
        if (roomadmin) {
            if (db.get("adminp_managesettings_"+message.channel.id) === true) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        if (args[0] === undefined) {
            message.channel.send("Didn't provide name to rename to.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        let name = S(message.content).stripLeft("!rename ").s
        if (name.length > 30) {
            message.channel.send("Name is too long.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        try{
            await tc.setName("💬┃"+name)
            await vc.setName("🔊┃"+name)
            message.channel.send("Success! Set channel name to " + name + "!").then(msg => {
                msg.delete({ timeout: 30000 })
                message.delete({ timeout: 30000 })
            })
        }catch(err) {
            message.channel.send("Ran into error while renaming room.").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            console.log(err)
            return;
        }
    }

    if (command === "ban") {
        if (roomadmin) {
            if (db.get("adminp_managemembers_"+message.channel.id) != false) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
                var owner = data[0].ID.split("_")[2]
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        let person = message.content.slice(5)
        let user = client.guilds.cache.get("899074075543105557").members.cache.find(member => member.user.tag === person)
        if (user === undefined) {
            message.channel.send("Could not find user...").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        if (db.get("room_admins_"+message.author.id) != null) {
            if (db.get("room_admins_"+message.author.id).includes(user.id) || owner === user.id) {
                return;
            }
        }
        if (user.id === message.author.id) {
            return;
        }
        await vc.updateOverwrite(user.id, {VIEW_CHANNEL: false})
        await tc.updateOverwrite(user.id, {VIEW_CHANNEL: false})
        message.channel.send(`User ${person} has been banned from your room.`).then(msg => {
            msg.delete({ timeout: 30000 })
            message.delete({ timeout: 30000 })
        })
    }

    if (command === "invite") {
        if (roomadmin) {
            if (db.get("adminp_managemembers_"+message.channel.id) != false) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
                var owner = data[0].ID.split("_")[2]
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        let person = message.content.slice(8)
        let user = client.guilds.cache.get("899074075543105557").members.cache.find(member => member.user.tag === person)
        if (user === undefined) {
            message.channel.send("Could not find user...").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        if (db.get("room_admins_"+message.author.id) != null) {
            if (db.get("room_admins_"+message.author.id).includes(user.id) || owner === user.id) {
                return;
            }
        }
        if (user.id === message.author.id) {
            return;
        }
        await vc.updateOverwrite(user.id, {VIEW_CHANNEL: true})
        await tc.updateOverwrite(user.id, {VIEW_CHANNEL: true})
        message.channel.send(`User ${person} has been added to your room.`).then(msg => {
            msg.delete({ timeout: 30000 })
            message.delete({ timeout: 30000 })
        })
    }

    if (command === "pardon") {
        if (roomadmin) {
            if (db.get("adminp_managemembers_"+message.channel.id) != false) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
                var owner = data[0].ID.split("_")[2]
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        let person = message.content.slice(8)
        let user = client.guilds.cache.get("899074075543105557").members.cache.find(member => member.user.tag === person)
        if (user === undefined) {
            message.channel.send("Could not find user...").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        if (db.get("room_admins_"+message.author.id) != null) {
            if (db.get("room_admins_"+message.author.id).includes(user.id) || owner === user.id) {
                return;
            }
        }
        if (user.id === message.author.id) {
            return;
        }
        if (vc.permissionOverwrites.get(user.id) === undefined) {
            return;
        }
        await vc.permissionOverwrites.get(user.id).delete()
        await tc.permissionOverwrites.get(user.id).delete()
        message.channel.send(`User ${person} has had their ban revoked.`).then(msg => {
            msg.delete({ timeout: 30000 })
            message.delete({ timeout: 30000 })
        })
    }

    if (command === "remove") {
        if (roomadmin) {
            if (db.get("adminp_managemembers_"+message.channel.id) != false) {
                let data = db.all().filter(filter => filter.data === '"'+message.channel.id+'"')
                if (data[0] === undefined) {
                    return;
                }
                var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${data[0].ID.split("_")[2]}`))
                var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${data[0].ID.split("_")[2]}`))
                var owner = data[0].ID.split("_")[2]
            }else{
                return;
            }
        }else{
            var tc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_tc_${message.author.id}`))
            var vc = client.guilds.cache.get("899074075543105557").channels.cache.get(db.get(`room_vc_${message.author.id}`))
        }
        let person = message.content.slice(8)
        let user = client.guilds.cache.get("899074075543105557").members.cache.find(member => member.user.tag === person)
        if (user === undefined) {
            message.channel.send("Could not find user...").then(msg => {
                msg.delete({ timeout: 10000 })
                message.delete({ timeout: 10000 })
            })
            return;
        }
        if (db.get("room_admins_"+message.author.id) != null) {
            if (db.get("room_admins_"+message.author.id).includes(user.id) || owner === user.id) {
                return;
            }
        }
        if (user.id === message.author.id) {
            return;
        }
        if (vc.permissionOverwrites.get(user.id) === undefined) {
            return;
        }
        await vc.permissionOverwrites.get(user.id).delete()
        await tc.permissionOverwrites.get(user.id).delete()
        message.channel.send(`User ${person} has been removed to your room.`).then(msg => {
            msg.delete({ timeout: 30000 })
            message.delete({ timeout: 30000 })
        })
    }

    if (command === "delete") {
        if (roomadmin) {
            return;
        }
        let data = db.all().filter(data => data.data.includes(message.channel.id) && data.ID.includes(message.author.id))
        if (data.length === 0) {
            return;
        }
        message.channel.send("Are you sure you want to delete your room?").then(async msg => {
            msg.awaitReactions((reaction, user) => {
                return(
                    ["✅", "❌"].includes(reaction.emoji.name) && user.id === message.author.id
                )
            }, {max: 1, time: 60000, errors: ['time']}).then(async (collected) => {
                if (collected.first().emoji.name === "✅") {
                    db.delete(`room_tc_${message.author.id}`)
                    await collected.first().message.guild.channels.cache.get(await db.get(`room_vc_${message.author.id}`)).delete()
                    db.delete(`room_vc_${message.author.id}`)
                    await collected.first().message.guild.channels.cache.get(await db.get(`room_cg_${message.author.id}`)).delete()
                    db.delete(`room_cg_${message.author.id}`)
                    message.channel.delete()
                }else{
                    msg.reactions.removeAll()
                    msg.edit("Room deletion cancelled...").then(msg => {
                        msg.delete({ timeout: 10000 })
                        message.delete({ timeout: 10000 })
                    })
                }
            }).catch(() => {
                msg.reactions.removeAll()
                msg.edit("Room deletion timed out...").then(msg => {
                    msg.delete({ timeout: 10000 })
                    message.delete({ timeout: 10000 })
                })
            })
            msg.react("✅")
            await sleep(1000)
            msg.react("❌")
        })
    }
})

//
// CLIENT LOGIN
//

client.on("error", (e) => {
    console.error(e)
});
client.on("warn", (e) => {
    console.warn(e)
});
client.on("debug", (e) => {
    if (e.includes("429 hit on route ")) {
        let data = db.all().filter(data => data.data.includes(S(e).between("/channels/").s))
        if (data.length === 0) {
            console.log("Could not find user that triggered " + e+"...")
            return;
        }
        let user = client.users.cache.get(data[0].ID.split("_")[2])
        user.send("You've changed your channel settings too quickly and have been put on a 10 minute cooldown. Please avoid making so many changes at once!")
        console.log(user.tag + " has been sent an alert for hitting 429 rate limit and is now on cooldown.")
        cooldown.add(user.id)
        setTimeout(() => {
            cooldown.delete(user.id)
            console.log(user.tag + " cooldown has been removed.")
            user.send("10 minute cooldown is now over.")
        }, 600000)
    }
    console.debug(e)
});
client.on("rateLimit", (e) => {
    console.warn(e)
});
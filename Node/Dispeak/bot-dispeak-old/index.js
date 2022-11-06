//Main file dependencies
const version = 'v0.13'
const discord = require('discord.js')
const client = new discord.Client()
const db = require('quick.db')
const S = require('string')
const fs = require('fs')
const prefix = '!'
const help = '822652236052168755'
const array = []
const channels = []
const timer = []
const stafflog = new discord.WebhookClient('822653427657474069', 'jLSefsd9mU3HKSlrC8FY_a3JjwOyHjx4s28iVT3TadLo9QFbXGV_B4dagOFbFHDMM7NH')
function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
}
const locked = false

//Discord.js Ready Up
client.on('ready', async () => {
    if (locked === true) {
        client.channels.cache.get('810240019528155158').messages.fetch('826284986470498335')
        return;
    }
    try{
        var notify = new discord.MessageEmbed()
        .setTitle('Notification Roles')
        .setDescription('🟡 - Small Patches Notifications\n🟠 - Release Notifications\n🔴 - Bot Downtime Notifications')
        .setColor('#0000ff')
        client.channels.cache.get('828815578465697814').messages.fetch('828816445248110613').then(async msg => {
            msg.edit(notify)
            await msg.react('🟡')
            await msg.react('🟠')
            await msg.react('🔴')
        })
        client.setInterval(() => {
            client.guilds.cache.get('810229320177942548').channels.cache.forEach(() => {channels.push('1')})
            var currentusage = new discord.MessageEmbed()
            .setTitle('Current Room Usage')
            .addField('Discord Channels Limit', channels.length + '/500 channels')
            .addField('Bot Room Limit', db.fetchAll().length + '/120 rooms')
            .setColor('#0000ff')
            .setTimestamp()
            .setFooter('Last Updated')
            client.channels.cache.get('810240019528155158').messages.fetch('826281243816755210').then(msg => {
                msg.edit(currentusage)
                channels.splice(0, 9999)
            })
        }, 10000)
        client.user.setActivity('DMs! (' + version + ')', {type: 'LISTENING'})
        var createroom = new discord.MessageEmbed()
        .setTitle('Create a room!')
        .setDescription('Click the reaction below to create a room! Make sure you\'ve read the <#810233171361792100> before getting started!')
        .setColor('#0000ff')
        client.channels.cache.get('810240019528155158').messages.fetch('826284986470498335').then(msg => {
            msg.edit(createroom)
            msg.react('📎')
        })
        var rules = new discord.MessageEmbed()
        .setTitle('Discord Rules')
        .setDescription('All Discord ToS/Community Guideline\'s rules apply here. Please review them at: __https://discordapp.com/terms__ and __https://discordapp.com/guidelines__\n\nDisclosure: The staff team may look into private rooms if a report is receieved or suspicious activity is detected.')
        .addField('Rule 1:', "Spamming is not allowed, even in private rooms! (it slows down the discord server)")
        .addField('Rule 2:', "Public rooms are expected to keep everything PG-13 unless the channel is marked NSFW.")
        .addField('Rule 3:', "Do not attempt to keep a rooms open. (they close for a reason)")
        .addField('Rule 4:', "Advertising other discord servers is not permitted. (even through DMs)")
        .addField('Rule 5:', "Abuse of the bots to ratelimit, lag them, or cause any damage to the discord is not allowed. (if you find a bug, report it)")
        .addField('Rule 6:', "Do not DM at staff member directly unless you know they are okay with it. If you need help with something or wish to report someone, please DM the Dispeak bot which will notify the staff team.")
        .setColor('#ff0000')
        client.channels.cache.get('810233171361792100').messages.fetch('810241625003261993').then(msg => {
            msg.edit(rules)
        })
        var info = new discord.MessageEmbed()
        .setTitle('Discord Info')
        .setDescription('Some general information and answers for commonly asked questions.')
        .addField('I need help or want to report someone!', "You can send me a DM at anytime and I will notify the staff team who can assist you further!")
        .addField('How can I manage my room?', 'You can find a list of commands by using "!cmds" and "!tips" in you\'re console room!')
        .addField('What does adding someone as a room admin do?', 'Room admins are people you trust and who can assist you in taking care of your room. They can ban, delete messages, mute members, etc... and are generally there to help you out.')
        .addField('Is my private room really private?', 'For the most part, yes. Staff members can forcefully join rooms though if a report is recieve or an alert is triggered in the bot. We also keep room logs which contain any conversations that go on in your text channels. These, however, are only accessed if something has been brought to our attention.')
        .setColor('#0000ff')
        client.channels.cache.get('810233171361792100').messages.fetch('813868498903105596').then(msg => {
            msg.edit(info)
        })
}catch(err) {
    console.error(`An issue occured while doing discord.js ready event. ${err}`)
}
})

//Discord.js Message Reaction Remove
client.on('messageReactionRemove', async (react, user) => {
    if (locked === true) {
        var dev = client.guilds.cache.get('810229320177942548').roles.cache.get('810232294333612032')
        if (client.guilds.cache.get('810229320177942548').members.cache.get(user.id).roles.cache.has(dev.id) === false) {
            return;
        }
    }
    if (react.message.id === '828816445248110613') {
        if (react.emoji.name === '🟡') {
            var spn = client.guilds.cache.get('810229320177942548').roles.cache.get('829091599030943764')
            var member = client.guilds.cache.get('810229320177942548').members.cache.get(user.id)
            member.roles.remove(spn.id)
        }
        if (react.emoji.name === '🟠') {
            var rn = client.guilds.cache.get('810229320177942548').roles.cache.get('829091724571312159')
            var member = client.guilds.cache.get('810229320177942548').members.cache.get(user.id)
            member.roles.remove(rn.id)
        }
        if (react.emoji.name === '🔴') {
            var dn = client.guilds.cache.get('810229320177942548').roles.cache.get('829091752492138526')
            var member = client.guilds.cache.get('810229320177942548').members.cache.get(user.id)
            member.roles.remove(dn.id)
        }
    }
})

//Discord.js Message Reaction Add
client.on('messageReactionAdd', async (react, user) => {
    if (locked === true) {
        var dev = client.guilds.cache.get('810229320177942548').roles.cache.get('810232294333612032')
        if (client.guilds.cache.get('810229320177942548').members.cache.get(user.id).roles.cache.has(dev.id) === false) {
            return;
        }
    }
    try{
        if (user.id != '664308359414939648') {
            if (react.message.id === '828816445248110613') {
                if (react.emoji.name === '🟡') {
                    var spn = client.guilds.cache.get('810229320177942548').roles.cache.get('829091599030943764')
                    var member = client.guilds.cache.get('810229320177942548').members.cache.get(user.id)
                    member.roles.add(spn.id)
                }
                if (react.emoji.name === '🟠') {
                    var rn = client.guilds.cache.get('810229320177942548').roles.cache.get('829091724571312159')
                    var member = client.guilds.cache.get('810229320177942548').members.cache.get(user.id)
                    member.roles.add(rn.id)
                }
                if (react.emoji.name === '🔴') {
                    var dn = client.guilds.cache.get('810229320177942548').roles.cache.get('829091752492138526')
                    var member = client.guilds.cache.get('810229320177942548').members.cache.get(user.id)
                    member.roles.add(dn.id)
                }
            }
            if (react.message.id === `826284986470498335`) {
                await react.message.reactions.removeAll();
                await sleep(1000)
                await react.message.react('📎')
                if (db.fetchAll().length > 120 || db.fetchAll().length === 120) {
                    var errortoomanyrooms = new discord.MessageEmbed()
                    .setAuthor(user.tag, user.avatarURL())
                    .setDescription('Too many rooms are currently active!')
                    .setColor('#ff0000')
                    react.message.channel.send(errortoomanyrooms).then((msg) => {
                        msg.delete({timeout: 5000})
                        return;
                    })
                }
                if (!db.get(`${user.id}_room`)) {
                    await react.message.guild.channels.create(`${user.tag}'s Room`, {type: 'category'}).then(async (cat) => {
                        var cmds = await react.message.guild.channels.create(`🤖｜${user.username}-console`, {type: 'text'})
                        await cmds.setParent(cat.id)
                        var text = await react.message.guild.channels.create(`💬｜${user.username}-general`, {type: 'text'})
                        await text.setParent(cat.id)
                        var vc = await react.message.guild.channels.create(`🔊｜${user.username}-vc`, {type: 'voice'})
                        await vc.setParent(cat.id)
                        await cmds.overwritePermissions([
                            {
                                id: user.id,
                                allow: ['VIEW_CHANNEL', 'MANAGE_MESSAGES', 'MENTION_EVERYONE', 'SEND_TTS_MESSAGES']
                            },
                            {
                                id: react.message.guild.roles.everyone,
                                deny: ['VIEW_CHANNEL']
                            }
                        ])
                        await text.overwritePermissions([
                            {
                                id: user.id,
                                allow: ['VIEW_CHANNEL', 'MANAGE_MESSAGES', 'MENTION_EVERYONE', 'SEND_TTS_MESSAGES']
                            },
                            {
                                id: react.message.guild.roles.everyone,
                                deny: ['VIEW_CHANNEL']
                            }
                        ])
                        await vc.overwritePermissions([
                            {
                                id: user.id,
                                allow: ['VIEW_CHANNEL', 'PRIORITY_SPEAKER','DEAFEN_MEMBERS', 'MUTE_MEMBERS', 'MOVE_MEMBERS', 'KICK_MEMBERS']
                            },
                            {
                                id: react.message.guild.roles.everyone,
                                deny: ['VIEW_CHANNEL']
                            }
                        ])
                        db.push(`${user.id}_room`,'Visibility1: Private :Visibility2')
                        db.push(`${user.id}_room`, `Owner1: ${user.id} :Owner2`)
                        db.push(`${user.id}_room`, `CC1: ${cat.id} :CC2`)
                        db.push(`${user.id}_room`, `CT1: ${cmds.id} :CT2`)
                        db.push(`${user.id}_room`, `GT1: ${text.id} :GT2`)
                        db.push(`${user.id}_room`, `VC1: ${vc.id} :VC2`)
                        var roomCreated = new discord.MessageEmbed()
                        .setAuthor(user.tag, user.avatarURL())
                        .setDescription(`Your room has been created!`)
                        .setColor('#00ff00')
                        await react.message.channel.send(roomCreated).then((msg) => {
                            msg.delete({timeout: 5000})
                        })
                        var embed = new discord.MessageEmbed()
                        .setTitle('Welcome to your own personal room!')
                        .setDescription('Thanks for creating a room! I am a bot that will assist you as you set up your room! \n\nTo see a list of commands, simply type !cmds and if you need more help, check out !tips!')
                        .setColor('#00ff00')
                        cmds.send(embed)
                    })
                }else{
                    var errorcreate = new discord.MessageEmbed()
                    .setAuthor(user.tag, user.avatarURL())
                    .setDescription('Looks like you already own a room!')
                    .setColor('#ff0000')
                    react.message.channel.send(errorcreate).then((msg) => {
                        msg.delete({timeout: 5000})
                    })
                }
            }
        }
}catch(err) {
    var errorcreate2 = new discord.MessageEmbed()
    .setAuthor(user.tag, user.avatarURL())
    .setDescription('It appears the bot has ran into an error whilst creating your room...')
    .addField('Error', err)
    .setColor('#ff0000')
    react.message.channel.send(errorcreate2).then((msg) => {
        msg.delete({timeout: 5000})
    })
    console.error(err)
}
})

//Discord.js Message Event
client.on('message', async (message) => {
    if (locked === true) {
        var dev = client.guilds.cache.get('810229320177942548').roles.cache.get('810232294333612032')
        if (message.member === null) {
            return;
        }
        if (client.guilds.cache.get('810229320177942548').members.cache.get(message.author.id).roles.cache.has(dev.id) === false) {
            return;
        }
    }
    try{
        if (message.content === '!d bump') {
            if (message.channel.id === '810233171361792101') {
                if (timer.length === 0) {
                    message.channel.send('Will notify when 120 minutes has passed.')
                    timer.push('A')
                    client.setTimeout(() => {
                        message.channel.send('Hey @everyone, bump it.')
                        timer.pop()
                    }, 7200000)
                }else{
                    message.channel.send('Can\'t bump yet!')
                }
            }
        }
        if (message.channel.type === 'dm') {
            if (message.author.id != '664308359414939648') {
                var pmsg = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription(message.content)
                .setFooter('Use !reply (user#0001) to respond.')
                .setColor('#008000')
                client.channels.cache.get(help).send(pmsg)
                var msg = new discord.MessageEmbed()
                .setTitle('Message sent to staff!')
                .setDescription('Your message was sent to the staff team! They will respond soon.')
                .setColor('#0000ff')
                message.channel.send(msg)
            }
        }
        if (!message.content.startsWith(prefix) || message.author.bot) return;
        const args = message.content.slice(prefix.length).trim().split(/ +/g);
        const command = args.shift().toLowerCase();
        if (command === 'reply') {
            if (message.member.roles.cache.has(message.guild.roles.cache.get('810233379374891048').id)) {
                if (!args[0]) {
                    var replynouser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('You did not provide a user!')
                    .setColor('#ff0000')
                    message.channel.send(replynouser)
                }else{
                    try{
                        var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                    }catch(err){
                        var replyinvaliduser = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('This is not a valid user!')
                        .setColor('#ff0000')
                        message.channel.send(replyinvaliduser)
                    }
                    var content = message.content.slice(args[0].length + 8)
                    var msg = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription(content)
                    .setColor('#008000')
                    user.send(msg)
                    message.react('✅')
                }
            }
        }
        if (command === 'dev') {
            if (message.author.id === '664280873503555614') {
                if (args[0] === 'check') {
                    if (!args[1]) {
                        var devchecknouser = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You did not provide a user!')
                        .setColor('#ff0000')
                        message.author.send(devchecknouser)
                        message.delete()
                    }else{
                        try{
                            var user = message.guild.members.cache.find(user => user.user.tag === args[1])
                        }catch(err){
                            var devcheckinvaliduser = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('Invalid user. (example: Username#0001)')
                            .setColor('#ff0000')
                            message.author.send(devcheckinvaliduser)
                            message.delete()
                        }
                        var data = await db.get(`${user.id}_room`)
                        if (!data) {
                            var devchecknoroom = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('That user doesn\'t own a room!')
                            .setColor('#ff0000')
                            message.author.send(devchecknoroom)
                            message.delete()
                        }else{
                            var devcheck = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .addField('Raw Database Output:', `${data}`)
                            .setColor('#00ff00')
                            message.author.send(devcheck)
                            message.delete()
                        }
                    }
                }else if (args[0] === 'allperms') {
                    var allpermsrole = client.guilds.cache.get('810229320177942548').roles.cache.get('810237398096674836')
                    if (message.member.roles.cache.has(allpermsrole.id)) {
                        message.member.roles.remove(allpermsrole.id)
                        message.delete()
                    }else{
                        message.member.roles.add(allpermsrole.id)
                        message.delete()
                    }
                }
            }else{
                var devnocmd = new discord.MessageEmbed()
                .setAuthor(user.tag, user.avatarURL())
                .setDescription('It doesn\'t appear a command of that type exists!')
                .setColor('#ff0000')
                message.channel.send(devnocmd)
            }
        }
        if (command === 'staff') {
            if (client.guilds.cache.get('810229320177942548').members.cache.get(message.author.id).roles.cache.has(client.guilds.cache.get('810229320177942548').roles.cache.get('810233379374891048').id)) {
                message.delete()
                if (args[0] === 'grant') {
                    if (!args[1]) {
                        var staffgrantnouser = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('No user provided! (example: Username#0001)')
                        .setColor('#ff0000')
                        message.channel.send(staffgrantnouser)
                    }else{
                        try{
                            var user = client.guilds.cache.get('810229320177942548').members.cache.find(user => user.user.tag === args[1])
                        }catch(err){
                            var staffgrantinvaliduser = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('Invalid user! (example: Username#0001)')
                            .setColor('#ff0000')
                            message.channel.send(staffgrantinvaliduser)
                        }
                        var data = await db.get(`${user.id}_room`)
                        if (!data) {
                            var staffgrantnoroom = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('This user doesn\'t have a room!')
                            .setColor('#ff0000')
                            message.channel.send(staffgrantnoroom)
                        }else{
                            var Owner = S(data).between("Owner1: ", " :Owner2").s
                            var CT = S(data).between("CT1: ", " :CT2").s
                            var GT = S(data).between("GT1: ", " :GT2").s
                            var VC = S(data).between("VC1: ", " :VC2").s
                            client.guilds.cache.get('810229320177942548').channels.cache.get(CT).updateOverwrite(message.author.id, { VIEW_CHANNEL: true})
                            client.guilds.cache.get('810229320177942548').channels.cache.get(GT).updateOverwrite(message.author.id, { VIEW_CHANNEL: true})
                            client.guilds.cache.get('810229320177942548').channels.cache.get(VC).updateOverwrite(message.author.id, { VIEW_CHANNEL: true})
                            var member = client.guilds.cache.get('810229320177942548').members.cache.get(Owner)
                            var modcheck = new discord.MessageEmbed()
                            .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                            .setDescription('Granted access to ' + member.user.tag + '\'s room!')
                            .setColor('#00ff00')
                            message.author.send(modcheck)
                            var modchecklog = new discord.MessageEmbed()
                            .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                            .setDescription(`${message.author.tag} has granted themselves access to ${member.user.tag}'s room.`)
                            .setColor('#ffa500')
                            stafflog.send(modchecklog)
                        }
                    }
                }else if (args[0] === 'revoke') {
                    if (!args[1]) {
                        var staffrevokenouser = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('No user provided! (example: Username#0001)')
                        .setColor('#ff0000')
                        message.channel.send(staffrevokenouser)
                    }else{
                        try{
                            var user = client.guilds.cache.get('810229320177942548').members.cache.find(user => user.user.tag === args[1])
                        }catch(err){
                            var staffrevokeinvaliduser = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('Invalid user! (example: Username#0001)')
                            .setColor('#ff0000')
                            message.channel.send(staffrevokeinvaliduser)
                        }
                        var data = await db.get(`${user.id}_room`)
                        if (!data) {
                            var staffrevokenoroom = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('This user doesn\'t have a room!')
                            .setColor('#ff0000')
                            message.channel.send(staffrevokenoroom)
                        }else{
                            var Owner = S(data).between("Owner1: ", " :Owner2").s
                            var CT = S(data).between("CT1: ", " :CT2").s
                            var GT = S(data).between("GT1: ", " :GT2").s
                            var VC = S(data).between("VC1: ", " :VC2").s
                            client.guilds.cache.get('810229320177942548').channels.cache.get(CT).permissionOverwrites.get(message.author.id).delete()
                            client.guilds.cache.get('810229320177942548').channels.cache.get(GT).permissionOverwrites.get(message.author.id).delete()
                            client.guilds.cache.get('810229320177942548').channels.cache.get(VC).permissionOverwrites.get(message.author.id).delete()
                            var member = client.guilds.cache.get('810229320177942548').members.cache.get(Owner)
                            var modrevoke = new discord.MessageEmbed()
                            .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                            .setDescription('Revoked access to ' + member.user.tag + '\'s room!')
                            .setColor('#ff0000')
                            message.author.send(modrevoke)
                            var modrevokelog = new discord.MessageEmbed()
                            .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                            .setDescription(`${message.author.tag} has ran mod revoke and removed their access to ${member.user.tag}'s room.`)
                            .setColor('#ffa500')
                            stafflog.send(modrevokelog)
                        }
                    }
                }else if (args[0] === 'delete') {
                    if (!args[1]) {
                        var staffdeletenouser = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('No user provided! (example: Username#0001)')
                        .setColor('#ff0000')
                        message.channel.send(staffdeletenouser)
                    }else{
                        try{
                            var user = client.guilds.cache.get('810229320177942548').members.cache.find(user => user.user.tag === args[1])
                        }catch(err){
                            var staffdeleteinvaliduser = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('Invalid user! (example: Username#0001)')
                            .setColor('#ff0000')
                            message.channel.send(staffdeleteinvaliduser)
                        }
                        var data = await db.get(`${user.id}_room`)
                        if (data === null) {
                            var staffdeletenoroom = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('This user doesn\'t have a room!')
                            .setColor('#ff0000')
                            message.channel.send(staffdeletenoroom)
                        }else{
                            var Owner = S(data).between("Owner1: ", " :Owner2").s
                            var CC = S(data).between("CC1: ", " :CC2").s
                            var CT = S(data).between("CT1: ", " :CT2").s
                            var GT = S(data).between("GT1: ", " :GT2").s
                            var VC = S(data).between("VC1: ", " :VC2").s
                            var member = client.guilds.cache.get('810229320177942548').members.cache.get(Owner)
                            var moddelete = new discord.MessageEmbed()
                            .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                            .setDescription('Deleted ' + member.user.tag + '\'s room!')
                            .setColor('#ff0000')
                            await message.author.send(moddelete)
                            var moddeletelog = new discord.MessageEmbed()
                            .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                            .setDescription(`${message.author.tag} deleted ${member.user.tag}'s room.`)
                            .setColor('#ffa500')
                            stafflog.send(moddeletelog)
                            client.guilds.cache.get('810229320177942548').channels.cache.get(VC).delete()
                            await sleep(500)
                            client.guilds.cache.get('810229320177942548').channels.cache.get(GT).delete()
                            await sleep(500)
                            client.guilds.cache.get('810229320177942548').channels.cache.get(CT).delete()
                            await sleep(500)
                            client.guilds.cache.get('810229320177942548').channels.cache.get(CC).delete()
                            db.delete(`${user.id}_room`)
                        }
                    }
                }else{
                    var staffinvalidcmd = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('That command doesn\'t exist!')
                    .setColor('#ff0000')
                    message.author.send(staffinvalidcmd)
                }
            }
        }
    db.fetchAll(message.channel.id).forEach(J => {
        if (S(J.data).include(message.channel.id)) {
            array.push(J.ID)
        }})
        if (array.length > 0) {
            var room = array.pop()
            var room2 = await db.get(room)
            var ctroom = S(await db.get(room)).between("CT1: ", " :CT2").s
            var authorroom = S(await db.get(room)).between("Owner1: ", " :Owner2").collapseWhitespace().s
            if (authorroom != message.author.id) {
                if (ctroom === message.channel.id) {
                    var check = true
                }
            }
        }
        if (room2 === undefined) {
            var room2 = 'none'
        }
    if (S(await db.get(`${message.author.id}_room`)).between("CT1: ", " :CT2").s === message.channel.id || S(room2).between("CT1: ", " :CT2").s === message.channel.id || check === true) {
        if (command === 'admin') {
            if (check === true) {
                var adminadminonly = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('Room admins can\'t run this command!')
                .setColor('#ff0000')
                message.channel.send(adminadminonly)
                return;
            }
            if (!args[0]) {
                var adminnouser = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('No user provided! (example: Username#0001)')
                .setColor('#ff0000')
                message.channel.send(adminnouser)
            }else{
                try{
                    var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                }catch(err){
                    var admininvaliduser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Invalid user! (example: Username#0001)')
                    .setColor('#ff0000')
                    message.channel.send(admininvaliduser)
                }
                var data = await db.get(`${message.author.id}_room`)
                if (!data) {
                    var adminnoroom = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('You don\'t have a room!')
                    .setColor('#ff0000')
                    message.channel.send(adminnoroom)
                }else{
                    var Owner = S(data).between("Owner1: ", " :Owner2").collapseWhitespace().s
                    var CT = S(data).between("CT1: ", " :CT2").s
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    if (user.user.id === Owner) {
                        var adminalreadyowner = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You are already the owner of this room!')
                        .setColor('#ff0000')
                        message.channel.send(adminalreadyowner)
                        return;
                    }
                    message.guild.channels.cache.get(CT).updateOverwrite(user.user.id, { VIEW_CHANNEL: true})
                    message.guild.channels.cache.get(GT).updateOverwrite(user.user.id, { VIEW_CHANNEL: true, MANAGE_MESSAGES: true, MENTION_EVERYONE: true, SEND_TTS_MESSAGES: true})
                    message.guild.channels.cache.get(VC).updateOverwrite(user.user.id, { VIEW_CHANNEL: true, PRIORITY_SPEAKER: true, DEAFEN_MEMBERS: true, MUTE_MEMBERS: true, MOVE_MEMBERS: true, KICK_MEMBERS: true})
                    var member = message.guild.members.cache.get(Owner)
                    var admin = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Added ${user.user.tag} as a room admin of ${message.author.tag}'s room.`)
                    .setColor('#00ff00')
                    message.channel.send(admin)
                    var adminlog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} added ${user.user.tag} as a room admin of their room.`)
                    .setColor('#ffa500')
                    stafflog.send(adminlog)
                }
            }
        }
        if (command === 'unadmin') {
            if (check === true) {
                var unadminadminonly = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('Room admins can\'t run this command!')
                .setColor('#ff0000')
                message.channel.send(unadminadminonly)
                return;
            }
            if (!args[0]) {
                var unadminnouser = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('No user provided! (example: Username#0001)')
                .setColor('#ff0000')
                message.channel.send(unadminnouser)
            }else{
                try{
                    var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                }catch(err){
                    var unadmininvaliduser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Invalid user! (example: Username#0001)')
                    .setColor('#ff0000')
                    message.channel.send(unadmininvaliduser)
                }
                var data = await db.get(`${message.author.id}_room`)
                if (!data) {
                    var unadminnoroom = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('You don\'t have a room!')
                    .setColor('#ff0000')
                    message.channel.send(unadminnoroom)
                }else{
                    var Owner = S(data).between("Owner1: ", " :Owner2").collapseWhitespace().s
                    var CT = S(data).between("CT1: ", " :CT2").s
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    if (user.user.id === Owner) {
                        var unadminowner = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You are the owner of this room!')
                        .setColor('#ff0000')
                        message.channel.send(unadminowner)
                        return;
                    }
                    message.guild.channels.cache.get(CT).updateOverwrite(user.user.id, { VIEW_CHANNEL: false})
                    message.guild.channels.cache.get(GT).updateOverwrite(user.user.id, { VIEW_CHANNEL: true, MANAGE_MESSAGES: false, MENTION_EVERYONE: false, SEND_TTS_MESSAGES: false})
                    message.guild.channels.cache.get(VC).updateOverwrite(user.user.id, { VIEW_CHANNEL: true, PRIORITY_SPEAKER: false, DEAFEN_MEMBERS: false, MUTE_MEMBERS: false, MOVE_MEMBERS: false, KICK_MEMBERS: false})
                    var member = message.guild.members.cache.get(Owner)
                    var admin = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Removed ${user.user.tag} as a room admin of ${message.author.tag}'s room.`)
                    .setColor('#ff0000')
                    message.channel.send(admin)
                    var adminlog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} removed ${user.user.tag} as a room admin of their room.`)
                    .setColor('#ffa500')
                    stafflog.send(adminlog)
                }
            }
        }
        if (command === 'delete') {
            if (check === true) {
                var deleteadminonly = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('Room admins can\'t run this command!')
                .setColor('#ff0000')
                message.channel.send(deleteadminonly)
                return;
            }
            var data = await db.get(`${message.author.id}_room`)
            if (data === null) {
                var deletenoroom = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('You don\'t have a room!')
                .setColor('#ff0000')
                message.channel.send(deletenoroom)
            }else{
                var deletee = new discord.MessageEmbed()
                .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                .setDescription(`You're room has been deleted!`)
                .setColor('#ff0000')
                await message.channel.send(deletee)
                var deletelog = new discord.MessageEmbed()
                .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                .setDescription(`${message.author.tag} deleted their room.`)
                .setColor('#ffa500')
                stafflog.send(deletelog)
                var CC = S(data).between("CC1: ", " :CC2").s
                var CT = S(data).between("CT1: ", " :CT2").s
                var GT = S(data).between("GT1: ", " :GT2").s
                var VC = S(data).between("VC1: ", " :VC2").s
                message.guild.channels.cache.get(VC).delete()
                await sleep(500)
                message.guild.channels.cache.get(GT).delete()
                await sleep(500)
                message.guild.channels.cache.get(CT).delete()
                await sleep(500)
                message.guild.channels.cache.get(CC).delete()
                db.delete(`${message.author.id}_room`)
            }
        }
        if (command === 'ban') {
            if (!args[0]) {
                var bannouser = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('No user provided! (example: Username#0001)')
                .setColor('#ff0000')
                message.channel.send(bannouser)
            }else{
                try{
                    var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                }catch(err){
                    var baninvaliduser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Invalid user! (example: Username#0001)')
                    .setColor('#ff0000')
                    message.channel.send(baninvaliduser)
                }
                if (check === true) {
                    var data = await db.get(room)
                    if (!data) {
                        var bannoroomadmin = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('Admin room does not exist!')
                        .setColor('#ff0000')
                        message.channel.send(bannoroomadmin)
                        return;
                    }
                }else{
                    var data = await db.get(`${message.author.id}_room`)
                    if (!data) {
                        var bannoroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You don\'t have a room!')
                        .setColor('#ff0000')
                        message.channel.send(bannoroom)
                        return;
                    }
                }
                if (S(await db.get(`${message.author.id}_room`)).between('Visibility1:', ':Visibility2').collapseWhitespace().s === 'Private') {
                    var banprivate = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Can\'t run this command in a private room!')
                    .setColor('#ff0000')
                    message.channel.send(banprivate)
                    return;
                }
                    var Owner = S(data).between("Owner1: ", " :Owner2").collapseWhitespace().s
                    var CT = S(data).between("CT1: ", " :CT2").s
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    if (user.user.id === Owner) {
                        var banownerroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t ban the owner!')
                        .setColor('#ff0000')
                        message.channel.send(banownerroom)
                        return;
                    }
                    if (user.user.id === message.author.id) {
                        var banselfroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t ban yourself!')
                        .setColor('#ff0000')
                        message.channel.send(banselfroom)
                        return;
                    }
                    message.guild.channels.cache.get(CT).updateOverwrite(user.user.id, { VIEW_CHANNEL: false})
                    message.guild.channels.cache.get(GT).updateOverwrite(user.user.id, { VIEW_CHANNEL: false})
                    message.guild.channels.cache.get(VC).updateOverwrite(user.user.id, { VIEW_CHANNEL: false})
                    var member = message.guild.members.cache.get(Owner)
                    var ban = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Banned ${user.user.tag} from room.`)
                    .setColor('#00ff00')
                    message.channel.send(ban)
                    var banlog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} banned ${user.user.tag} from their room.`)
                    .setColor('#ffa500')
                    stafflog.send(banlog)
                }
        }
        if (command === 'pardon') {
            if (!args[0]) {
                var pardonnouser = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('No user provided! (example: Username#0001)')
                .setColor('#ff0000')
                message.channel.send(pardonnouser)
            }else{
                try{
                    var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                }catch(err){
                    var pardoninvaliduser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Invalid user! (example: Username#0001)')
                    .setColor('#ff0000')
                    message.channel.send(pardoninvaliduser)
                }
                if (check === true) {
                    var data = await db.get(room)
                    if (!data) {
                        var pardonnoroomadmin = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('Admin room does not exist!')
                        .setColor('#ff0000')
                        message.channel.send(pardonnoroomadmin)
                        return;
                    }
                }else{
                    var data = await db.get(`${message.author.id}_room`)
                    if (!data) {
                        var pardonnoroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You don\'t have a room!')
                        .setColor('#ff0000')
                        message.channel.send(pardonnoroom)
                        return;
                    }
                }
                if (S(await db.get(`${message.author.id}_room`)).between('Visibility1:', ':Visibility2').collapseWhitespace().s === 'Private') {
                    var pardonprivate = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Can\'t run this command in a private room!')
                    .setColor('#ff0000')
                    message.channel.send(pardonprivate)
                    return;
                }
                    var Owner = S(data).between("Owner1: ", " :Owner2").collapseWhitespace().s
                    var CT = S(data).between("CT1: ", " :CT2").s
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    if (user.user.id === Owner) {
                        var pardonownerroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t pardon the owner!')
                        .setColor('#ff0000')
                        message.channel.send(pardonownerroom)
                        return;
                    }
                    if (user.user.id === message.author.id) {
                        var pardonselfroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t pardon yourself!')
                        .setColor('#ff0000')
                        message.channel.send(pardonselfroom)
                        return;
                    }
                    message.guild.channels.cache.get(CT).permissionOverwrites.get(user.id).delete()
                    message.guild.channels.cache.get(GT).permissionOverwrites.get(user.id).delete()
                    message.guild.channels.cache.get(VC).permissionOverwrites.get(user.id).delete()
                    var member = message.guild.members.cache.get(Owner)
                    var pardon = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Removed room ban of ${user.user.tag}.`)
                    .setColor('#00ff00')
                    message.channel.send(pardon)
                    var pardonlog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} unbanned ${user.user.tag} from their room.`)
                    .setColor('#ffa500')
                    stafflog.send(pardonlog)
            }
        }
        if (command === 'visibility') {
            if (check === true) {
                var visibilityadminonly = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('Room admins can\'t run this command!')
                .setColor('#ff0000')
                message.channel.send(visibilityadminonly)
                return;
            }
            var data = await db.get(`${message.author.id}_room`)
            if (data === null) {
                var visibilitynoroom = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('You don\'t have a room!')
                .setColor('#ff0000')
                message.channel.send(visibilitynoroom)
                return;
            }else{
                if (!args[0]) {
                    var visibilitynoroom = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('No visibility provided! (Private/Public)')
                    .setColor('#ff0000')
                    message.channel.send(visibilitynoroom)
                }else{
                    var Owner = S(data).between("Owner1:", ":Owner2").collapseWhitespace().s
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var GTD = client.guilds.cache.get('810229320177942548').channels.cache.get(GT)
                    var VC = S(data).between("VC1: ", " :VC2").s
                    var VCD = client.guilds.cache.get('810229320177942548').channels.cache.get(VC)
                    if (args[0] === 'public') {
                        if (S(await db.get(`${message.author.id}_room`)).between('Visibility1:', ':Visibility2').collapseWhitespace().s === 'Public') {
                            var visibilitynoroom = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('Room is already public!')
                            .setColor('#ff0000')
                            message.channel.send(visibilitynoroom)
                            return;
                        }
                        GTD.overwritePermissions([
                            {
                                id: Owner,
                                allow: ['VIEW_CHANNEL', 'MANAGE_MESSAGES', 'MENTION_EVERYONE', 'SEND_TTS_MESSAGES']
                            },
                            {
                                id: message.guild.roles.everyone,
                                allow: ['VIEW_CHANNEL']
                            }
                        ])
                        VCD.overwritePermissions([
                            {
                                id: Owner,
                                allow: ['VIEW_CHANNEL', 'PRIORITY_SPEAKER','DEAFEN_MEMBERS', 'MUTE_MEMBERS', 'MOVE_MEMBERS', 'KICK_MEMBERS']
                            },
                            {
                                id: message.guild.roles.everyone,
                                allow: ['VIEW_CHANNEL']
                            }
                        ])
                        await db.set(`${message.author.id}_room`, S(await db.get(`${message.author.id}_room`)).replaceAll('Visibility1: Private :Visibility2', 'Visibility1: Public :Visibility2').s)
                        var visibility = new discord.MessageEmbed()
                        .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                        .setDescription(`Set room's visibility to ${args[0]}! Permissions has been reset.`)
                        .setColor('#00ff00')
                        message.channel.send(visibility)
                        var visibilitylog = new discord.MessageEmbed()
                        .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                        .setDescription(`${message.author.tag} set their room's visibility to ${args[0]}.`)
                        .setColor('#ffa500')
                        stafflog.send(visibilitylog)
                    }else if (args[0] === 'private'){
                        if (S(await db.get(`${message.author.id}_room`)).between('Visibility1:', ':Visibility2').collapseWhitespace().s === 'Private') {
                            var visibilitynoroom = new discord.MessageEmbed()
                            .setAuthor(message.author.tag, message.author.avatarURL())
                            .setDescription('Room is already private!')
                            .setColor('#ff0000')
                            message.channel.send(visibilitynoroom)
                            return;
                        }
                        GTD.overwritePermissions([
                            {
                                id: Owner,
                                allow: ['VIEW_CHANNEL', 'MANAGE_MESSAGES', 'MENTION_EVERYONE', 'SEND_TTS_MESSAGES']
                            },
                            {
                                id: message.guild.roles.everyone,
                                deny: ['VIEW_CHANNEL']
                            }
                        ])
                        VCD.overwritePermissions([
                            {
                                id: Owner,
                                allow: ['VIEW_CHANNEL', 'PRIORITY_SPEAKER','DEAFEN_MEMBERS', 'MUTE_MEMBERS', 'MOVE_MEMBERS', 'KICK_MEMBERS']
                            },
                            {
                                id: message.guild.roles.everyone,
                                deny: ['VIEW_CHANNEL']
                            }
                        ])
                        await db.set(`${message.author.id}_room`, S(await db.get(`${message.author.id}_room`)).replaceAll('Visibility1: Public :Visibility2', 'Visibility1: Private :Visibility2').s)
                        var visibility = new discord.MessageEmbed()
                        .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                        .setDescription(`Set room's visibility to ${args[0]}! Permissions has been reset.`)
                        .setColor('#00ff00')
                        message.channel.send(visibility)
                        var visibilitylog = new discord.MessageEmbed()
                        .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                        .setDescription(`${message.author.tag} set their room's visibility to ${args[0]}.`)
                        .setColor('#ffa500')
                        stafflog.send(visibilitylog)
                    }else{
                        var visibilityinvalid = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('Invalid Visibility')
                        .setColor('#ff0000')
                        message.channel.send(visibilityinvalid)
                    }
                }
            }
        }
        if (command === 'rename') {
            if (check === true) {
                var renameadminonly = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('Room admins can\'t run this command!')
                .setColor('#ff0000')
                message.channel.send(renameadminonly)
                return;
            }
            var data = await db.get(`${message.author.id}_room`)
            if (data === null) {
                var renamenoroom = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('You don\'t have a room!')
                .setColor('#ff0000')
                message.channel.send(renamenoroom)
                return;
            }else{
                if (!args[0]) {
                    var renamenoname = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('No name provided!')
                    .setColor('#ff0000')
                    message.channel.send(renamenoname)
                }else{
                    var CT = S(data).between("CT1: ", " :CT2").s
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    message.guild.channels.cache.get(CT).setName(`🤖｜${args[0]}-console`)
                    message.guild.channels.cache.get(GT).setName(`💬｜${args[0]}-general`)
                    message.guild.channels.cache.get(VC).setName(`🔊｜${args[0]}-vc`)
                    var rename = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Renamed room to ${args[0]}!`)
                    .setColor('#00ff00')
                    message.channel.send(rename)
                    var renamelog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} renamed their room to ${args[0]}.`)
                    .setColor('#ffa500')
                    stafflog.send(renamelog)
                }
            }
        }
        if (command === 'invite') {
            if (!args[0]) {
                var invitenouser = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('No user provided! (example: Username#0001)')
                .setColor('#ff0000')
                message.channel.send(invitenouser)
            }else{
                try{
                    var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                }catch(err){
                    var inviteinvaliduser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Invalid user!')
                    .setColor('#ff0000')
                    message.channel.send(inviteinvaliduser)
                    return;
                }
                if (check === true) {
                    var data = await db.get(room)
                    if (!data) {
                        var invitenoroomadmin = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('Admin room does not exist!')
                        .setColor('#ff0000')
                        message.channel.send(invitenoroomadmin)
                        return;
                    }
                }else{
                    var data = await db.get(`${message.author.id}_room`)
                    if (!data) {
                        var invitenoroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You don\'t have a room!')
                        .setColor('#ff0000')
                        message.channel.send(invitenoroom)
                        return;
                    }
                }
                if (S(await db.get(`${message.author.id}_room`)).between('Visibility1:', ':Visibility2').collapseWhitespace().s === 'Public') {
                    var invitepublic = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Can\'t run this command in a public room!')
                    .setColor('#ff0000')
                    message.channel.send(invitepublic)
                    return;
                }
                    var Owner = S(data).between("Owner1: ", " :Owner2").s
                    if (user.user.id === Owner) {
                        var inviteownerroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t invite the owner!')
                        .setColor('#ff0000')
                        message.channel.send(inviteownerroom)
                        return;
                    }
                    if (user.user.id === message.author.id) {
                        var inviteselfroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t invite yourself!')
                        .setColor('#ff0000')
                        message.channel.send(inviteselfroom)
                        return;
                    }
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    message.guild.channels.cache.get(GT).updateOverwrite(user.user.id, { VIEW_CHANNEL: true})
                    message.guild.channels.cache.get(VC).updateOverwrite(user.user.id, { VIEW_CHANNEL: true})
                    var member = message.guild.members.cache.get(Owner)
                    var invite = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Added ${user.user.tag} to ${message.author.tag}'s room.`)
                    .setColor('#00ff00')
                    message.channel.send(invite)
                    var invitelog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} added ${user.user.tag} to their room.`)
                    .setColor('#ffa500')
                    stafflog.send(invitelog)
                }
            }
        if (command === 'remove') {
            if (!args[0]) {
                var removenouser = new discord.MessageEmbed()
                .setAuthor(message.author.tag, message.author.avatarURL())
                .setDescription('No user provided! (example: Username#0001)')
                .setColor('#ff0000')
                message.channel.send(removenouser)
            }else{
                try{
                    var user = message.guild.members.cache.find(user => user.user.tag === args[0])
                }catch(err){
                    var removeinvaliduser = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Invalid user!')
                    .setColor('#ff0000')
                    message.channel.send(removeinvaliduser)
                    return;
                }
                if (check === true) {
                    var data = await db.get(room)
                    if (!data) {
                        var removenoroomadmin = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('Admin room does not exist!')
                        .setColor('#ff0000')
                        message.channel.send(removenoroomadmin)
                        return;
                    }
                }else{
                    var data = await db.get(`${message.author.id}_room`)
                    if (!data) {
                        var removenoroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You don\'t have a room!')
                        .setColor('#ff0000')
                        message.channel.send(removenoroom)
                        return;
                    }
                }
                if (S(await db.get(`${message.author.id}_room`)).between('Visibility1:', ':Visibility2').collapseWhitespace().s === 'Public') {
                    var removepublic = new discord.MessageEmbed()
                    .setAuthor(message.author.tag, message.author.avatarURL())
                    .setDescription('Can\'t run this command in a public room!')
                    .setColor('#ff0000')
                    message.channel.send(removepublic)
                    return;
                }
                    var Owner = S(data).between("Owner1: ", " :Owner2").s
                    if (user.user.id === Owner) {
                        var removeownerroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t remove the owner!')
                        .setColor('#ff0000')
                        message.channel.send(removeownerroom)
                        return;
                    }
                    if (user.user.id === message.author.id) {
                        var removeselfroom = new discord.MessageEmbed()
                        .setAuthor(message.author.tag, message.author.avatarURL())
                        .setDescription('You can\'t remove yourself!')
                        .setColor('#ff0000')
                        message.channel.send(removeselfroom)
                        return;
                    }
                    var GT = S(data).between("GT1: ", " :GT2").s
                    var VC = S(data).between("VC1: ", " :VC2").s
                    message.guild.channels.cache.get(GT).permissionOverwrites.get(user.user.id).delete()
                    message.guild.channels.cache.get(VC).permissionOverwrites.get(user.user.id).delete()
                    var member = message.guild.members.cache.get(Owner)
                    var remove = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`Removed ${user.user.tag} from ${message.author.tag}'s room.`)
                    .setColor('#ff0000')
                    message.channel.send(remove)
                    var removelog = new discord.MessageEmbed()
                    .setAuthor(message.member.user.tag, message.member.user.avatarURL())
                    .setDescription(`${message.author.tag} removed ${user.user.tag} from their room.`)
                    .setColor('#ffa500')
                    stafflog.send(removelog)
                }
            }
        if (command === 'cmds') {
            if (S(db.get(`${message.author.id}_room`)).between("Visibility1:", ":Visibility2").collapseWhitespace().s === 'Private') {
                var prcmds = new discord.MessageEmbed()
                .setTitle('Private Room Commands:')
                .addField('!invite (username#0001)', 'Invite a user to your room.')
                .addField('!remove (username#0001)', 'Remove a user from your room.')
                .addField('!visibility (public/private)', 'Change who can see your channel.')
                .addField('!rename (name)', 'Rename your room!')
                .addField('!admin (username#0001)', 'Add a user as your room admin.')
                .addField('!unadmin (username#0001)', 'Remove a user as your room admin.')
                .addField('!delete', 'Delete the current room!')
                .setColor('#0000ff')
                message.channel.send(prcmds)
            }else{
                var pucmds = new discord.MessageEmbed()
                .setTitle('Public Room Commands:')
                .addField('!ban (username#0001)', 'Remove a user from your room.')
                .addField('!pardon (username#0001)', 'Unban a user from your room.')
                .addField('!visibility (public/private)', 'Change who can see your channel.')
                .addField('!rename (name)', 'Rename your room!')
                .addField('!admin (username#0001)', 'Add a user as your room admin.')
                .addField('!unadmin (username#0001)', 'Remove a user as your room admin.')
                .addField('!delete', 'Delete the current room!')
                .setColor('#0000ff')
                message.channel.send(pucmds)
            }
        }
        if (command === 'tips') {
            var embed = new discord.MessageEmbed()
            .setTitle('Room Tips:')
            .addField('Nothing here...', 'You can recommend tips by DMing dispeak with a suggestion!')
            .setColor('#0000ff')
            message.channel.send(embed)
        }
    }
    }catch(err) {
        var commanderror = new discord.MessageEmbed()
        .setAuthor(message.author.tag, message.author.avatarURL())
        .setDescription('Ran into command error...')
        .addField('Error', err)
        .setColor('#ff0000')
        message.channel.send(commanderror)
        console.error(err)
    }
})

//Logging system.
try{
    fs.unlinkSync('./logs/debug.log')
    fs.unlinkSync('./logs/error.log')
    fs.unlinkSync('./logs/warn.log')
}catch(err){
    console.error(err)
}

var debug = fs.createWriteStream('./logs/debug.log', {flags: 'a'})
var error = fs.createWriteStream('./logs/error.log', {flags: 'a'})
var warn = fs.createWriteStream('./logs/warn.log', {flags: 'a'})
var trueDebug = console.log;
var trueDebug2 = console.debug;
var trueError = console.error;
var trueWarn = console.warn;
console.debug = function(msg) {
    trueDebug2(msg)
    debug.write(`\nDebug: ${msg}`, function(err) {
        if(err) {
            console.error(err);
        }
    });
}
console.log = function(msg) {
    trueDebug(msg)
    debug.write(`\nDebug: ${msg}`, function(err) {
        if(err) {
            console.error(err);
        }
    });
}
console.error = function(msg) {
    trueError(msg)
    error.write(`\nError: ${msg}`)
}
console.warn = function(msg) {
    trueWarn(msg)
    warn.write(`\nWarn: ${msg}`, function(err) {
        if(err) {
            console.error(err);
        }
    });
}

client.on("error", (e) => {
    console.error(e)
});
client.on("warn", (e) => {
    console.warn(e)
});
client.on("debug", (e) => {
    console.debug(e)
});
client.on("rateLimit", (e) => {
    console.warn(e)
});
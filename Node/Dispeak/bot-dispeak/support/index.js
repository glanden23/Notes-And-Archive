//
// MAIN DEPENDENCIES
//

const discord = require('discord.js')//@12.5.3
const client = new discord.Client()
const fs = require('fs')
const devMode = false

//
// Sleep Function
//

function sleep(ms) {
    return new Promise((resolve) => {
      setTimeout(resolve, ms);
    });
}

client.on("ready", async () => {
    if (devMode) {
        return;
    }
    autoSetStatus()
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
        name: "DM for help.",
        type: "PLAYING"
    })
}

client.on("message", (message) => {
    if (message.author.id === client.user.id) {
        return;
    }
    if (devMode) {
        if (client.guilds.cache.get("901547634983075942").members.cache.get(message.author.id).roles.cache.has("899080837084086283") === false) {
            return;
        }
    }
    if (message.channel.type === "dm") {
        console.log(message.author.tag+": "+message.content)
        fs.appendFileSync("./logs/"+message.author.tag+".log", message.author.tag+": "+message.content+"\n")
        let channel = client.guilds.cache.get("899079205608894515").channels.cache.find(channel => channel.name === message.author.id)
        if (channel === undefined) {
            client.guilds.cache.get("899079205608894515").channels.create(message.author.id, {type: "text"}).then(channel => {
                channel.setParent("899293880246206525")
                channel.send(message.author.tag+": "+message.content)
            })
            return;
        }
        channel.send(message.author.tag+": "+message.content)
    }else{
        if (message.guild.id === "899074075543105557") {
            return;
        }
        console.log(message.author.tag+": "+message.content)
        fs.appendFileSync("./logs/"+message.author.tag+".log", message.author.tag+": "+message.content+"\n")
        if (!message.content.startsWith("!")) {
            var user = client.users.cache.find(user => user.id === message.channel.name)
            if (user != null) {
                client.users.cache.get(user.id).send(message.content)
            }
        }else{
            const args = message.content.slice(1).trim().split(/ +/g);
            const command = args.shift().toLowerCase();
            if (command === "close") {
                var user = client.users.cache.find(user => user.id === message.channel.name)
                if (user != null) {
                    client.users.cache.get(user.id).send("**__Your ticket has been closed! Thank you for choosing Dispeak.__**")
                }
                if (message.channel.parentID === "899293880246206525") {
                    message.channel.delete()
                }
            }
        }
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
    console.debug(e)
});
client.on("rateLimit", (e) => {
    console.warn(e)
});
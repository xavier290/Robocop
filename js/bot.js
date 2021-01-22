const Discord = require("discord.js");
const client = new Discord.Client();
const welcome = require("./welcome");

client.on("ready", () => {
	console.log(`Logged in as ${client.user.tag}!`);

	welcome(client);
});

client.on("message", (msg) => {
	if (msg.content === "$help") {
		msg.reply(
			"You can visit the stackoverflow website to get help with your code"
		);
	}
});

client.login("ODAxNTQyNjEwMjAzNzA1NDE1.YAiMug.CslwIm92uRTGx8mvaYPOA1Z6tus");

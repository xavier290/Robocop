module.exports = (client) => {
	const channelID = "";

	client.on("guildMemberAdd", (member) => {
		console.log(member);

		const message = "Welcome <${member.id}> to the server!";

		const channel = member.guild.channels.cache.get(channelID);
		channel.send(message);
	});
};

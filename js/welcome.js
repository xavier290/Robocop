module.exports = (client) => {
	const channelID = "801915428775002124";

	client.on("guildMemberAdd", (member) => {
		console.log(member);

		const message = `Welcome to the server!, <${member}>`;

		const channel = member.guild.channels.cache.get(channelID);
		channel.send(message);
	});
};

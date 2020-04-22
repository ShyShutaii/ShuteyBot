# used for the help command
USAGE = "say <text>"
DESCRIPTION = "the bot says whatever you enter as arguments"

# the main function that's ran when this script is called
async def run(message, client, args):
    if len(args) > 0:
        await client.send_message(message.channel, " ".join(args))
    else:
        await client.send_message(message.channel, "```Please tell me what to say!```")

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION

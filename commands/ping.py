# used for the help command
USAGE = "ping"
DESCRIPTION = "because it'd be stupid not to have it"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, "```PONG!```")

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION

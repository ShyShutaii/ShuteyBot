# used for the help command
USAGE = "^^DrPepper"
DESCRIPTION = "Show's Image Of DrPeppr"

# the lol message
DrPepper = "**MMmmm DrPepper**"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, DrPepper)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

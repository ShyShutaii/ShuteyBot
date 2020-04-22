# used for the help command
USAGE = "^^clear"
DESCRIPTION = "Clears Chat"

# the lol message
clear = "**Chat Has Been Cleared**"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, clear)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

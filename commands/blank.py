# used for the help command
USAGE = "blank"
DESCRIPTION = "blank"

# the lol message
blank = "blank"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, blank)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

# used for the help command
USAGE = "rage"
DESCRIPTION = "AYAYA RAGE"

# the lol message
rage = "**AYAYA**"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, rage)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

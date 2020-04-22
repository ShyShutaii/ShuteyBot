# used for the help command
USAGE = "gbans"
DESCRIPTION = "Shows All The Plebs That Got Banned"

# the lol message
gbans = "**THEESE MUDA FUKA'S HAVE BEEN BANNED**"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, gbans)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

# used for the help command
USAGE = "banzai"
DESCRIPTION = "He Is A Tree"

# the lol message
banzai = "Banzai is a bonsai tree"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, banzai)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

# used for the help command
USAGE = "madikfelloff"
DESCRIPTION = "it just did"

# the lol message
madikfelloff = "Yes, Yes it did!"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, madikfelloff)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

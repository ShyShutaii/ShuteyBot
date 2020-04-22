# used for the help command
USAGE = "emi"
DESCRIPTION = "Emi's Own Custom Command"

# the lol message
emi = "WUUFF WOF WUF (wolfie language)"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, emi)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

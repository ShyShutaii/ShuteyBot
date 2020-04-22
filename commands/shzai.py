# used for the help command
USAGE = "shzai"
DESCRIPTION = "shute+banzai"

# the lol message
shzai = "Shzai is Shute + Banzai #BroLove ^-^"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, shzai)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

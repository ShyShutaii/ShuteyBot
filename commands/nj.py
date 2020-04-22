# used for the help command
USAGE = "N+J"
DESCRIPTION = "Nathan And Jess's Love"

# the lol message
nj = "Nathan + Jess Is The Best Couple Ive Seen :blue_heart: :blue_heart:  There love will last forever ^-^"

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, nj)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION


#rename all files named * and py

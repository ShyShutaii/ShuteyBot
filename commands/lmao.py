# used for the help command
USAGE = "lmao"
DESCRIPTION = "lol"

# the lol message
LOL = ":regional_indicator_l: :regional_indicator_m: :regional_indicator_a: :regional_indicator_o: "

# the main function that's ran when this script is called
async def run(message, client, args):
    await client.send_message(message.channel, LOL)
    await client.delete_message(message)

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION

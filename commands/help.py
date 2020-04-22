# importing from os for listing files from directory
# importing importlib for calling functions from each script file
from os import listdir
from os.path import isfile, join
import importlib
import configparser
# creating our config file stuffs
config = configparser.ConfigParser()
config.read('config.ini')
# setting our globals from config file
PREFIX = config["Settings"]["prefix"]
# used for the help command
USAGE = "funlist <command>"
DESCRIPTION = "getting the fun list"

# the main function that's ran when this script is called
async def run(message, client, args):
    # get all files in command directory
    commands = [f for f in listdir('commands') if isfile(join('commands', f))]
    # begin making the help message
    help_message = "```\n"
    for command in commands:
        if command != "__init__.py" and len(args) == 0:
            help_info = await importlib.import_module("commands." + command.replace(".py", "")).get_help()
            help_message += command.replace(".py", " -> " + help_info[1] + "\n")
        elif len(args) > 0:
            if args[0] == command.replace(".py", ""):
                help_info = await importlib.import_module("commands." + command.replace(".py", "")).get_help()
                help_message += command.replace(".py", " -> " + help_info[1] + " -> " + PREFIX + help_info[0] + "\n")
    # finish making the message
    help_message += "```"
    # if the help message isn't just what it would be if it never added any help text ( i can't word )
    if help_message != "```\n```":
        await client.send_message(message.channel, help_message)
    else:
        await client.send_message(message.channel, "```That isn't a command!```")

# function called by help to retrieve info about the command
async def get_help():
    return USAGE, DESCRIPTION

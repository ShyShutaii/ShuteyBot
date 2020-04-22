import time
import discord
import configparser
import importlib
from config import token, link, prefix, ownerid
from discord.ext.commands import Bot
import asyncio
import random
from discord.voice_client import VoiceClient
from discord.ext import commands

startup_extensions = ["Music"]
client = Bot(prefix)


config = configparser.ConfigParser()
config.read('config.ini')
# setting our globals from config file
PREFIX = config["Settings"]["prefix"]
OWNER = config["Settings"]["owner"]  # unused but will be needed

@client.event
async def on_ready():
    print("----------------------")
    print("Logged In As")
    print("Username: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("----------------------")

class Main_Commands():
       def _init_(self, bot):
           self.bot = bot


@client.command(pass_context=True)
async def hug(ctx):
    """Huggiez somone"""
    links = ["https://m.popkey.co/edbc5e/jZVdb.gif", "https://i.imgur.com/4oLIrwj.gif", "https://m.popkey.co/fca5d5/bXDgV.gif", "http://i0.kym-cdn.com/photos/images/original/000/906/455/51f.gif", "https://78.media.tumblr.com/9a97b1ca2cf20c70907cf3e8f328bd91/tumblr_ognz58o2ic1vbgf8lo1_500.gif", "https://i.imgur.com/rlOJqHL.gif"]
    await client.send_message(ctx.message.channel, random.choice(links))

@client.command(pass_context=True)
async def rage(ctx):
    """AYAYA RAGE"""
    links = ["chttp://i.imgur.com/KXYrJzY.gif", "https://thumbs.gfycat.com/DetailedInfamousCranefly-size_restricted.gif", "http://i0.kym-cdn.com/photos/images/original/001/035/769/fba.jpg"]
    await client.send_message(ctx.message.channel, random.choice(links))


@client.command(pass_context=True)
async def pat(ctx):
    """Pat's somone"""
    links = ["https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif?itemid=9920853", "https://media.giphy.com/media/iGZJRDVEM6iOc/giphy.gif", "https://thumbs.gfycat.com/FlimsyDeafeningGrassspider-size_restricted.gif", "https://media1.tenor.com/images/398c9c832335a13be124914c23e88fdf/tenor.gif?itemid=9939761", "https://media.giphy.com/media/ye7OTQgwmVuVy/giphy.gif"]
    await client.send_message(ctx.message.channel, random.choice(links))


@client.command(pass_context=True)
async def DrPepper(ctx):
    """Dr Pepper Nothin Else"""
    links = ["http://www.drinksecrets.com/images/ingredients/megahuge/xxl_drpepper.png"]
    await client.send_message(ctx.message.channel, random.choice(links))
    
@client.command(pass_context=True)
async def command(ctx):
    """Shows The Custom Command Image"""
    links = ["https://i.imgur.com/c5yQxiV.png"]
    await client.send_message(ctx.message.channel, random.choice(links))

@client.command()
async def ping():
    '''See if The Bot is Working'''
    pingtime = time.time()
    pingms = await client.say("Pinging...")
    ping = time.time() - pingtime
    await client.edit_message(pingms, ":ping_pong:  time is `%.01f seconds`" % ping)
    
@client.command()
async def botinvite():
    '''A Link To Invite This Bot To Your Server!'''
    await client.say("Check Your Dm's I Just Slid in :wink:")
    await client.whisper(link)
        
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    await client.process_commands(message)
    if message.content.startswith(PREFIX) and not message.author.bot:
        # parsing the message to get arguments and the command
        command = message.content.split(" ")[0][len(PREFIX):]
        arguments = message.content.split(" ")[1:]
        try:
            await importlib.import_module("commands." + command).run(message, client, arguments)
        except ImportError:
            await client.send_message(message.channel, "```That isn't a command!```")
        except discord.Forbidden:
            print("[Error] Forbidden error!")

    if message.content.startswith('^CuteCommands'):
      embed = discord.Embed(title="All the cute commands", description="Just Make Sure To Put A ^ Infront Of The Trigger Word", color=0xB800FF)
      embed.add_field(name="**Huggiez**", value="Hug Command", inline=False)
      embed.add_field(name="**Slap**", value="Slap Command", inline=False)
      embed.add_field(name="**Pat**", value="Pat Command", inline=False)
      embed.add_field(name="**Poke**", value="Poke Command", inline=False)
	  embed.add_field(name="**WanSomeGo**", value="U Heard MEH", inline=False)
      embed.set_thumbnail(url="https://productivitysteps.files.wordpress.com/2016/10/golden_rule.png")
      await client.send_message(message.channel, embed=embed)
            
    if message.content.startswith('^Huggiez'):
      embed = discord.Embed(title="Huggiez", description="Cuteness", color=0xB800FF)
      embed.add_field(name="**Awweee**", value="They Just Gave You A Hug", inline=False)
      embed.set_thumbnail(url="http://moziru.com/images/heartshaped-clipart-gif-small-13.png")
      embed.set_image(url="https://m.popkey.co/edbc5e/jZVdb.gif",)
      await client.send_message(message.channel, embed=embed)
            
    if message.content.startswith('^Slap'):
      embed = discord.Embed(title="SLAP", description="OI YOU", color=0xB800FF)
      embed.add_field(name="You Have Been Slapped", value="Git Gud", inline=False)
      embed.set_thumbnail(url="http://www.emofaces.com/png/200/emoticons/slap.png")
      embed.set_image(url="https://media.giphy.com/media/jLeyZWgtwgr2U/giphy.gif",)
      await client.send_message(message.channel, embed=embed)
	  
	if message.content.startswith('^WanSomeGo'):
      embed = discord.Embed(title="YouWantSomeGo", description="You Heard Me!", color=0xB800FF)
      embed.add_field(name="**Slaps Da Shit Out Of You!**", value="Git Gud", inline=False)
      embed.set_thumbnail(url="http://moziru.com/images/splatter-clipart-transparent-background-14.png")
      embed.set_image(url="https://pa1.narvii.com/6397/a87128b051685c1f006819269a04db7270fe4d92_hq.gif",)
      await client.send_message(message.channel, embed=embed)
                  
    if message.content.startswith('^Pat'):
      embed = discord.Embed(title="Nya~", description="Ya Got Patted", color=0xB800FF)
      embed.set_image(url="https://media.giphy.com/media/YAhTcaxxGrKCI/giphy.gif",)
      await client.send_message(message.channel, embed=embed)

    if message.content.startswith('^Poke'):
      embed = discord.Embed(title="Nya~", description="Ya Got Poked", color=0xB800FF)
      embed.set_image(url="https://media.giphy.com/media/hRQ6OBek0erPG/giphy.gif",)
      await client.send_message(message.channel, embed=embed)
      
    if message.content.startswith('^^hugs myself'):
        await client.send_message(message.channel, "Awweeeee {0.author.mention} I Hugz You *hugs*".format(message))

    # Greetings
    if message.content.startswith('Hello Shute'):
        msg = 'Heya ^-^ {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('im hungry'):
        msg = 'OI {0.author.mention} Have Some **FOASH N CHOAPS**'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^^shzai'):
        msg = 'Shzai is Shute + Banzai {0.author.mention} #BroLove ^-^'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('^^nathan+jess'):
        msg = ' Nathan + Jess Is The Best Couple Ive Seen {0.author.mention} There love will last forever ^-^ '.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('madikfelloff'):
        msg = 'Yes, Yes it did! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('banzai'):
        msg = '{0.author.mention} Banzai is a bonsai tree'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('@ShuteyBot'):
        msg = '{0.author.mention} You mentioned me?'.format(message)
        await client.send_message(message.channel, msg)  


    # say (id) is the best
    # This is where I am lost. how to mention someone's name or id ?
    if message.content.startswith('^^best'):
        mid = User.id('ZERO#6885').format(message)
        await client.send_message(message.channel, '{mid} mentioned')
        
#gets a server invite and pms it to the user who requested it  

@client.command(pass_context=True)
async def serverinvite(context):
	"""Pm's A Invite Code (To The Server) To The User"""
	invite = await client.create_invite(context.message.server,max_uses=1,xkcd=True)
	await client.send_message(context.message.author,"Your invite URL is {}".format(invite.url))
	await client.say ("Check Your Dm's :wink:")

#Gets a List of Bans From The Server

@client.command(pass_context = True)
async def gbans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

#Lists Info About The server

@client.command(pass_context = True)
async def serverinfo(ctx):
    '''Displays Info About The Server!'''

    server = ctx.message.server
    roles = [x.name for x in server.role_hierarchy]
    role_length = len(roles)

    if role_length > 50: #Just in case there are too many roles...
        roles = roles[:50]
        roles.append('>>>> Displaying[50/%s] Roles'%len(roles))

    roles = ', '.join(roles);
    channelz = len(server.channels);
    time = str(server.created_at); time = time.split(' '); time= time[0];

    join = discord.Embed(description= '%s '%(str(server)),title = 'Server Name', colour = 0xFFFF);
    join.set_thumbnail(url = server.icon_url);
    join.add_field(name = '__Owner__', value = str(server.owner) + '\n' + server.owner.id);
    join.add_field(name = '__ID__', value = str(server.id))
    join.add_field(name = '__Member Count__', value = str(server.member_count));
    join.add_field(name = '__Text/Voice Channels__', value = str(channelz));
    join.add_field(name = '__Roles (%s)__'%str(role_length), value = roles);
    join.set_footer(text ='Created: %s'%time);

    return await client.say(embed = join);

#a command that sets the bots game

@client.command(pass_context=True)
async def setgame(ctx, *, game):
    """Sets my game (Owner)"""
    if ctx.message.author.id == (ownerid):
        message = ctx.message
        await client.delete_message(message)
        await client.whisper("Game was set to **{}**!".format(game))
        await client.change_presence(game=discord.Game(name=game))

#Clears The Chat

@client.command(pass_context=True)       
async def clear(ctx, number):
    '''Clears The Chat 2-100'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass
    mgs = []
    number = int(number)
    async for x in client.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await client.delete_messages(mgs)

@client.command()
async def warn(user="", reason="", mod="", n="", channel=""):
    """Warns a Member"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    if user == "":
        await client.say(":x: No user Mentioned")
    if reason == "":
        await client.say(":x: No reason entered!")
    if mod == "":
        await client.say(":x: No Mod is Selected!")
    if n == "":
        await client.say(":x: No Warn Number was selected")
    if channel == "":
        await client.say(":x: No Channel entered!")
    channel = client.get_channel(channel)
    em = discord.Embed(color=0x42fc07)
    em.add_field(name='Warning', value=("You Have Been Warned -->"))
    em.add_field(name='User', value=(user))
    em.add_field(name='Reason', value=(reason))
    em.add_field(name='Moderator', value=(mod))
    em.set_footer(text="Warnings had : {}".format(n))
    await client.send_message(channel, embed=em)

@client.command(pass_context=True, hidden = True)
async def report(ctx, user: discord.Member, *, reason):
    """Reports user and sends report to Bot Admin"""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    author = ctx.message.author
    server = ctx.message.server


    joined_at = user.joined_at
    user_joined = joined_at.strftime("%d %b %Y %H:%M")
    joined_on = "{}".format(user_joined)

    args = ''.join(reason)
    adminlist = []
    check = lambda r: r.name in 'YOUR_ROLE_HERE'

    members = server.members
    for i in members:

        role = bool(discord.utils.find(check, i.roles))

        if role is True:
            adminlist.append(i)
        else:
            pass

    colour = discord.Colour.magenta()

    description = "User Reported"
    data = discord.Embed(description=description, colour=colour)
    data.add_field(name="Report reason", value=reason)
    data.add_field(name="Report by", value=author)
    data.add_field(name="Reported user joinned this server on", value=joined_on)
    data.set_footer(text="User ID:{}"
                            "".format(user.id))

    name = str(user)
    name = " ~ ".join((name, user.nick)) if user.nick else name

    if user.avatar_url:
        data.set_author(name=name, url=user.avatar_url)
        data.set_thumbnail(url=user.avatar_url)
    else:
        data.set_author(name=name)

    for i in adminlist:
        await client.send_message(i, embed=data)

@client.command(pass_context = True)
async def ban(ctx, member : discord.Member = None, days = " ", reason = " "):
    """Bans specified member from the server."""
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    try:
        if member == None:
            await client.say(ctx.message.author.mention + ", please specify a member to ban.")
            return

        if member.id == ctx.message.author.id:
            await client.say(ctx.message.author.mention + ", you cannot ban yourself.")
            return
        else:
            await client.ban(member, days)
            if reason == ".":
                await client.say(member.mention + " has been banned from the server.")
            else:
                await client.say(member.mention + " has been banned from the server. Reason: " + reason + ".")
            return
    except Forbidden:
        await client.say("You do not have the necessary permissions to ban someone.")
        return
    except HTTPException:
        await client.say("Something went wrong, please try again.")

#Kick a Member From The Server

@client.command(pass_context = True)
async def kick(ctx, *, member : discord.Member = None):
    '''Kicks A User From The Server'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to kick!")
    try:
        await client.kick(member)
    except Exception as e:
        if 'Privilege is too low' in str(e):
            return await client.say(":x: Privilege too low!")
 
    embed = discord.Embed(description = "**%s** has been kicked."%member.name, color = 0xF00000)
    embed.set_footer(text="BasicDiscord Bot v1.0")
    await client.say(embed = embed)

#Mutes a Member From The server

@client.command(pass_context = True)
async def mute(ctx, *, member : discord.Member):
    '''Mutes A Memeber'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = False
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)

    await client.say("**%s** is now Muted! Wait For an Unmute.."%member.mention)

#Unmutes a member

@client.command(pass_context = True)
async def unmute(ctx, *, member : discord.Member):
    '''Unmutes The Muted Memeber'''
    user_roles = [r.name.lower() for r in ctx.message.author.roles]

    if "admin" not in user_roles:
        return await client.say("You do not have the role: Admin")
    pass

    overwrite = discord.PermissionOverwrite()
    overwrite.send_messages = True
    await client.edit_channel_permissions(ctx.message.channel, member, overwrite)

    await client.say("**%s** Times up...You are Unmuted!"%member.mention)

                                  
client.run(token)

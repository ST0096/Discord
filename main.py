# Please do not copy this code because I wasted a lot of time working on this code and it takes a lot of time to make this.

# This application is built in Python3 and it can be run local on Code Editors or Local Terminals like Termux

# If you are willing to run using termux please visit my github page and clone the repo.

# My Github: https://www.github.com/ST0096

# All my projects are avaliable there


import discord
#freezes time using time.sleep(time)
# some of these modules may give you a hard time on terminals
import time
import random
import asyncio
from discord.ext import commands
from opposite import word_pairs
import datetime


intents = discord.Intents.all()
intents.bans = True
client = commands.Bot(command_prefix="?", intents=intents)
# Discord bot token
DISCORD_TOKEN = 'MTIxNTQzMDQ2MDU3NDkyODk5Nw.GK4-t6.cu3VleAxlwv-CmvYU76b9Mo2Un6ZgOWeV0PkS0'

# This will run if bot has started succesfully
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Soccer"))
  print("---------------------------")
  print("Bot Started Successfully!!!")
  print("---------------------------")
  print(f"Currently logged in as {client.user}")
  print("---------------------------")
  print(f"Bot ID: {client.user.id}")
  print("---------------------------")
  print("running on Local Client")
  print("---------------------------")

# List of science questions
# note: work on this and put it in a file and let the science command acess it when called
#these questions r provided by ChatGPT so idk them answers 
science_questions = [
    ("What is the SI unit of force?", "newton"),
    ("What is the formula for kinetic energy?", "0.5 * mass * velocity^2"),
    ("What is the first law of thermodynamics also known as?",
     "law of conservation of energy"),
    ("What is the SI unit of temperature?", "kelvin"),
    ("What is the formula for pressure?", "force / area"),
    ("What is the second law of thermodynamics?", "entropy always increases"),
    ("What is the SI unit of power?", "watt"),
    ("What is the formula for gravitational potential energy?",
     "mass * gravity * height"),
    ("What is Boyle's law?",
     "pressure and volume are inversely proportional at constant temperature"),
    ("What is the SI unit of work?", "joule")
]



# Hello CMD
@client.command()
async def hello(ctx):
  await ctx.send("Hey! How can I assist you today?")

# Bot Activity CMD
@client.command()
async def activity(ctx, activity_type: str, *, activity_name: str):
    # Convert activity_type to lowercase
    activity_type = activity_type.lower()

    # Check if activity type is valid
    valid_activity_types = ['playing', 'watching', 'listening', 'streaming']
    if activity_type not in valid_activity_types:
        await ctx.send("Invalid activity type. Please use one of the following: playing, watching, listening, streaming.")
        return

    # Set the member's activity
    if activity_type == 'playing':
        activity = discord.ActivityType.playing
    elif activity_type == 'watching':
        activity = discord.ActivityType.watching
    elif activity_type == 'listening':
        activity = discord.ActivityType.listening
    elif activity_type == 'streaming':
        activity = discord.ActivityType.streaming
    else:
        await ctx.send("Invalid activity type.")
        return

    await client.change_presence(activity=discord.Activity(type=activity, name=activity_name))

    await ctx.send(f"Changed activity to {activity_type} {activity_name}")

  

# Server Nuke
@client.command()
async def nuke(ctx):
  await ctx.send(" Hey, are you sure you want to do this? ")
  await ctx.send(
      "If you really want to do this try using ?nuke-all command! Good Luck")

# Hi CMD
@client.command()
async def hi(ctx):
  await ctx.send("Hey there! What's up?")

# Whatsup CMD
@client.command()
async def whatsup(ctx):
  await ctx.send("Not much, just here to help! What can I do for you?")

# Weather CMD 
# This function does not work because I am not rich and unable to pay for the api!
# if you do have the api you can code it in here!
@client.command()
async def weather(ctx):
  await ctx.send("Sorry, I am not rich! Therefore I am not able to purchase the api to give weather information!")

# who is cmd
# info on specific user
@client.command()
async def whois(ctx, member: discord.Member):
  await ctx.send(f"Username: {member.name}")
  await ctx.send(f"User ID: {member.id}")
  await ctx.send(f"Joined Server: {member.joined_at}")
  await ctx.send(f"Account Created: {member.created_at}")
  

# Random thing
@client.command()
async def random_fruit(ctx):
  word = [
      "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
      "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "peach",
      "quince", "raspberry", "strawberry", "tangerine", "watermelon",
      "blueberry", "blackberry", "cranberry", "gooseberry", "rambutan",
      "pomegranate", "apricot", "coconut", "date", "guava", "jackfruit",
      "lychee", "mangosteen", "nectarine", "papaya", "passionfruit",
      "pineapple", "starfruit", "tamarind", "ugli fruit", "pomegranate",
      "persimmon", "raspberry"
  ]
  random_fruit_word = random.choice(word)
  await ctx.send(f"Your random fruit is: {random_fruit_word}")

# Another random thing
@client.command()
async def random_word(ctx):
  word = [
      "elephant",
      "computer",
      "rainbow",
      "mountain",
      "ocean",
      "sunshine",
      "butterfly",
      "unicorn",
      "dragon",
      "guitar",
      "candle",
      "television",
      "telephone",
      "dictionary",
      "umbrella",
      "suitcase",
      "submarine",
      "microphone",
      "helicopter",
      "skyscraper",
      "architecture",
      "revolution",
      "parachute",
      "adventure",
      "exploration",
      "magnificent",
      "landscape",
      "breathtaking",
      "entertainment",
      "sensational",
      "phenomenal",
      "spectacular",
      "extraordinary",
      "fascinating",
      "remarkable",
      "wonderful",
      "fantastic",
      "brilliant",
      "marvelous",
      "incredible",
      "unbelievable",
      "astounding",
      "stupendous",
      "astonishing",
      "prodigious",
      "breathtaking",
      "majestic",
      "impressive",
      "grandiose",
      "extraordinary",
      "outstanding",
      "magnificent",
      "phenomenal",
      "stunning",
      "wonderful",
      "marvelous",
      "fantastic",
      "exceptional",
      "awe-inspiring",
      "mind-blowing",
      "unforgettable",
      "incomparable",
      "splendid",
      "fabulous",
      "awe-inspiring",
      "dazzling",
      "astounding",
  ]
  random_word = random.choice(word)
  await ctx.send(f"Your random word is: {random_word}")

# Another random thing :)
@client.command()
async def random_country(ctx):
  country = [
      "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
      "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
      "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus",
      "Belgium", "Belize", "Benin", "Bhutan", "Bolivia",
      "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
      "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada",
      "Cape Verde", "Central African Republic", "Chad", "Chile", "China",
      "Colombia", "Comoros", "Congo", "Costa Rica", "Croatia", "Nepal"
  ]
  random_country = random.choice(country)
  await ctx.send(f"Here's a random country: {random_country}")

# math cmd
# prints questions for you! STUDY!
@client.command()
async def math(ctx):
  num1 = random.randint(1, 10)
  num2 = random.randint(1, 10)
  operator = random.choice(['+', '-', '*'])
  correct_answer = eval(f'{num1}{operator}{num2}')
  question = f'What is {num1} {operator} {num2}?'
  await ctx.send(question)

  tries = 2
  while tries > 0:
    try:
      response = await client.wait_for(
          'message',
          check=lambda message: message.author == ctx.author and message.
          channel == ctx.channel,
          timeout=10)
      user_answer = int(response.content)
      if user_answer == correct_answer:
        await ctx.send('Correct!')
        break
      else:
        await ctx.send('Incorrect. Try again.')
        tries -= 1
    except asyncio.TimeoutError:
      await ctx.send('Time is up!')
      break

  if tries == 0:
    await ctx.send(
        f'The correct answer is {correct_answer}. You need to learn math!')

# science cmd
# gives science related questions so you can be better at science :) So nice of me!
@client.command()
async def science(ctx):
    question, answer = random.choice(science_questions)
    await ctx.send(question)

    tries = 3
    while tries > 0:
        try:
            response = await client.wait_for('message', check=lambda message: message.author == ctx.author and message.channel == ctx.channel, timeout=15)
            user_answer = response.content.lower()
            if user_answer == answer:
                await ctx.send('Correct!')
                break
            else:
                await ctx.send('Incorrect. Try again.')
                tries -= 1
        except asyncio.TimeoutError:
            await ctx.send('Time is up!')
            break

    if tries == 0:
        await ctx.send(f'The correct answer is "{answer}". You need to learn science!')

# Function to check if the given word is the opposite of the expected word
def is_opposite(word, expected_opposite):
    return word.lower() == expected_opposite.lower()

# Define a command named 'opposite'
@client.command()
async def opposite(ctx):
    # Shuffle the word pairs to make the game more interesting
    random.shuffle(word_pairs)

    # Function to check if the message is from the same user and in the same channel
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    incorrect_attempts = 0

    while incorrect_attempts < 2:
        # Choose a random word pair
        word, opposite = word_pairs.pop(0)  # Get the first pair and remove it from the list

        # Send the word to the channel
        await ctx.send(f"Word: {word}")

        try:
            # Wait for the user's response
            msg = await client.wait_for('message', timeout=30, check=check)
            response = msg.content

            # Check if the response is the opposite of the word
            if is_opposite(response, opposite):
                await ctx.send("Correct!")
                incorrect_attempts = 0  # Reset incorrect_attempts when the answer is correct
            else:
                await ctx.send(f"Wrong! The opposite of {word} is {opposite}.")
                incorrect_attempts += 1
        except TimeoutError:
            await ctx.send("Time's up! You didn't respond in time.")

    await ctx.send("You got the opposite word wrong twice in a row. Game over.")


# idk random stuff again
@client.command()
async def weird(ctx):
  await ctx.send("Hey, are you sure you want to see some stuff? ")
  time.sleep(0.2)
  await ctx.send("Here we go!")
  time.sleep(0.2)
  await ctx.send("SIKE! You thought! I am a bot not a human! AHAHAHAHAHA")

# python cmd
# give a breif info about python programming 
# this is how I was made :)
@client.command()
async def python(ctx):
  await ctx.send("Looks like you want a berif knowledge about Python!")
  time.sleep(0.2)
  await ctx.send("Python is a popular programming language known for its simplicity and readability.")
  time.sleep(0.2)
  await ctx.send("It was first released in 1991 by Guido van Rossum and was developed by the Python Software Foundation.")
  time.sleep(0.2)
  await ctx.send("Python is a high-level programming language that is easy to learn and use.")
  time.sleep(0.2)
  await ctx.send("It is a dynamic language that supports multiple programming paradigms, including object-oriented, imperative, and functional programming.")
  time.sleep(0.2)
  await ctx.send("Python has a large and active community of developers and users, with many libraries and frameworks available for various purposes.")
  time.sleep(0.5)
  await ctx.send("Well well well... Thats all I got to say about Python! Have a good day!")


# help cmd
# outputs helpful commands using discord py embeds
@client.command()
async def support(ctx):
    embed = discord.Embed(title="SUPPORT", color=discord.Color.red())
    embed.add_field(name="Commands", value=(
        "?hello - Say hello to the bot\n"
        "?hi - Say hi to the bot\n"
        "?whatsup - Ask the bot what's up\n"
        "?weather - Ask the bot about the weather\n"
        "?whois - Get information about a user\n"
        "?random_fruit - Get a random fruit\n"
        "?random_word - Get a random word\n"
        "?random_country - Get a random country\n"
        "?math - Play a math game\n"
        "?science - Play a science game\n"
        "?weird - Do you really want to do this?\n"
        "?python - Learn about Python\n"
        "?support - Show this help message\n"
        "?nuke - Nuke the server\n"
        "?nuke-all - Nuke all the members\n"
        "?ban - Ban a member\n"
        "?kick - Kick a member\n"
        "?unban - Unban a member\n"
        "?mute - Mute a member\n"
        "?unmute - Unmute a member\n"
        "?clear - Clear a certain amount of messages\n"
        "?lock - Lock a channel\n"
        "?unlock - Unlock a channel\n"
        "?hide - Hide a channel\n"
        "?unhide - Unhide a channel\n"
        "Thats all I got!!!"
    ))
    await ctx.send(embed=embed)

# time cmd
# IDK how to fix this it doesnt give America/New York time ! Idk i am a bit stupid :)
@client.command()
async def time(ctx):
   await ctx.send("Sorry, This module is currently unavaliable!")
    # Get the current time in New York timezone
    #ny_time = datetime.datetime.now(tz=tz.gettz('America/New_York'))

    # Create an embed to display the time
    #embed = discord.Embed(
        #title="Current time and date in New York",
        #description=f"Date: {ny_time.strftime('%m - %d - %Y')}\nTimezone: {ny_time.strftime('%Z')}\nTime: {ny_time.strftime('%H : %M : %S')}",
        #color=discord.Color.blue()
    #)

    # Send the embed to the channel where the command was invoked
    #await ctx.send(embed=embed)

# Last line of defense ! The defense of destruction :)
@client.command()
async def nukeall(ctx, action=None):
  if action == "create":
    # Create channels
    for i in range(10000):
      await ctx.guild.create_text_channel(f"nuked-{i+1}")
    await ctx.send("Channel creation spammed succesfully!")
  elif action == "delete":
    # Delete all channels
    for channel in ctx.guild.channels:
      await channel.delete()
    await ctx.send("All Channels nuked/deleted")
  else:
    await ctx.send(
        "Oops! Invalid Input. Please specify by using 'create' or 'delete'! ")

# ban cmd (usage obvious)
@client.command()
async def ban(ctx, member: discord.Member, *, reason="Reason not provided 💀💀"):
  if ctx.author.guild_permissions.ban_members:
    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned for {reason}. 😀")
  else:
    await ctx.send("You don't have permission to ban members. 😡😡")

# kick cmd (usage obvious)
@client.command()
async def kick(ctx, member: discord.Member, *, reason="No reason provided 💀"):
  if ctx.author.guild_permissions.kick_members:
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked for {reason}. 😀")
  else:
    await ctx.send("You don't have permission to kick members. 😡😡")

# unban cmd (usage obvious)
@client.command()
async def unban(ctx, member_id: int):
  if ctx.author.guild_permissions.ban_members:
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
      if ban_entry.user.id == member_id:
        await ctx.guild.unban(ban_entry.user)
        await ctx.send(
            f"{ban_entry.user.name}#{ban_entry.user.discriminator} has been unbanned successfully."
        )
        return
    await ctx.send("User not listed in ban list.")
  else:
    await ctx.send("You don't have permission to unban members.")

# info cmd
# gives info obviously 
@client.command()
async def info(ctx):
  guild = ctx.guild
  total_members = guild.member_count
  owner = guild.owner
  creation_date = guild.created_at.strftime("%Y-%m-%d %H:%M:%S")
  verification_level = guild.verification_level
  afk_channel = guild.afk_channel
  afk_timeout = guild.afk_timeout

  embed = discord.Embed(title=f"Server Info - {guild.name}",
                        color=discord.Color.red())
  embed.add_field(name="Owner", value=owner, inline=False)
  embed.add_field(name="Total Members", value=total_members, inline=False)
  embed.add_field(name="Creation Date", value=creation_date, inline=False)
  embed.add_field(name="Verification Level",
                  value=verification_level,
                  inline=False)
  embed.add_field(name="AFK Channel",
                  value=afk_channel.name if afk_channel else "None",
                  inline=False)
  embed.add_field(
      name="AFK Timeout",
      value=f"{afk_timeout // 60} minutes" if afk_timeout else "None",
      inline=False)

  await ctx.send(embed=embed)

# credit cmd
# gives credit to the bot owner obviously using embeds 
@client.command()
async def credit(ctx):
  cred = "Username: @st0096_ | Display: Cat  "
  coder = "Unprofessional Python Coder, Python Html, Css, Javascript, Lua, C#, Bash Programmer"
  date = "Bot made in: 3/07/2024 | March 7, 2024 | In Pennsylvania, United States of America"
  lang = "Made with Python Programming Language in PyCharm IDE by JetBrains"
  thank = "Thank You for using Cristiano Ronaldo Bot"
  age = "This bot is 4 Months Old"

  embed = discord.Embed(title="Credit", color=discord.Color.red())
  embed.add_field(name="Programmer", value=cred, inline=False)
  embed.add_field(name="Profession", value=coder, inline=False)
  embed.add_field(name="Made In", value=date, inline=False)
  embed.add_field(name="Bot Age", value=age, inline=False)
  embed.add_field(name="Detail", value=lang, inline=False)
  embed.add_field(name="Thanks", value=thank, inline=False)

  await ctx.send(embed=embed)

# rule cmd
# outputs random rules probably not used by many servers 
@client.command()
async def rule(ctx):
  await ctx.send(
      "Below are REQUIRED server rules all members/staffs are required to follow! These rule may be different depending on your servers current rules!"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rules\n----------------------------------------\nRule 1 │ Be respectful\nAlways treat others with respect. Discriminatory, hate speech, and personal attacks are not allowed.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 2 │ No spamming\nDo not send multiple messages in a row, post irrelevant content, or flood the chat with excessive messages. This can disrupt the conversation and annoy others.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 3 │ No advertising\nDo not promote other Discord servers, websites, or services without permission from the server owner or moderators. This includes DMing members.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 4 │ No NSFW content\nDo not post or share any explicit or pornographic content. This includes images, videos, or text. Keep the server appropriate for all ages.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 5 │ Stay on topic\nStay on topic in the appropriate channels. Avoid going off-topic or discussing unrelated topics in channels meant for specific purposes.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 6 │ No trolling\nDo not intentionally provoke others or disrupt conversations for the sake of amusement.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 7 │ Use appropriate language\nDo not use excessive profanity or vulgar language. Keep the conversation respectful and appropriate.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 8 │ No doxxing\nDo not share personal information of other users without their consent. This includes full names, addresses, phone numbers, and any other identifying information. Doxxing is not only a violation of privacy but also a serious offense.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 9 │ No unauthorized alt accounts\nThe use of unauthorized alt accounts is not allowed on the server. Alt accounts can be used to circumvent bans, spam, harass, or impersonate other users, which can cause disruptions in the community. If a user wishes to use an alternate account, they must receive permission from the server moderators. Unauthorized alt accounts may result in a ban.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 10 │ Take arguments to DMs\nArguments or disagreements should be taken to private messages (DMs) instead of public channels. Public arguments can be disruptive and make others uncomfortable. If you have a disagreement with another user, try to resolve it in private messages before it becomes a public issue. If the argument persists and starts to affect the community, moderators may intervene to help resolve the conflict.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 11 │ Respectful use of voice channels\nWhen using voice channels, please be respectful towards others. This includes not shouting, not playing loud music or sounds, and avoiding background noise as much as possible. Also, refrain from using any discriminatory or offensive language. If you are in a voice channel with others, make sure to take turns speaking and not interrupt or talk over others.\n\n"
  )
  time.sleep(0.2)
  await ctx.send(
      "Rule 12 │ Discord TOS (discord.com/terms)\nAll members of this server must adhere to the Discord Terms of Service (TOS) and Community Guidelines. Any behaviour or content that violates these rules will not be tolerated."
  )
  time.sleep(0.5)
  await ctx.send(
      "If these rules aren't followed you will be muted, kicked, or banned by mods or admins!"
  )
  time.sleep(0.2)
  await ctx.send("Thank You! Please follow these rules! 😀")

# dm cmd 
# sents direct mesages to a user
@client.command()
async def dm(ctx, member: discord.Member, *, message: str):
  try:
    await member.send(message)
    await ctx.send(f"Message sent to {member.display_name} successfully!")
  except discord.Forbidden:
    await ctx.send("I'm unable to send a message to that user.")

# member join cmd 
# informs when a new user joins server
@client.event
async def on_member_join(member):
  guild_name = member.guild.name
  channel_names = [
      "welcome", "general", "introductions", "chat", "starter"
  ]  # List of channels that could be in the server where the bot can welcome incoming members
  welcome_channel = None

  # Iterate through each channel name in the list
  for name in channel_names:
    # Try to find a channel with the current name
    channel = discord.utils.get(member.guild.channels, name=name)
    if channel and isinstance(channel,
                              discord.TextChannel) and channel.permissions_for(
                                  member.guild.me).send_messages:
      welcome_channel = channel
      break

  if welcome_channel:
    await welcome_channel.send(
        f"{member.name} has joined the server '{guild_name}'")
  else:
    # If no suitable channel is found, send the message to the system console
    print(
        f"No suitable text channels are found in '{guild_name}'! Please try again when the current server has a text channel that corresponds with the list of names listed!"
    )

# bot token for the bot to run obviously 
client.run(DISCORD_TOKEN)

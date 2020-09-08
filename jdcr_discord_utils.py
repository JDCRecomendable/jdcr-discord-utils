# JDCR Discord Utilities
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.

from random import random, randrange
from datetime import datetime
import asyncio
import requests
import discord

from units import unit_values, unit_names, MSG_DOC_UNITS
from units import MSG_DOC_UNITS_LENGTH, MSG_DOC_UNITS_AREA
from units import MSG_DOC_UNITS_VOLUME, MSG_DOC_UNITS_TIME
from units import MSG_DOC_UNITS_SPEED, MSG_DOC_UNITS_PRESSURE
from constants import MSG_DOC_CONSTANTS, constant_names, constant_values
from base_conversions import MSG_DOC_BASE_CONV, to_dec, from_dec


# Discord Bot Params
TOKEN = "<insert token here>"
STATUS = "with you"


# Values for use in functions
VAL_HIGHEST_INT = 10000
VAL_JOKE_URL = "<insert joke API URL here>"
VAL_JOKE_HEADERS = {"Accept": "text/plain"}


# Channel ID's
CHNL_ID = 000000000000000000


# Input Strings
INP_VULGARITIES = [
    ""
]


# Output Strings for Messages
MSG_JOKE_HEADER = "**JOKE OF THE DAY**"
MSG_FUNC_ERROR = """Command invalid.
Did you use the function as specified in the documentation?
Try `$help`.
If you did, file a bug report."""
MSG_NO_VULGAR = [
    "No vulgar language pls",
    "Pls, no vulgarities",
    "Pls avoid using vulgarities if possible",
    "Inappropriate language detected."
]
MSG_DOC = """```
JDCR Discord Utilities 0.3
Copyright (c) 2020 Jared Recomendable.

USAGE: $<command> [options]

COMMANDS:
  help              display this document
  convert <params>  convert units
  constant <param>  display constant value and unit
  base <params>     convert integers from one base to another
  random <option>   display a random value from the desired category

CONVERT PARAMETERS:
  $convert  <category>  <orig_value>  <from_unit>  to  <to_unit>
  E.g. `$convert length 25 metre to furlong`
  More details available by calling `$help convert`.

CONSTANT PARAMETER:
  $constant  <constant>
  E.g. `$constant avogadro-constant`
  More details available by calling `$help constant`.

BASE PARAMETERS:
  $base  <orig_value>  <from_base>  to  <to_base>
  E.g. `$base 7E b30 to b2`
  More details available by calling `$help base`.

RANDOM CATEGORIES:
  integer           get an integer from 0 to 9999
  float             get a float with range [0.0, 1.0)
  joke              get a lame joke```
"""




## MAIN APP ACTIVITY


# Create Discord Client
client = discord.Client()


# Initialise
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=STATUS))


# Background Tasks
async def background_tasks():
    global jotd_state
    jotd_state = False
    while not client.is_closed():
        datetimestr = str(datetime.now())
        hh = int(datetimestr[11:13])
        mm = int(datetimestr[14:16])
        ss = int(datetimestr[17:19])
        await client.wait_until_ready()
        await joke_of_the_day(hh)
        await asyncio.sleep(30)

async def joke_of_the_day(hh):
    global jotd_state
    trigger = 13
    if hh == trigger:
        if not jotd_state:
            channel = client.get_channel(CHNL_ID)
            await channel.send(MSG_JOKE_HEADER)
            joke = requests.get(VAL_JOKE_URL, headers=VAL_JOKE_HEADERS)
            await channel.send(joke.text)
            jotd_state = True
    else:
        jotd_state = False


# Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    channel = message.channel
    message_content = message.content.lower()

    ## COMMANDS
    # Command Help
    if message_content.startswith("$help convert length"):
        await channel.send(MSG_DOC_UNITS_LENGTH)

    elif message_content.startswith("$help convert area"):
        await channel.send(MSG_DOC_UNITS_AREA)

    elif message_content.startswith("$help convert volume"):
        await channel.send(MSG_DOC_UNITS_VOLUME)

    elif message_content.startswith("$help convert time"):
        await channel.send(MSG_DOC_UNITS_TIME)

    elif message_content.startswith("$help convert speed"):
        await channel.send(MSG_DOC_UNITS_SPEED)

    elif message_content.startswith("$help convert pressure"):
        await channel.send(MSG_DOC_UNITS_PRESSURE)

    elif message_content.startswith("$help convert"):
        await channel.send(MSG_DOC_UNITS)

    elif message_content.startswith("$help constant"):
        await channel.send(MSG_DOC_CONSTANTS)

    elif message_content.startswith("$help base"):
        await channel.send(MSG_DOC_BASE_CONV)

    elif message_content.startswith("$help"):
        await channel.send(MSG_DOC)

    # Command Convert Units
    if message_content.startswith("$convert"):
        try:
            words = message_content.split(" ")
            unit_type = words[1]
            from_val = float(words[2])
            from_unit = words[3]
            to_unit = words[5]
            from_unit_id = unit_names["{}-{}".format(unit_type, from_unit)]
            to_unit_id = unit_names["{}-{}".format(unit_type, to_unit)]
            result = (from_val * unit_values[from_unit_id] / unit_values[to_unit_id])
            await channel.send(result)
        except:
            await channel.send(MSG_FUNC_ERROR)

    # Command Constant
    if message_content.startswith("$constant"):
        try:
            words = message_content.split(" ")
            constant_name = words[1]
            constant_id = constant_names[constant_name]
            result = constant_values[constant_id]
            await channel.send(result)
        except:
            await channel.send(MSG_FUNC_ERROR)

    # Command Base Conversion
    if message_content.startswith("$base"):
        try:
            words = message_content.split(" ")
            from_val = str(words[1])
            from_base = int(words[2][1:])
            to_base = int(words[4][1:])
            result = from_dec(to_dec(from_val, from_base), to_base)
            await channel.send(result)
        except:
            await channel.send(MSG_FUNC_ERROR)

    # Command Random Int
    if message_content.startswith("$random integer"):
        integer = str(randrange(VAL_HIGHEST_INT))
        await channel.send(integer)

    # Command Random Float
    if message_content.startswith("$random float"):
        floatation = str(random())
        await channel.send(floatation)

    # Command Random Joke
    if message_content.startswith("$random joke"):
        joke = requests.get(VAL_JOKE_URL, headers=VAL_JOKE_HEADERS)
        await channel.send(joke.text)

    ## FEATURES
    # Feature Censor Vulgarities
    if any(word in message_content for word in INP_VULGARITIES):
        integer = randrange(len(MSG_NO_VULGAR))
        await channel.send(MSG_NO_VULGAR[integer])


# Run App
client.loop.create_task(background_tasks())
client.run(TOKEN)

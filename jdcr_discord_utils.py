# JDCR Discord Utilities 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.

## INITIALISATION
# Import Libraries
from discord.ext import commands
from discord import Game
import asyncio
import requests

from data_reader import ConfigReader, DataReader
from random_utils import RandomJoker, RandomNumber
from uoa_grad import UoAGraduationUtility
from sci_utils.base_converter import BaseConverter
from sci_utils.constants import Constants
from sci_utils.unit_converter import UnitConverter
from docs import get_main_help_usage, get_base_converter_help_usage
from docs import get_constants_help_usage, get_unit_converter_help_usage
from docs import get_random_utils_help_usage, list_constants, list_units
from docs import get_grad_utils_help_usage


# Initialise Config and Readers
config_reader = ConfigReader("config.txt")
CONFIG = config_reader.retrieve_config()

sci_utils_readers = [
    DataReader(CONFIG["CONSTANTS_FILE"]),
    DataReader(CONFIG["LENGTH_UNITS_FILE"]),
    DataReader(CONFIG["AREA_UNITS_FILE"]),
    DataReader(CONFIG["VOLUME_UNITS_FILE"]),
    DataReader(CONFIG["TIME_UNITS_FILE"]),
    DataReader(CONFIG["SPEED_UNITS_FILE"]),
    DataReader(CONFIG["PRESSURE_UNITS_FILE"])
]


# Initialise Base Converter
base_converter = BaseConverter()


# Initialise Constants Utils
constants = Constants(
    sci_utils_readers[0].retrieve_data_names(),
    sci_utils_readers[0].retrieve_data_values(),
    sci_utils_readers[0].retrieve_data_aliases()
)


# Initialise UoA Grad Utils
grad_utils = UoAGraduationUtility()


# Initialise Unit Converter
unit_converters = []
for converter_reader in sci_utils_readers[1:]:
    unit_converters.append(
        UnitConverter(
            converter_reader.retrieve_data_names(),
            converter_reader.retrieve_data_values(),
            converter_reader.retrieve_data_aliases()
        )
    )


# Initialise Random Utils
random_joker = RandomJoker(CONFIG["JOKE_API_URL"], CONFIG["JOKE_API_HEADERS"])
random_number = RandomNumber()


## MAIN APP ACTIVITY
# Create Discord Client
bot = commands.Bot(command_prefix="$")
bot.remove_command("help")


# Initialise Discord Connection
@bot.event
async def on_ready():
    await bot.change_presence(activity=Game(name=CONFIG["STATUS"]))


# Command Handlers
@bot.command()
async def help(ctx, category="", sub_category=""):
    category = category.lower()
    sub_category = sub_category.lower()

    if category == "base":
        await ctx.send(get_base_converter_help_usage())
    elif category == "constant":
        if sub_category == "list":
            await ctx.send(list_constants(
                constants.get_names(),
                constants.get_aliases()
            ))
        else:
            await ctx.send(get_constants_help_usage())
    elif category == "convert":
        unit_converter_categories = [
            "length",
            "area",
            "volume",
            "time",
            "speed",
            "pressure"
        ]

        if unit_converter_categories.count(sub_category):
            unit_category_index = unit_converter_categories.index(sub_category)
            unit_converter = unit_converters[unit_category_index]

            await ctx.send(list_units(
                unit_converter_categories[unit_category_index],
                unit_converter.get_names(),
                unit_converter.get_aliases()
            ))
        else:
            await ctx.send(get_unit_converter_help_usage())
    elif category == "grad":
        await ctx.send(get_grad_utils_help_usage())
    elif category == "random":
        await ctx.send(get_random_utils_help_usage())
    else:
        await ctx.send(get_main_help_usage())

@bot.command()
async def base(ctx, orig_value="0", from_base="b0", to_keyword="to", to_base="b0"):
    try:
        from_b = from_base[1:]
        to_b = to_base[1:]
        value = base_converter.convert(orig_value, from_b, to_b)
        await ctx.send(value)
    except:
        await ctx.send(get_base_converter_help_usage())

@bot.command()
async def constant(ctx, name=""):
    try:
        constant_index = constants.auto_get_index(name)
        if not constant_index == -1:
            constant_value = constants.get_value_by_index(constant_index)
            await ctx.send(constant_value)
        else:
            await ctx.send(list_constants(
                constants.get_names(),
                constants.get_aliases()
            ))
    except:
        await ctx.send(get_constants_help_usage())

@bot.command()
async def convert(ctx, category="invalid", orig_value=0, from_unit="m", to_keyword="to", to_unit="m"):
    try:
        category_index = [
            "length",
            "area",
            "volume",
            "time",
            "speed",
            "pressure"
        ].index(category.lower())

        unit_converter = unit_converters[category_index]
        value = unit_converter.convert(orig_value, from_unit, to_unit)

        await ctx.send(value)
    except:
        await ctx.send(get_unit_converter_help_usage())

@bot.command()
async def grad(ctx, input_type, *, value=""):
    input_type = input_type.lower()
    if input_type == "honours" or input_type == "honors":
        await ctx.send(grad_utils.get_honours_level_answer_string(value))
    elif input_type == "gpa":
        await ctx.send(grad_utils.get_gpa_answer_string(value))
    else:
        await ctx.send(
            get_grad_utils_help_usage()
        )

@bot.command()
async def random(ctx, category=""):
    category = category.lower()
    if category == "joke":
        joke = random_joker.get_joke()
        await ctx.send(joke)
    elif category == "integer":
        integer = random_number.get_integer()
        await ctx.send(integer)
    elif category == "float":
        float_num = random_number.get_float()
        await ctx.send(float_num)
    else:
        await ctx.send(
            get_random_utils_help_usage()
        )


# Run App
# bot.loop.create_task(background_tasks())
bot.run(CONFIG["TOKEN"])

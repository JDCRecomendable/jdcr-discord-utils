# JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.


from datetime import datetime
import asyncio
import requests
import discord


from data_reader import ConfigReader, DataReader
from random_utils import RandomJoker, RandomNumber
from sci_utils.base_converter import BaseConverter
from sci_utils.constants import Constants
from sci_utils.unit_converter import UnitConverter
from docs import *


class Bot:
    def __init__(self):
        self.retrieve_config()
        self.retrieve_data()

    def retrieve_config(self):
        config_reader = ConfigReader("config.txt")
        self.config = config_reader.retrieve_config()

    def retrieve_data(self):
        constants_filename = self.config["constants_file"]
        length_filename = self.config["length_units_file"]
        area_filename = self.config["area_units_file"]
        volume_filename = self.config["volume_units_file"]
        time_filename = self.config["time_units_file"]
        speed_filename = self.config["speed_units_file"]
        pressure_filename = self.config["pressure_units_file"]

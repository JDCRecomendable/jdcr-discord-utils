#!/usr/bin/env python3

from data_reader import DataReader, ConfigReader
from sci_utils.base_converter import BaseConverter
from sci_utils.constants import Constants
from sci_utils.unit_converter import UnitConverter
from docs import *

config_reader    =   ConfigReader("config.txt")

constants_reader =   DataReader("data/constants.txt")
length_reader    =   DataReader("data/units_length.txt")
area_reader      =   DataReader("data/units_area.txt")
volume_reader    =   DataReader("data/units_volume.txt")
time_reader      =   DataReader("data/units_time.txt")
speed_reader     =   DataReader("data/units_speed.txt")
pressure_reader  =   DataReader("data/units_pressure.txt")

constant_names = constants_reader.retrieve_data_names()
constant_values = constants_reader.retrieve_data_values()
constant_aliases = constants_reader.retrieve_data_aliases()

length_names = length_reader.retrieve_data_names()
length_values = length_reader.retrieve_data_values()
length_aliases = length_reader.retrieve_data_aliases()

area_names = area_reader.retrieve_data_names()
area_values = area_reader.retrieve_data_values()
area_aliases = area_reader.retrieve_data_aliases()

volume_names = volume_reader.retrieve_data_names()
volume_values = volume_reader.retrieve_data_values()
volume_aliases = volume_reader.retrieve_data_aliases()

time_names = time_reader.retrieve_data_names()
time_values = time_reader.retrieve_data_values()
time_aliases = time_reader.retrieve_data_aliases()

speed_names = speed_reader.retrieve_data_names()
speed_values = speed_reader.retrieve_data_values()
speed_aliases = speed_reader.retrieve_data_aliases()

pressure_names = pressure_reader.retrieve_data_names()
pressure_values = pressure_reader.retrieve_data_values()
pressure_aliases = pressure_reader.retrieve_data_aliases()

base_converter = BaseConverter()
constants = Constants(constant_names, constant_values, constant_aliases)
length_converter = UnitConverter(length_names, length_values, length_aliases)
area_converter = UnitConverter(area_names, area_values, area_aliases)
volume_converter = UnitConverter(volume_names, volume_values, volume_aliases)
time_converter = UnitConverter(time_names, time_values, time_aliases)
speed_converter = UnitConverter(speed_names, speed_values, speed_aliases)
pressure_converter = UnitConverter(pressure_names, pressure_values, pressure_aliases)

print(length_converter.convert(1, "inch", "millimetre"))
print(speed_converter.convert(1, "kmph", "metre per second"))
print(time_converter.convert(2, "fortnight", "day"))
print(list_length_units(length_names, length_aliases))
print(list_area_units(area_names, area_aliases))
print(list_volume_units(volume_names, volume_aliases))
print(list_time_units(time_names, time_aliases))
print(list_speed_units(speed_names, speed_aliases))
print(list_pressure_units(pressure_names, pressure_aliases))
print(list_constants(constant_names, constant_aliases))
print(config_reader.retrieve_config())

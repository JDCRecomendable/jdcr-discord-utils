# Documentation Strings
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
#
# Contains the documentation strings for the JDCR Discord Utils
# bot.


DOC_STD_TITLE = """
JDCR Discord Utils 0.3
Copyright (c) 2020 Jared Recomendable.
Licensed under the GNU GPL v3. This program is provided with
ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
"""


DOC_MAIN_USAGE = """
USAGE: $<command> [options]

COMMANDS:
  help              display this document
  base <params>     convert integers from one base to another
  constant <param>  display constant value and unit
  convert <params>  convert units
  grad <params>     get information about graduation
  random <option>   display a random value from the desired category

BASE PARAMETERS:
  $base  <orig_value>  <from_base>  to  <to_base>
  E.g. `$base 7E b30 to b2`
  More details available by calling `$help base`.

CONSTANT PARAMETER:
  $constant  <constant>
  E.g. `$constant avogadro-constant`
  More details available by calling `$help constant`.

CONVERT PARAMETERS:
  $convert  <category>  <orig_value>  <from_unit>  to  <to_unit>
  E.g. `$convert length 25 metre to furlong`
  More details available by calling `$help convert`.

GRAD PARAMETERS:
  $grad  <input_type>  <value>
  E.g. `$grad gpa 9.0`
  More details available by calling `$help grad`.

RANDOM PARAMETER:
  $random  <category>
  E.g. `$random joke`
  More details available by calling `$help random`.
"""


DOC_BASE_CONVERTER_USAGE = """
USAGE: $base <orig_value> <from_base> to <to_base>

EXAMPLES:
  $base 128 b10 to b2
  $base A2 b16 to b8
  $base 14 b8 to b12
  $base 11100000 b2 to b30

LIMITATIONS:
  This program only deals with integers, from base 2 to base 30.
"""


DOC_CONSTANTS_USAGE = """
USAGE: $constant <constant>

EXAMPLES:
  $constant avogadro-constant
  $constant na
  $constant gravitational-constant
  $constant ga
  $constant speed-of-light
  $constant c

List all constants by calling `$help constant list`.
"""


DOC_CONSTANTS_LIST = "LIST OF CONSTANTS:"


DOC_UNIT_CONVERTER_USAGE = """
USAGE: $convert <category> <orig_value> <from_unit> to <to_unit>

EXAMPLES:
  $convert length 25 metre to furlong
  $convert length 25 m to furlong
  $convert speed 8 metre-per-second to kilometre-per-hour
  $convert speed 8 m/s to km/h
  $convert pressure 5 bar to megapascal
  $convert pressure 5 bar to mpa

CATEGORIES:
  length    $help convert length
  area      $help convert area
  volume    $help convert volume
  time      $help convert time
  speed     $help convert speed
  pressure  $help convert pressure
"""


DOC_UNITS_LIST = "LIST OF {} UNITS:"


DOC_GRAD_UTILS_USAGE = """
USAGE: $grad <input_type> <value>

EXAMPLES:
  $grad honours first class
  $grad honours 1st class
  $grad honours second class, first division
  $grad honours 2nd class division 1
  $grad honours class 2 2nd division
  $grad honours class 2nd
  $grad gpa 7.0
  $grad gpa 8
"""


DOC_RANDOM_UTILS_USAGE = """
USAGE: $random <category>

CATEGORIES:
  float      get a float with range [0.0, 1.0)
  integer    get an integer from 0 to 9999
  joke       get a lame joke
"""

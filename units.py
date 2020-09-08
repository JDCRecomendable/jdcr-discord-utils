MSG_DOC_UNITS = """```
CLI Unit Converter
JDCR Discord Utilities 0.3
Copyright (c) 2020 Jared Recomendable.

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
  pressure  $help convert pressure```
"""

MSG_DOC_UNITS_LENGTH = """```
LENGTH UNITS:
  metre | m
  nautical-mile
  hectometre
  kilometre | km
  decimetre | dm
  centimetre | cm
  millimetre | mm
  micrometre | um
  nanometre | nm
  angstrom
  mile | ml
  furlong
  chain
  rod
  horse-length
  fathom
  yard | yd
  foot | ft
  inch | in
  astronomical-unit
  light-year
  parsec```
"""

MSG_DOC_UNITS_AREA = """```
AREA UNITS:
  square-metre | m^2
  square-kilometre | km^2
  square-decimetre | dm^2
  square-centimetre | cm^2
  square-millimetre | mm^2
  square-micrometre | um^2
  are
  stremma
  hectare
  tetrad
  hectad
  myriad
  square-mile | mi^2
  square-yard | yd^2
  square-foot | ft^2
  square-inch | in^2
  acre
  rood
  section
  survey-township```
"""

MSG_DOC_UNITS_VOLUME = """```
VOLUME UNITS:
  cubic-metre | m^3
  cubic-centimetre | cm^3 | cc
  cubic-millimetre | mm^3
  cubic-yard | yd^3
  cubic-foot | ft^3
  cubic-inch | in^3
  litre | l
  millilitre | ml
  barrel
  gallon
  quart
  pint
  cup
  tablespoon
  teaspoon```
"""

MSG_DOC_UNITS_TIME = """```
TIME UNITS:
  second | sec | s
  millisecond | ms
  microsecond | us
  nanosecond | ns
  minute | min | m
  hour | hr | h
  day | d
  week | wk | w
  fortnight
  year | yr | y
  leap-year | lyr | ly```
"""

MSG_DOC_UNITS_SPEED = """```
SPEED UNITS:
  metre-per-second | m/s
  metre-per-minute | m/min
  metre-per-hour | m/hr | m/h
  kilometre-per-second | km/s
  kilometre-per-minute | km/min
  kilometre-per-hour | km/hr | km/h
  speed-of-light | c
  foot-per-second | ft/s
  foot-per-minute | ft/min
  foot-per-hour | ft/hr | ft/h
  mile-per-second | mi/s
  mile-per-minute | mi/min
  mile-per-hour | mi/hr | mi/h
  mach
  knot```
"""

MSG_DOC_UNITS_PRESSURE = """```
PRESSURE UNITS:
  pascal | pa
  hectopascal | hpa
  kilopascal | kpa
  megapascal | mpa
  gigapascal | gpa
  standard-atmosphere | atm
  technical-atmosphere
  bar
  kilobar | kbar
  megabar
  decibar | dbar
  centibar | cbar
  millibar | mbar
  millimetre-of-mercury | mmhg
  centimetre-of-mercury | cmhg
  inch-of-mercury | inhg
  foot-of-mercury | fthg
  millimetre-of-water | mmh2o
  centimetre-of-water | cmh2o
  metre-of-water | mh2o
  inch-of-water | inh2o
  foot-of-water | fth2o
  pound-per-square-inch | psi
  torr```
"""


unit_names = {
    # LENGTHS
    "length-metre": 0,
    "length-m": 0,
    "length-nautical-mile": 1,
    "length-hectometre": 2,
    "length-kilometre": 3,
    "length-km": 3,
    "length-decimetre": 4,
    "length-dm": 4,
    "length-centimetre": 5,
    "length-cm": 5,
    "length-millimetre": 6,
    "length-mm": 6,
    "length-micrometre": 7,
    "length-um": 7,
    "length-nanometre": 8,
    "length-nm": 8,
    "length-angstrom": 9,
    "length-mile": 10,
    "length-mi": 10,
    "length-furlong": 11,
    "length-chain": 12,
    "length-rod": 13,
    "length-horse-length": 14,
    "length-fathom": 15,
    "length-yard": 16,
    "length-yd": 16,
    "length-foot": 17,
    "length-ft": 17,
    "length-inch": 18,
    "length-in": 18,
    "length-astronomical-unit": 19,
    "length-light-year": 20,
    "length-parsec": 21,


    # AREA
    "area-square-metre": 22,
    "area-m^2": 22,
    "area-square-kilometre": 23,
    "area-km^2": 23,
    "area-square-decimetre": 24,
    "area-dm^2": 24,
    "area-square-centimetre": 25,
    "area-cm^2": 25,
    "area-square-millimetre": 26,
    "area-mm^2": 26,
    "area-square-micrometre": 27,
    "area-um^2": 27,
    "area-are": 28,
    "area-stremma": 29,
    "area-hectare": 30,
    "area-tetrad": 31,
    "area-hectad": 32,
    "area-myriad": 33,
    "area-square-mile": 34,
    "area-mi^2": 34,
    "area-square-yard": 35,
    "area-yd^2": 35,
    "area-square-foot": 36,
    "area-ft^2": 36,
    "area-square-inch": 37,
    "area-in^2": 37,
    "area-acre": 38,
    "area-rood": 39,
    "area-section": 40,
    "area-survey-township": 41,


    # VOLUME
    "volume-cubic-metre": 42,
    "volume-m^3": 42,
    "volume-cubic-centimetre": 43,
    "volume-cm^3": 43,
    "volume-cc": 43,
    "volume-cubic-millimetre": 44,
    "volume-mm^3": 44,
    "volume-cubic-yard": 45,
    "volume-yd^3": 45,
    "volume-cubic-foot": 46,
    "volume-ft^3": 46,
    "volume-cubic-inch": 47,
    "volume-in^3": 47,
    "volume-litre": 48,
    "volume-l": 48,
    "volume-millilitre": 49,
    "volume-ml": 49,
    "volume-barrel": 50,
    "volume-gallon": 51,
    "volume-quart": 52,
    "volume-pint": 53,
    "volume-cup": 54,
    "volume-tablespoon": 55,
    "volume-teaspoon": 56,


    # TIME
    "time-second": 57,
    "time-sec": 57,
    "time-s": 57,
    "time-millisecond": 58,
    "time-ms": 58,
    "time-microsecond": 59,
    "time-us": 59,
    "time-nanosecond": 60,
    "time-ns": 60,
    "time-minute": 61,
    "time-min": 61,
    "time-m": 61,
    "time-hour": 62,
    "time-hr": 62,
    "time-h": 62,
    "time-day": 63,
    "time-d": 63,
    "time-week": 64,
    "time-wk": 64,
    "time-w": 64,
    "time-fortnight": 65,
    "time-year": 66,
    "time-yr": 66,
    "time-y": 66,
    "time-leap-year": 67,
    "time-lyr": 67,
    "time-ly": 67,


    # SPEED
    "speed-metre-per-second": 68,
    "speed-m/s": 68,
    "speed-metre-per-minute": 69,
    "speed-m/min": 69,
    "speed-metre-per-hour": 70,
    "speed-m/hr": 70,
    "speed-m/h": 70,
    "speed-kilometre-per-second": 71,
    "speed-km/s": 71,
    "speed-kilometre-per-minute": 72,
    "speed-km/min": 72,
    "speed-kilometre-per-hour": 73,
    "speed-km/hr": 73,
    "speed-km/h": 73,
    "speed-speed-of-light": 74,
    "speed-c": 74,
    "speed-foot-per-second": 75,
    "speed-ft/s": 75,
    "speed-foot-per-minute": 76,
    "speed-ft/min": 76,
    "speed-foot-per-hour": 77,
    "speed-ft/hr": 77,
    "speed-ft/h": 77,
    "speed-mile-per-second": 78,
    "speed-mi/s": 78,
    "speed-mile-per-minute": 79,
    "speed-mi/min": 79,
    "speed-mile-per-hour": 80,
    "speed-mi/hr": 80,
    "speed-mi/h": 80,
    "speed-mach": 81,
    "speed-knot": 82,


    # PRESSURE
    "pressure-pascal": 83,
    "pressure-pa": 83,
    "pressure-hectopascal": 84,
    "pressure-hpa": 84,
    "pressure-kilopascal": 85,
    "pressure-kpa": 85,
    "pressure-megapascal": 86,
    "pressure-mpa": 86,
    "pressure-gigapascal": 87,
    "pressure-gpa": 87,
    "pressure-standard-atmosphere": 88,
    "pressure-atm": 88,
    "pressure-technical-atmosphere": 89,
    "pressure-bar": 90,
    "pressure-kilobar": 91,
    "pressure-kbar": 91,
    "pressure-megabar": 92,
    "pressure-decibar": 93,
    "pressure-dbar": 93,
    "pressure-centibar": 94,
    "pressure-cbar": 94,
    "pressure-millibar": 95,
    "pressure-mbar": 95,
    "pressure-millimetre-of-mercury": 96,
    "pressure-mmhg": 96,
    "pressure-centimetre-of-mercury": 97,
    "pressure-cmhg": 97,
    "pressure-inch-of-mercury": 98,
    "pressure-inhg": 98,
    "pressure-foot-of-mercury": 99,
    "pressure-fthg": 99,
    "pressure-millimetre-of-water": 100,
    "pressure-mmh2o": 100,
    "pressure-centimetre-of-water": 101,
    "pressure-cmh2o": 101,
    "pressure-metre-of-water": 102,
    "pressure-mh2o": 102,
    "pressure-inch-of-water": 103,
    "pressure-inh2o": 103,
    "pressure-foot-of-water": 104,
    "pressure-fth2o": 104,
    "pressure-pound-per-square-inch": 105,
    "pressure-psi": 105,
    "pressure-torr": 106
}


unit_values = {
    # LENGTH
    0 : 1,
    1 : 1852,
    2 : 100,
    3 : 1000,
    4 : 0.1,
    5 : 0.01,
    6 : 0.001,
    7 : 0.000001,
    8 : 0.000000001,
    9 : 0.0000000001,
    10: (1 / 3.280839895) * 5280,
    11: (1 / 3.280839895) * 660,
    12: (1 / 3.280839895) * 66,
    13: (1 / 3.280839895) * 16.5,
    14: (1 / 3.280839895) * 8,
    15: (1 / 3.280839895) * 6,
    16: (1 / 3.280839895) * 3,
    17: 1 / 3.280839895,
    18: (1 / 3.280839895) / 12,
    19: 149597900000,
    20: 9460730000000000,
    21: 30856782064650000,


    # AREA
    22: 1,
    23: 1000000,
    24: 0.01,
    25: 0.0001,
    26: 0.000001,
    27: 0.000000000001,
    28: 100,
    29: 1000,
    30: 10000,
    31: 4000000,
    32: 100000000,
    33: 10000000000,
    34: (1 / 1.19599004630108) * 3097600,
    35: (1 / 1.19599004630108),
    36: (1 / 1.19599004630108) / 9,
    37: (1 / 1.19599004630108) / 1296,
    38: (1 / 1.19599004630108) * 4840,
    39: (1 / 1.19599004630108) * 1210,
    40: (1 / 1.19599004630108) * 3097600,
    41: (1 / 1.19599004630108) * 111513600,


    # VOLUME
    42: 1,
    43: 0.000001,
    44: 0.000000001,
    45: 1 / 1.30795061931439,
    46: (1 / 1.30795061931439) / 27,
    47: (1 / 1.30795061931439) / 46656,
    48: 0.001,
    49: 0.000001,
    50: ((1 / 1.30795061931439) / 46656) * 9702,
    51: 1 / 219.969248299088,
    52: (1 / 219.969248299088) / 4,
    53: (1 / 219.969248299088) / 8,
    54: 4226.75283773038,
    55: 4226.75283773038 / 16,
    56: 4226.75283773038 / 48,


    # TIME
    57: 1,
    58: 0.001,
    59: 0.000001,
    60: 0.000000001,
    61: 60,
    62: 3600,
    63: 86400,
    64: 604800,
    65: 1209600,
    66: 31536000,
    67: 31622400,


    # SPEED
    68: 1,
    69: 1 / 60,
    70: 1 / 3600,
    71: 1000,
    72: 1000 / 60,
    73: 1 / 3.6,
    74: 299792458,
    75: 1 / 3.28083989,
    76: (1 / 3.280839895) / 60,
    77: (1 / 3.280839895) / 3600,
    78: (1 / 3.280839895) * 5280,
    79: (1 / 3.280839895) * 5280 / 60,
    80: (1 / 3.280839895) * 5280 / 3600,
    81: 340,
    82: 1852 / 3600,


    # PRESSURE
    83 : 1,
    84 : 100,
    85 : 1000,
    86 : 1000000,
    87 : 1000000000,
    88 : 101325,
    89 : 98066.5,
    90 : 100000,
    91 : 100000000,
    92 : 100000000000,
    93 : 10000,
    94 : 1000,
    95 : 100,
    96 : 133.322387415,
    97 : 1333.22387415,
    98 : 133322.387415 * ((1 / 3.280839895) / 12),
    99 : 133322.387415 * (1 / 3.280839895),
    100: 9.80664857,
    101: 98.0664857,
    102: 9806.64857,
    103: 9806.64857 * ((1 / 3.280839895) / 12),
    104: 9806.64857 * (1 / 3.280839895),
    105: 6894.75729,
    106: 101325 / 760
}

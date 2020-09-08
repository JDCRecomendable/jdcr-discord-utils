MSG_DOC_CONSTANTS = """```
CLI Constants
JDCR Discord Utilities 0.3
Copyright (c) 2020 Jared Recomendable.

USAGE: $constant <constant>

EXAMPLES:
  $constant avogadro-constant
  $constant na
  $constant gravitational-constant
  $constant ga
  $constant speed-of-light
  $constant c

CONSTANTS:
  avogadro-constant | na
  boltzmann-constant | kb
  coulomb-constant | kc
  elementary-charge | e- | e
  molar-gas-constant | r
  gravitational-constant | ga
  electron-mass | me
  proton-mass | mp
  neutron-mass | mn
  magnetic-constant | u0
  electric-constant | e0
  planck-constant | h
  speed-of-light | c
  unified-atomic-mass-unit | u```
"""


constant_names = {
    "avogadro-constant": 0,
    "na": 0,
    "boltzmann-constant": 1,
    "kb": 1,
    "coulomb-constant": 2,
    "kc": 2,
    "elementary-charge": 3,
    "e-": 3,
    "e": 3,
    "molar-gas-constant": 4,
    "r": 4,
    "gravitational-constant": 5,
    "ga": 5,
    "electron-mass": 6,
    "me": 6,
    "proton-mass": 7,
    "mp": 7,
    "neutron-mass": 8,
    "mn": 8,
    "magnetic-constant": 9,
    "u0": 9,
    "electric-constant": 10,
    "e0": 10,
    "planck-constant": 11,
    "h": 11,
    "speed-of-light": 12,
    "c": 12,
    "unified-atomic-mass-unit": 13,
    "u": 13
}


constant_values = {
    0 : "6.02214129 E23 mol^(-1)",
    1 : "1.3806488 E(-23) J/K",
    2 : "8.987551787 E9 Nm²/C²",
    3 : "1.602176565 E(-19) C",
    4 : "8.3144621 J/mol K",
    5 : "6.67384 E(-11) m³ / kg s²",
    6 : "9.10938291 E(-31) kg",
    7 : "1.672621777 E(-27) kg",
    8 : "1.674927351 E(-27) kg",
    9 : "1.256637061 E(-6) N/A²",
    10: "8.854187817 E(-12) F/m",
    11: "6.62606957 E(-34) Js",
    12: "2.99792458 E(8) m/s",
    13: "1.660538921 E(-27) kg"
}

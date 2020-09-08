MSG_DOC_BASE_CONV = """```
CLI Base Converter
JDCR Discord Utilities 0.3
Copyright (c) 2020 Jared Recomendable.

USAGE: $base <orig_value> <from_base> to <to_base>

EXAMPLES:
  $base 128 b10 to b2
  $base A2 b16 to b8
  $base 14 b8 to b12
  $base 11100000 b2 to b30

LIMITATIONS:
  This program only deals with integers, from base 2 to base 30.```
"""

def to_dec(val, base):
    """Convert value from specified base to decimal."""
    return int(val, base)

def from_dec(val, base):
    """Convert value from decimal to specified base."""
    result = ""
    string_res = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while val:
        result += string_res[val % base]
        val //= base
    return result[::-1]

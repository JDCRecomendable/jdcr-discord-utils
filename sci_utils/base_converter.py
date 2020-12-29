# Base Converter
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
#
# Contains the class for base conversion.


class BaseConverter:
    def __init__(self):
        self.symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def convert(self, val, fr_base, to_base):
        """Convert value from one base to another."""
        if 1 < fr_base < 31 and 1 < to_base < 31 and val > -1:
            return self.from_dec(self.to_dec(val, fr_base), to_base)
        return -1

    def to_dec(self, val, base):
        """Convert value from specified base to decimal."""
        if 1 < base < 31 and val > -1:
            return int(val, base)
        return -1

    def from_dec(self, val, base):
        """Convert value from decimal to specified base."""
        if 1 < base < 31 and val > -1:
            result = ""
            while val:
                result += self.symbols[val % base]
                val //= base
            return result[::-1]
        return -1

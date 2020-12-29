# Unit Converter
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESSED OR IMPLIED.
#
# Contains the class for unit conversion. Create an object for
# each unit category.


from sci_utils.common_sci_utils import DataClass


class UnitConverter(DataClass):
    def __init__(self, names, values, alias_list):
        super().__init__(names, values, alias_list)

    def convert(self, value, fr_unit, to_unit):
        fr_index = self.auto_get_index(fr_unit)
        to_index = self.auto_get_index(to_unit)
        if fr_index > -1 and to_index > -1:
            fr_value = self.get_value_by_index(fr_index)
            to_value = self.get_value_by_index(to_index)
            return value * fr_value / to_value
        return -1

# Constants
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
#
# Contains the class for constants.


from sci_utils.common_sci_utils import DataClass


class Constants(DataClass):
    def __init__(self, names, values, alias_list):
        super().__init__(names, values, alias_list)

    def get_constant(self, cnst):
        index = self.auto_get_index(cnst)
        if index > -1:
            value = self.get_value_by_index(index)
            return value
        return -1

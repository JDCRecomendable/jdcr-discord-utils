# Common Science Utils
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
#
# Contains the class for inheritance by Unit Converter class
# and Constant class.


class DataClass:
    def __init__(self, names, values, alias_list):
        self.names = names
        self.names_lower = []
        self.values = values
        self.alias_list = alias_list
        for name in names:
            self.names_lower.append(name.lower())

    def update_data(self, names, values, alias_list):
        self.__init__(names, values, alias_list)

    def get_names(self):
        return self.names

    def get_values(self):
        return self.values

    def get_aliases(self):
        return self.alias_list

    def auto_get_index(self, data):
        index = self.get_index_by_name(data)
        if index == -1:
            index = self.get_index_by_alias(data)
        return index

    def get_index_by_name(self, data_name):
        if not self.names_lower.count(data_name.lower()):
            return -1
        return self.names_lower.index(data_name.lower())

    def get_index_by_alias(self, data_alias):
        index = 0
        for aliases in self.alias_list:
            if aliases.count(data_alias.lower()):
                return index
            index += 1
        return -1

    def get_name_by_index(self, data_index):
        return self.names[data_index]

    def get_value_by_index(self, data_index):
        return self.values[data_index]

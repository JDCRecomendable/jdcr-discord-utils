# Data Reading Utils
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.


class FileReader:
    def __init__(self, filename):
        """Create a FileReader object for reading from a single
        file.
        """
        self.lines = self._read_file(filename)

    def _read_file(self, filename):
        lines = []
        with open(filename) as f:
            for line in f:
                lines.append(line.rstrip())
        return lines


class ConfigReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def retrieve_config(self):
        config = {}
        for line in self.lines:
            key = line.split("=")[0]
            value = line.split("=")[1]
            config[key] = self._process_value(value)
        return config
    
    def _process_value(self, value):
        if value[0] == "[" and value[-1] == "]":
            value = value[1:-1].split(",")
        if value[0] == "{" and value[-1] == "}":
            dictionary = {}
            dict_elements = value[1:-1].split(",")
            for element in dict_elements:
                header, value = element.split(":")
                dictionary[header] = value
            value = dictionary
        return value


class DataReader(FileReader):
    def __init__(self, filename):
        super().__init__(filename)

    def retrieve_data_names(self):
        names = []
        for line in self.lines:
            word_num = int(line.split(" ")[0])
            name = ""
            for i in range(word_num):
                name += line.split(" ")[2+i] + " "
            names.append(name.strip())
        return names

    def retrieve_data_values(self):
        values = []
        for line in self.lines:
            value = float(line.split(" ")[1])
            values.append(value)
        return values

    def retrieve_data_aliases(self):
        alias_list = []
        for line in self.lines:
            word_num = int(line.split(" ")[0])
            aliases = line.split(" ")[2+word_num:]
            alias_list.append(aliases)
        return alias_list

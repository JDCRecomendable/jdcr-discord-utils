# Documentation Functions
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
#
# Contains the documentation functions for the JDCR Discord Utils
# bot. Takes documentation strings from `doc_strings.py`.


from doc_strings import *


def get_main_help_usage():
    string = DOC_STD_TITLE
    string += DOC_MAIN_USAGE
    return "```\n{}```".format(string)


def get_base_converter_help_usage():
    string = DOC_STD_TITLE
    string += DOC_BASE_CONVERTER_USAGE
    return "```\n{}```".format(string)


def get_constants_help_usage():
    string = DOC_STD_TITLE
    string += DOC_CONSTANTS_USAGE
    return "```\n{}```".format(string)


def get_unit_converter_help_usage():
    string = DOC_STD_TITLE
    string += DOC_UNIT_CONVERTER_USAGE
    return "```\n{}```".format(string)

def get_grad_utils_help_usage():
    string = DOC_STD_TITLE
    string += DOC_GRAD_UTILS_USAGE
    return "```\n{}```".format(string)

def get_random_utils_help_usage():
    string = DOC_STD_TITLE
    string += DOC_RANDOM_UTILS_USAGE
    return "```\n{}```".format(string)


def list_items(string, names, aliases):
    for i in range(len(names)):
        string += "\n  {0:<26}:".format(names[i].upper())
        for alias in aliases[i]:
            string += "   {}".format(alias)
    return "```\n{}```".format(string)


def list_constants(names, aliases):
    return list_items(DOC_CONSTANTS_LIST, names, aliases)


def list_units(category, names, aliases):
    return list_items(DOC_UNITS_LIST.format(category.upper()), names, aliases)

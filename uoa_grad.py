# UoA Graduation Utility
# for JDCR Discord Utils 0.3
# Copyright (c) 2023 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.
#
# Contains the class for mapping honours levels to GPAs.


class UoAGraduationUtility:
    def __init__(self):
        self.honours_levels = {
            1: ["first class", "1st class", "class 1", "class first", "class 1st"],
            2: ["second class", "2nd class", "class 2", "class second", "class 2nd"]
        }
        self.second_class_honours_divisions = {
            1: ["first division", "1st division", "first div", "1st div", "div 1", "division 1"],
            2: ["second division", "2nd division", "second div", "2nd div", "div 2", "division 2"]
        }
        self.honours_gpas = [7.0, 5.5, 4.0, 1.0]

    def get_honours_level_answer_string(self, honours_level_string_input):
        answer_string = ""

        selected_honours_level = []
        selected_second_class_honours_divisions = []

        for honours_level in self.honours_levels:
            for honours_level_string in self.honours_levels[honours_level]:
                if honours_level_string in honours_level_string_input.lower():
                    selected_honours_level.append(honours_level)
                    honours_level_string_input = honours_level_string_input.replace(honours_level_string, "")
                    break

        if 2 in selected_honours_level:
            for second_class_honours_division in self.second_class_honours_divisions:
                for second_class_honours_division_string in self.second_class_honours_divisions[second_class_honours_division]:
                    if second_class_honours_division_string in honours_level_string_input.lower():
                        selected_second_class_honours_divisions.append(second_class_honours_division)
                        honours_level_string_input = honours_level_string_input.replace(second_class_honours_division_string, "")
                        break

        if 1 in selected_honours_level:
            answer_string += " For first class honours, you need a GPA of 7.0 and above."
        if 2 in selected_honours_level:
            if 1 in selected_second_class_honours_divisions:
                answer_string += " For second class, first division honours, you need a GPA between 5.5 and 6.9."
            elif 2 in selected_second_class_honours_divisions:
                answer_string += " For second class, second division honours, you need a GPA between 4.0 and 5.4."
            else:
                answer_string += " For second class honours, you need a GPA between 4.0 and 6.9."

        if answer_string == "":
            answer_string += "Sorry, I did not understand your input\n¯\_(ツ)_/¯"

        return answer_string.strip()


    def get_gpa_answer_string(self, gpa_string):
        try:
            gpa = float(gpa_string)
            if gpa >= 7.0:
                return f"A GPA of {gpa} gets you First class honours"
            elif gpa >= 5.5:
                return f"A GPA of {gpa} gets you Second class, First division"
            elif gpa >= 4.0:
                return f"A GPA of {gpa} gets you Second class, Second division"
            else:
                return f"No honours for you, your GPA of {gpa} is too low"
        except:
            return "Sorry, I did not understand your input\n¯\_(ツ)_/¯"

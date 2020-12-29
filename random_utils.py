# Random Utils
# for JDCR Discord Utils 0.3
# Copyright (c) 2020 Jared Recomendable.
# Licensed under the GNU GPL v3. This program is provided with
# ABSOLUTELY NO WARRANTY, EXPRESS OR IMPLIED.


from requests import get
from random import random, randrange


class RandomJoker:
    def __init__(self, joke_api_url, joke_api_headers):
        self.joke_api_url = joke_api_url
        self.joke_api_headers = joke_api_headers

    def get_joke(self):
        joke = get(self.joke_api_url, headers=self.joke_api_headers)
        return joke.text


class RandomNumber:
    def __init__(self):
        pass

    def get_integer(self):
        return randrange(1000)

    def get_float(self):
        return random()

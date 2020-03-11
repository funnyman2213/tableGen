import json
from random import choice
import click

class TableParser:

    def __init__(self, file):
        self.unparsed = json.load(file)
        self.scheme = self.unparsed.pop("scheme")
        self.options = self.unparsed

    def pick(self) -> str:
        '''picks data specified by the table and returns it'''
        # FIXME pick based on request
        picked = {}
        for key, val in self.options.items():
            picked[key] = choice(val)
        try:
            while True:
                self.scheme = self.scheme.format(**picked)
                if not "{" in self.scheme or not "}" in self.scheme:
                    break
        except ValueError as e:
            return(f"ValueError in scheme: {e}")

        return self.scheme
        
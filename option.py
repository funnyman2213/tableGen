import random

class Option:

    def __init__(self, optionlist: list):
        if type(optionlist) == list:
            self.optionlist = optionlist
        else:
            raise TypeError("Option list is not list")

    def pick(self):
        return random.choice(self.optionlist)

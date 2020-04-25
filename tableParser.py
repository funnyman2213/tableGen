import json
from random import choice
from table import Table
from option import Option

class TableParser:

    @staticmethod
    def parse(file):
        unparsed = json.load(file)
        scheme = unparsed.pop("scheme")
        options = unparsed.pop("options")
        meta = unparsed.pop("meta")

        for option, values in options.items():
            options.update({option: Option(values)})
        
        return Table(scheme, options, meta)
        
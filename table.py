import json
from option import Option
import re


class Table:

    def __init__(self, scheme: str, options: dict, meta: dict):
        self.scheme = scheme
        self.options = options
        self.meta = meta

    def generate(self) -> str:
        result = self.scheme
        
        try:
            # Creates a loop that doesn't close until there are no {} in the result
            while "{" in result or "}" in result:
                # Grabs the properties of the result, this is done recursivly to account for sub properties
                props = (x[1] for x in re.findall(r"(\{)(\w+)(\})", result))
                # Starts the filler list
                filler = list()

                for prop in props:
                    filler.append(self.options[prop].pick())
                
                result = re.sub(r"(\{)(\w+)(\})", lambda x: x.group(1)+x.group(3), result).format(*filler)
        except Exception as e:
            return "Error in Generate: " + e

        return result

    
import json
import re
import click
import random


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

    @staticmethod
    def parse(file):
        unparsed = json.load(file)
        scheme = unparsed.pop("scheme")
        options = unparsed.pop("options")
        meta = unparsed.pop("meta")

        for option, values in options.items():
            options.update({option: Option(values)})
        
        return Table(scheme, options, meta)

class Option:

    def __init__(self, optionlist: list):
        if type(optionlist) == list:
            self.optionlist = optionlist
        else:
            raise TypeError("Option list is not list")

    def pick(self):
        return random.choice(self.optionlist)


def createTable(table):
    '''Creates a table dictionary'''
    click.echo("the table needs a scheme")
    result = dict()
    scheme = click.prompt(f"{table}/Scheme", prompt_suffix="> ")
    result["scheme"]=scheme
    result["options"]=dict()
    result["meta"]=dict()

    props = (x[1] for x in re.findall(r"(\{)(\w+)(\})", scheme))

    single_props = list(set(props))

    occurances = dict(zip(single_props, [props.count(prop) for prop in single_props]))

    print(occurances)

    for prop in single_props:
        result["options"][f"{prop}"] = list()
        
        while True:
            current = click.prompt(f"{table}/{prop}", prompt_suffix="> ", default="", show_default=False)
            newprops = [x[1] for x in re.findall(r"(\{)(\w+)(\})", current)]
            
            if len(newprops) > 0:
                for newprop in newprops:
                    if newprop not in single_props:
                        single_props.append(newprop)

            if current == "":
                break

            result[f"{prop}"].append(current)

    return result
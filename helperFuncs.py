import click
import re


def createTable(table):
    '''Creates a table dictionary'''
    click.echo("the table needs a scheme")
    result = dict()
    scheme = click.prompt(f"{table}/Scheme", prompt_suffix="> ")
    result["scheme"]=scheme
    result["options"]=dict()

    props = [x.strip('{}') for x in re.findall(r"\{\w+\}", scheme)]

    single_props = list(set(props))

    occurances = dict(zip(single_props, [props.count(prop) for prop in single_props]))

    print(occurances)

    for prop in single_props:
        result["options"][f"{prop}"] = list()
        
        while True:
            current = click.prompt(f"{table}/{prop}", prompt_suffix="> ", default="", show_default=False)
            newprops = [x.strip('{}') for x in re.findall(r"\{\w+\}", current)]
            
            if len(newprops) > 0:
                for newprop in newprops:
                    if newprop not in single_props:
                        single_props.append(newprop)

            if current == "":
                break

            result[f"{prop}"].append(current)

    return result

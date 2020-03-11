import click
import re


def createTable(table):
    '''Creates a table dictionary'''
    click.echo("the table needs a scheme")
    result = dict()
    scheme = click.prompt(f"{table}/Scheme", prompt_suffix="> ")

    props = list(set([x.strip('{}') for x in re.findall(r"\{\w+\}", scheme)]))

    for prop in props:
        result[f"{prop}"] = list()
        
        while True:
            current = click.prompt(f"{table}/{prop}", prompt_suffix="> ", default="", show_default=False)
            newprops = [x.strip('{}') for x in re.findall(r"\{\w+\}", current)]
            
            if len(newprops) > 0:
                for newprop in newprops:
                    if newprop not in props:
                        props.append(newprop)

            if current == "":
                break

            result[f"{prop}"].append(current)

    return result

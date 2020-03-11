import click
import re


def createTable(table):
    '''Creates a table dictionary'''
    # this is more verbose then it needs to be
    click.echo("the table needs a scheme")
    scheme = click.prompt(f"{table}")

    props = [x.strip('{}') for x in re.findall(r"\{\w+\}", scheme)]

    for prop in props:
        next

    return {"Scheme": "nothing here yet"}

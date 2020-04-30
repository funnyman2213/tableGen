import click
import os
from click.testing import CliRunner
import json
from tableParser import TableParser
from helperFuncs import createTable


@click.group()
def main():
    pass


@main.command()
@click.argument("tables", required=True, nargs=-1)
@click.option("-f", "--folder", "folder", default="tables")
@click.pass_context
def gen(ctx, tables, folder):
    """Generates based on table"""
    generated = []
    
    for table in tables:
        try:
            with open(f"{folder}/{table}.json", 'r') as file:
                parsed = TableParser.parse(file)
                generated.append(f"{table}: {parsed.generate()}")
        except FileNotFoundError:
            if click.confirm("[Error] File not found!\nwould you like to Create this table now?", default=True ):
                ctx.invoke(create, table=table, folder=folder)
        except Exception as e:
            click.echo(f"Error: {e} ")
    
    [click.echo(f"{x}") for x in generated] # FIXME this is a horrible work around but I wanted 1 line


@main.command()
@click.argument("table", type=str)
@click.option("-f", "--folder", "folder", default="tables", required=False)
def create(table, folder):
    tableDict = createTable(table)
    if not os.path.exists(folder):
        try:
            os.mkdir(folder)
        except Exception as e:
            print(f"Error creating folder {e}")
    with open(f"{folder}/{table}.json",'w') as f:
        print(json.dumps(tableDict, indent=4),file=f)
    click.echo(f"table {table}, created in {folder}")


# TODO add ability to edit tables
@main.command()
def edit():
    pass



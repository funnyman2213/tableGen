import click
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
                parsed = TableParser(file)
                generated.append(f"{table}: {parsed.pick()}")
        except FileNotFoundError:
            if click.confirm("[Error] File not found!\nwould you like to Create this table now?", default=True ):
                ctx.invoke(create, table=table, folder=folder)
        except Exception as e:
            click.echo(f"error {e}")
    
    [click.echo(f"{x}") for x in generated] # FIXME this is a horrible work around but I wanted 1 line


@main.command()
@click.argument("table", type=str)
@click.option("-f", "--folder", "folder", default="tables", required=False)
def create(table, folder):
    with open(f"{folder}/{table}.json",'w') as f:
        tableDict = createTable(table)
        print(json.dumps(tableDict, indent=4),file=f)
    click.echo(f"table {table}, created in {folder}")
    # TODO work a simple prompt based startup input


# TODO add ability to edit tables
@main.command()
def edit():
    pass

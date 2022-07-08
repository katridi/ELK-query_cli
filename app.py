import json
import sys
from typing import Dict

import click

from app_context import AppContext, create_app_context
from commands import fuzzy_term, match_term, geo_query



@click.command()
@click.pass_context
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--value", help="value for the term")
def match(ctx, term, value):
    query: Dict = match_term(term=term, value=value)
    searcher: AppContext = ctx.obj
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.pass_context
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--value", help="value for the term")
def fuzzy(ctx, term, value):
    query: Dict = fuzzy_term(term=term, value=value)
    searcher: AppContext = ctx.obj
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.argument("raw_query", type=click.File('r'), default=sys.stdin)
@click.pass_context
def raw(ctx, raw_query):
    """Takes stdin input for quering."""
    query: Dict = json.loads(raw_query.read())
    searcher: AppContext = ctx.obj
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.option("--distance", type=float, default=1, help="distance in km, default = 1")
@click.argument("long", type=float)
@click.argument("lat", type=float)
@click.pass_context
def geo(ctx, distance, long, lat):
    """Takes longitude and latitude input for quering."""
    searcher: AppContext = ctx.obj
    query: Dict = geo_query(long=long, lat=lat, distance=distance)
    print(json.dumps(query, indent=4, ensure_ascii=False))
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))
    

@click.group()
@click.pass_context
def cli(ctx):
    pass


if __name__ == "__main__":
    commands = [match, raw, fuzzy, geo]
    for command in commands:
        cli.add_command(command)
    # make decorator to pass es
    app_context = create_app_context()
    cli(obj=app_context)

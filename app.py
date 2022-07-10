import json
import sys
from typing import Dict

import click

from app_context import AppContext, create_app_context
from commands import fuzzy_term, geo_query, match_term, range_term, regexp_term, prefix_term


@click.command()
@click.pass_context
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--value", help="value for the term")
def match(ctx, term, value):
    """Takes term and value for direct search."""
    query: Dict = match_term(term=term, value=value or "")
    searcher: AppContext = ctx.obj
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.pass_context
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--value", help="value for the term")
def fuzzy(ctx, term, value):
    """Takes term and value for fuzzy search."""
    query: Dict = fuzzy_term(term=term, value=value or "")
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
@click.option("--geo_term", type=str, default="geo_distance", help="name of geo field")
@click.argument("long", type=float)
@click.argument("lat", type=float)
@click.pass_context
def geo(ctx, distance, geo_term, long, lat):
    """Takes term for longitude and latitude input for quering."""
    searcher: AppContext = ctx.obj
    query: Dict = geo_query(long=long, lat=lat, distance=distance, geo_term=geo_term)
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.pass_context
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--re", help="Regular expression for the term")
def regex(ctx, term, re):
    """Takes term and regular expression for search."""
    query: Dict = regexp_term(term=term, regex=re or "")
    searcher: AppContext = ctx.obj
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.option("--term", type=str, default="total_quantity", help="name of range field")
@click.option("--gte", type=str, help="lower bound greater or equal of range field")
@click.option("--lte", type=str, help="upper bound less or equal of range field")
@click.pass_context
def range(ctx, term, gte, lte):
    """Takes term for lower and upper bound input for quering."""
    searcher: AppContext = ctx.obj
    query: Dict = range_term(term=term, gte=gte, lte=lte)
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--pre", type=str, help="prefix for a term for quering")
@click.pass_context
def prefix(ctx, term, pre):
    """Takes term and prefix for quering."""
    searcher: AppContext = ctx.obj
    query: Dict = prefix_term(term=term, prefix=pre or "")
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.option("--term", default="customer_first_name.keyword", help="term for quering")
@click.option("--pre", type=str, help="prefix for a term for quering")
@click.pass_context
def prefix(ctx, term, pre):
    """Takes term and prefix for quering."""
    searcher: AppContext = ctx.obj
    query: Dict = prefix_term(term=term, prefix=pre or "")
    res: Dict = searcher.search_in_index(body=query)
    print(json.dumps(res, indent=4, ensure_ascii=False))


@click.command()
@click.argument("index_name", type=str)
@click.pass_context
def index(ctx, index_name):
    """Set index for quering."""
    searcher: AppContext = ctx.obj
    searcher.set_index(index_name=index_name)


@click.group()
@click.pass_context
def cli(ctx):
    pass


if __name__ == "__main__":
    commands = [match, raw, fuzzy, geo, regex, range, prefix, index]
    for command in commands:
        cli.add_command(command)
    app_context = create_app_context()
    cli(obj=app_context)

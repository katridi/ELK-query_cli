from typing import Dict, Optional


def match_term(term: str, value: str) -> Dict:
    return {"query": {"term": {term: {"value": value}}}}


def fuzzy_term(term: str, value: str) -> Dict:
    return {"query": {"fuzzy": {term: {"value": value}}}}


def geo_query(long: float, lat: float, distance: float, geo_term: str) -> Dict:
    return {
        "query": {
            "bool": {
                "must": {
                    "match_all": {}
                },
                "filter": {
                    geo_term: {
                        "distance": f'{distance}km',
                        "geoip.location": [long, lat]
                    }
                }
            }
        }
    }


def regexp_term(term: str, regex: str) -> Dict:
    return {"query": {"regexp": {term: {"value": regex}}}}


def range_term(term: str, gte: Optional[str], lte:  Optional[str]) -> Dict:
    return {
        "query": {
            "range": {
                term: {
                    **({"gte": gte} if gte else {}),
                    **({"lte": lte} if lte else {}),
                }
            }
        }
    }


def prefix_term(term: str, prefix: str) -> Dict:
    return {"query": {"prefix": {term: prefix}}}

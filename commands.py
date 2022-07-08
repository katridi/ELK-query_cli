from typing import Dict


def match_term(term: str, value: str) -> Dict:
    return {"query": {"term": {term: {"value": value}}}}


def fuzzy_term(term: str, value: str) -> Dict:
    return {"query": {"fuzzy": {term: {"value": value}}}}


def geo_query(long: float, lat: float, distance: float) -> Dict:
    return {
        "query": {
            "bool": {
                "must": {
                    "match_all": {}
                },
                "filter": {
                    "geo_distance": {
                        "distance": f'{distance}km',
                        "geoip.location": [long, lat]
                    }
                }
            }
        }
    }


def regexp_term(term: str, regex: str):
    return {"query": {"regexp": {term: {"value": regex}}}}

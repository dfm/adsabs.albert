# -*- coding: utf-8 -*-

"""Search the NASA ADS API

Synopsis: <trigger> <query>"""

import albertv0 as albert
import os
import re
import shlex

__iid__ = "PythonInterface/v0.1"
__prettyname__ = "NASA ADS"
__version__ = "1.0"
__trigger__ = "ads "
__author__ = "Dan Foreman-Mackey"
__dependencies__ = []

icon_path = albert.iconLookup("adsabs")
if not icon_path:
    icon_path = os.path.dirname(__file__) + "/adsabs.svg"


def parse_query_string(query):
    # Remove parentheses
    query = query.replace("(", " ").replace(")", " ")

    # Tokenize the query
    tokens = shlex.split(query)
    years = []
    authors = []
    for token in tokens:
        token = token.strip()
        numbers = re.findall("[0-9]+", token)
        years += list(int(n) for n in numbers if len(n) == 4)
        if len(numbers) == 0:
            authors.append(token)
    years = list(sorted(years))

    # Fail fast if there are no authors
    if len(authors) == 0:
        return query

    # Construct the query in ADS's format
    q = []
    for author in authors:
        q.append('author:"' + author + '"')
    if len(years) == 1:
        q.append("year:{0}".format(years[0]))
    elif len(years) > 1:
        q.append("year:[{0} TO {1}]".format(min(years), max(years)))
    q = " ".join(q)
    return q


def handleQuery(query):
    if not query.isTriggered:
        return albert.Item(
            id=__prettyname__,
            icon=icon_path,
            text=__prettyname__,
            subtext="Search NASA ADS",
            completion=query.rawString,
        )

    stripped = query.string.strip()
    query_string = parse_query_string(stripped)
    return [
        albert.Item(
            id=__prettyname__,
            icon=icon_path,
            text="Sorted by date",
            subtext="Execute search: " + query_string,
            completion=query.rawString,
            actions=[
                albert.UrlAction(
                    "Search on the web",
                    "https://ui.adsabs.harvard.edu/search/q=" + query_string,
                )
            ],
        ),
        albert.Item(
            id=__prettyname__,
            icon=icon_path,
            text="Sorted by citation count",
            subtext="Execute search: " + query_string,
            completion=query.rawString,
            actions=[
                albert.UrlAction(
                    "Search on the web",
                    "https://ui.adsabs.harvard.edu/search/q="
                    + query_string
                    + "&sort=citation_count desc",
                )
            ],
        ),
    ]

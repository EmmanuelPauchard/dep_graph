#!/usr/bin/env ipython3
"""
Validation tests for the module as a black box
"""
from dep_graph.analyzer import Analyzer
from dep_graph.parser import JsonParser

from common import reference


def test_reference_exercise(capsys):
    (data, expected, _) = reference
    # We expect output written to stdout
    Analyzer(JsonParser(data).parse()).run()
    assert capsys.readouterr().out == expected

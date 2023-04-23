#!/usr/bin/env ipython3
"""
Validation tests for the module as a black box
"""
from dep_graph.analyzer import Analyzer
from dep_graph.parser import JsonParser

reference = (
    """{
      "pkg1": ["pkg2", "pkg3"],
      "pkg2": ["pkg3"],
      "pkg3": []
    }
    """,
    """- pkg1
  - pkg2
    - pkg3
  - pkg3
- pkg2
  - pkg3
- pkg3
""",
)


def test_reference_exercise(capsys):
    (data, expected) = reference
    # We expect output written to stdout
    Analyzer(JsonParser(data).parse()).run()
    assert capsys.readouterr().out == expected

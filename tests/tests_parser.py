#!/usr/bin/env ipython3
test = """
{
"pkg1": ["pkg2", "pkg3"],
"pkg2": ["pkg3"],
"pkg3": [""]
}
"""


def test_reference():
    """Check that the reference example is implemented correctly."""
    pass


def test_empty_lines():
    """Check empty lines are not taken into account"""
    pass

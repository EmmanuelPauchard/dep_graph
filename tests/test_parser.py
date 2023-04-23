#!/usr/bin/env ipython3
import pytest

from dep_graph.parser import JsonParser
from common import reference


def test_reference():
    """Check that the reference example is implemented correctly."""
    assert JsonParser(reference[0]).parse() == reference[2]


@pytest.mark.xfail(reason="Does not handle empty strings deps")
def test_no_deps():
    """Case verifies that if the input data is valid json, but uses empty string
    to indicate package has no dep, then the parser correctly removes the empty
    string to leave an empty list.

    """
    assert JsonParser("""{"p": [""]}""").parse() == {"p": []}

#!/usr/bin/env ipython3
import pytest

from dep_graph.analyzer import Analyzer


from common import reference, StrVisitor

test_data = [
    (reference[2], reference[1], "Reference Example"),
    (
        {"pkg1": ["pkg2"], "pkg2": ["pkg1"]},
        """
- pkg1
  - pkg2
- pkg2
  - pkg1
        """,
        "Circular Dependency",
    ),
]


@pytest.mark.parametrize(
    "data, expected", [(d[0], d[1]) for d in test_data], ids=[d[2] for d in test_data]
)
def test_reference(data, expected):
    """Check that the reference example is implemented correctly."""
    r = StrVisitor()
    Analyzer(data, r).run()
    # Use strip to allow for a new line as first/last character
    assert r.res.strip() == expected.strip()

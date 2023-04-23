#!/usr/bin/env ipython3
from dep_graph import

reference = (
{
"pkg1": ["pkg2", "pkg3"],
"pkg2": ["pkg3"],
"pkg3": [],
},
"""
- pkg1
  - pkg2
    - pkg3
  - pkg3
- pkg2
  - pkg3
- pkg3
""",
)


def test_reference():
    """Check that the reference example is implemented correctly."""
    pass


def test_circular_dep():
    """Check that in case of circular dependency the analyzer stops after 1 loop"""
    pass

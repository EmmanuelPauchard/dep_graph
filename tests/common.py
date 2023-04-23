#!/usr/bin/env ipython3

from dep_graph.analyzer import PackageVisitor

"""
Reference Example, as 3-uple:
- JSON
- Expected output
- Object representation
"""
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
    {
        "pkg1": ["pkg2", "pkg3"],
        "pkg2": ["pkg3"],
        "pkg3": [],
    },
)


class StrVisitor(PackageVisitor):
    """Instead of outputting to stdout, this visitor concatenates the same text
    to a string

    """

    res = ""

    def visit(self, level, package_name):
        self.res += "  " * level + "- " + package_name + "\n"

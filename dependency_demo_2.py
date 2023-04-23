#!/usr/bin/env ipython3
test = """
{
"pkg1": ["pkg2", "pkg3"],
"pkg2": ["pkg3"],
"pkg3": ["pkg4"]
"pkg4": []
}
"""

import json

packages = json.loads(test)

# packages["pkg3"] = ["pkg1"]


def print_package(level, name):
    print("  " * level + "- " + name)


def print_level(dependencies: list[str], parent: list[str] = [], level: int = 0):
    """
    Note: relies on the fact that dependencies is always a list, empty if no dependencies
    :param parent: list of direct ancestors to avoid circular dependencies
    """
    # using a set to remove potential duplicates
    # If dependencies is empty list, recursion ends
    for p in dependencies:
        # Check for circular dependency
        if p in parent:
            print(f"Circular dependency: {p}<-{'<-'.join(reversed(parent))}")
        else:
            # Recurse
            print_package(level, p)
            print_level(packages[p], parent + [p], level + 1)


print_level(packages)

print()
print("*" * 80)
print()

import networkx as nx


G = nx.DiGraph()


def using_graphs():
    roots = set()
    for r, d in packages.items():
        roots.add(r)
        for i in d:
            G.add_edge(r, i)

    for s in roots:
        print(s)
        spacer = {s: 0}
        for prereq, target in nx.edge_dfs(G, s):
            spacer[target] = spacer[prereq] + 2
            print("{spacer}+-{t}".format(spacer=" " * spacer[prereq], t=target))
        print()


using_graphs()

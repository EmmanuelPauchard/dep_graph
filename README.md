# DepGraph, an example dependency graph analyzer

Given a description of items and their mutual dependency, DepGraph prints, for each item, the recursive list of its dependencies.

## Usage

## Design Notes

Dependency Graph is implemented using a simple recursion.

## Limitations

DepGraph currently can't handle versions specifier.

## Further work

The following could be improved in the current implementation:
  * Use Dynamic Programming to store already solved dependencies: this could improve speed when handling large amounts of items
  * Use an external Graph Analysis library, for instance [[https://networkx.org/][networkx]]: this would improve reuse and immediately provide additional functionality (plot dependency graph...)
  

## Developping
- Coding style: black
- Test Framework: pytest

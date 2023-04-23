#!/usr/bin/env ipython3

from typing import Union, List
import logging
from abc import ABC


# Type Alias for Packages definition
# Keys are packages names
# Values are package dependencies, as a list of other package name.
# If no dependencies, use an empty list
Packages = dict[str, Union[List[str], List]]


class Parser(ABC):
    """
    Main object to parse Dependency Graph input.
    """

    def __init__(self, data: str):
        """Interface for a Dependency Graph Parser

        :param data: the input data to be parsed.

        """
        self.data = data

    def parse() -> Packages:
        """Parse packages dependency structure.

        :return packages: The dependency network, a structure with packages and
        their dependencies

        """
        pass


import json


class JsonParser(Parser):
    """Parse Package dependencies from JSON text"""

    def parse(self) -> Packages:
        return json.loads(self.data)


class PackageVisitor(ABC):
    """Utility class to format output of an Analyser class"""

    def visit(self, level: int, package_name: str):
        """
        Called by the Analyzer for each visited package.

        :param level: The current depth in the analyze
        :param package_name: The visited package name

        """
        pass


class Analyzer:
    """
    Analyse a Dependency Graph
    """

    def __init__(self, packages: Packages, visitor: PackageVisitor):
        """Create a Dependency Graph Analyser.
        :param packages: The dependency graph structure to be analyzed
        :param visitor: Will be called during graph analysis to handle output.
        """
        self.packages = packages
        self.visitor = visitor

    def _analyze_level(
        self, dependencies: list[str], parent: list[str] = [], level: int = 0
    ):
        """Recursive function to traverse the packages dependencies. The
        function iterates on all dependencies and recurse until one of the two
        exit conditions is met:

          - package no longer has dependency
          - a circular dependency is detected

        The function calls the registered PackageVisitor for each found
        dependency.

        :note: relies on the fact that dependencies is always a list that must
        be empty if there are no dependencies

        :param dependencies: list of dependencies for the analyzed package
        :param parent: list of direct ancestors (to avoid circular dependencies)
        :param level: current level (depth) of the analysis

        """
        # FIXME: we could be using a set to remove potential duplicates
        # If dependencies list is empty, recursion ends
        for p in dependencies:
            # In case of circular dependency, recursion ends
            if p in parent:
                logging.warning(
                    f"Circular dependency: {p}<-{'<-'.join(reversed(parent))}"
                )
            else:
                # Visit
                self.visitor.visit(level, p)
                # Recurse
                self._analyze_level(self.packages[p], parent + [p], level + 1)

    def run(self):
        """Perform the dependency analysis for the current package structure"""

        self._analyze_level(self.packages)


class PackagePrinter(PackageVisitor):
    def visit(self, level, package_name):
        print("  " * level + "- " + package_name)

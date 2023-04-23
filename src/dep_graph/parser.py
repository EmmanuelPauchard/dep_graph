#!/usr/bin/env ipython3

from abc import ABC
import json

from analyzer import Packages


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


class JsonParser(Parser):
    """Parse Package dependencies from JSON text"""

    def parse(self) -> Packages:
        return json.loads(self.data)

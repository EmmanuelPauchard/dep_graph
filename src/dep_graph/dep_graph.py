#!/usr/bin/env ipython3

import argparse

from dep_graph.analyzer import Analyzer
from dep_graph.parser import JsonParser


def parse_arguments():
    parser = argparse.ArgumentParser(description="Simple Dependency Graph analyzer.")
    parser.add_argument(
        "input",
        nargs="?",
        default="-",
        type=argparse.FileType("r"),
        help="Input file containing package structure in JSON description. Use '-' for stdin (default).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    Analyzer(JsonParser(args.input.read()).parse()).run()

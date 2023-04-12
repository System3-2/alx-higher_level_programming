#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a utf8 text file to stdout."""
    with open(filename, endcoding="utf-8") as f:
        print(f.read(), end="")

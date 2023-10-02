"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        val = str(i)
        frequencies[val] = frequencies.get(val, 0) + 1
    return frequencies
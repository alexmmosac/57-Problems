#!/usr/bin/python3

def string_count(string):
    try:
        return len(string)
    except TypeError:
        return None

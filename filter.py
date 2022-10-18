#!/usr/bin/env python3

def filter_text(text):
        keys = []
        values = []
        for l in text.split("\n"):
                if l.startswith("#"):
                        (key, val) = map(str.strip, l[1:].split("="))
                        keys.append(key)
                        values.append(val)
        for k in keys:
                for v in values:
                        if k in v:
                                return False
        return True

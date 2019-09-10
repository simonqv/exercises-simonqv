#!/usr/bin/env python3
import sys
import struct


with open("shell.bin") as f:
    payload = f.read()

sys.stdout.write("header")
sys.stdout.write("\n")

sys.stdout.write("body")
sys.stdout.write("\n")


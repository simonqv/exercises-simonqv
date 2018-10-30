#!/usr/bin/python
import sys
import struct


payload = open("shell.bin").read()

sys.stdout.write("header")
sys.stdout.write("\n")

sys.stdout.write("body")
sys.stdout.write("\n")


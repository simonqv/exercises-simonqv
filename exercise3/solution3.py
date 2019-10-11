#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(v):
	sys.stdout.flush()
	sys.stdout.buffer.write(v.encode("ascii"))
	sys.stdout.flush()

def writeBytes(v):
	sys.stdout.flush()
	sys.stdout.buffer.write(v)
	sys.stdout.flush()

writeStr("user")


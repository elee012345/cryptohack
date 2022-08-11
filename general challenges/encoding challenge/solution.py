from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import long_to_bytes

r = remote('socket.cryptohack.org', 13377, level = 'debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:
    received = json_recv()
    type = received["type"]
    encoded = received["encoded"]

    if type == "base64":
        # take the encoded value, decode it from base 64, turn it back into a string from a binary string with decode()
        decoded = base64.b64decode(encoded).decode()

    elif type == "hex":
        # take the encoded value, turn it into binary aka un-hex it, and turn the binary string into a normal string with decode()
        decoded = bytes.fromhex(encoded).decode()

    elif type == "rot13":
        # rot 13 is a caeser shift by 13 lol
        # can encode or decode because 13 either way is the same thing
        decoded = codecs.encode(encoded, "rot13")

    elif type == "bigint":
        # take the hex number, turn it into a base 10 number, turn the base 10 number into byte string, turn it back into normal string
        decoded = long_to_bytes(int(encoded, 16)).decode()

    elif type == "utf-8":
        # you receive a list of ints for this
        decoded = ""
        for i in encoded:
            # un-unicode all of the characters
            decoded += chr(i)
        
    # recieve the flag
    else:
        break

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)


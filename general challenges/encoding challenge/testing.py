from pwn import * # pip install pwntools
import json
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes


type = "utf-8"
encoded = [100, 101, 115, 95, 114, 105, 100, 101, 115, 95, 115, 105, 109, 117, 108, 97, 116, 105, 111, 110, 115]


if type == "base64":
    decoded = base64.b64decode(encoded).decode()
elif type == "hex":
    decoded = bytes.fromhex(encoded).decode()
elif type == "rot13":
    decoded = codecs.encode(encoded, "rot13")
elif type == "bigint":
    decoded = long_to_bytes(int(encoded, 16)).decode()
elif type == "utf-8":
    decoded = ""
    for i in encoded:
        decoded += chr(i)

print(decoded)
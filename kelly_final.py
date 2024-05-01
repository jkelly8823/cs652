import os
import base64
from Crypto.Cipher import ARC4

strs = []
dec = []

file_path = input("Provide a file path:\n")

with open(file_path, 'rb') as file:
    data = file.read()
    for s in data:
        strs.append(s)

print("Bytes:")
print(strs)

userKey = input("Enter a base64 key: ").encode('utf-8')

for s in strs:
    tmpArc = ARC4.new(userKey)
    tmpStr = tmpArc.decrypt(base64.b64decode(s))
    dec.append(tmpStr)

print('Decoded Bytes:')
print(dec)

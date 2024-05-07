from base64 import b64decode
import math

string1 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
num = 664813035583918006462745898431981286737635929725

print(b64decode(string1))
byte_length = math.ceil(num.bit_length() / 8)
print(num.to_bytes(byte_length, "big"))
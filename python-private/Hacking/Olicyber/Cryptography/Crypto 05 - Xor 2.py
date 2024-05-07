def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

def decrypt(ciphertext):
    for key in range(256):  
        key = key.to_bytes(1, "big")
        msg = xor(ciphertext, key)
        if msg.isascii():
            print(msg.decode(), end='')

def main():
    ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
    ciphertext = bytes.fromhex(ciphertext)
    decrypt(ciphertext)

if __name__ == "__main__":
    main()
expected = [0x242, 0x238, 0x24c, 0xf8, 0x23d, 0x23d, 0x1fc, 0x21f, 0x26a, 0x102, 0x229, 0x215, 0xf3, 0x260, 0x1de, 0x260, 0xf3, 0x24c, 0x23d, 0x1de, 0x215, 0x107, 0x251, 0x107, 0x1de, 0x1f2, 0xf3, 0x201, 0x201, 0x102, 0x102, 0x1de, 0x111, 0x102, 0x120, 0xfd, 0x116, 0x107, 0x274]

password = []
for i in range(len(expected)):
    c = chr((expected[i] - 3) // 5)
    password.append(c)

print("The correct password is: " + ''.join(password))
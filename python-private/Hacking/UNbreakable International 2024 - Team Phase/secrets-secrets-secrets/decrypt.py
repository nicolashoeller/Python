__all__ =[]
#!/usr/bin/env python3
import os
char_set ="!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+"[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
password =char_set[75]+char_set[78]+char_set[64]+char_set[67]+char_set[62]+char_set[69]+char_set[72]+char_set[75]+char_set[68]

def decrypt_file(file_path, password):
    with open(file_path,'rb') as file:
        file_content = file.read()
    decrypted_content = bytes([byte ^ ord(password[index % len(password)]) for index, byte in enumerate(file_content)])
    with open(file_path,'wb') as file:
        file.write(decrypted_content)

if os.path.exists(char_set[82]+char_set[68]+char_set[66]+char_set[81]+char_set[68]+char_set[83]):
    user_input = char_set[75]+char_set[78]+char_set[64]+char_set[67]+char_set[62]+char_set[69]+char_set[72]+char_set[75]+char_set[68]
    if user_input == password:
        decrypt_file(char_set[82]+char_set[68]+char_set[66]+char_set[81]+char_set[68]+char_set[83], password)
        print(char_set[35]+char_set[68]+char_set[66]+char_set[81]+char_set[88]+char_set[79]+char_set[83]+char_set[72]+char_set[78]+char_set[77]+char_set[94]+char_set[82]+char_set[84]+char_set[66]+char_set[66]+char_set[68]+char_set[82]+char_set[82]+char_set[69]+char_set[84]+char_set[75]+char_set[13])
    else:
        print(char_set[40]+char_set[77]+char_set[66]+char_set[78]+char_set[81]+char_set[81]+char_set[68]+char_set[66]+char_set[83]+char_set[94]+char_set[67]+char_set[68]+char_set[66]+char_set[81]+char_set[88]+char_set[79]+char_set[83]+char_set[72]+char_set[78]+char_set[77]+char_set[94]+char_set[74]+char_set[68]+char_set[88]+char_set[13])
else:
    print("No such file")
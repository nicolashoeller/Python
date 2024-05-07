# Given string
encrypted_string = "2913644539381752683376904342495776245651598615591796790741725206197492919511780238846669609947545766526"

# Convert into ASCII
ascii_text = ""
for i in range(0, len(encrypted_string), 8):
    chunk = encrypted_string[i:i+8]
    ascii_char = chr(int(chunk))
    ascii_text += ascii_char

print(ascii_text)

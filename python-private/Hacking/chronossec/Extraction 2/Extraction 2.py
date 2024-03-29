import re

md5_pattern = re.compile(r'^[a-fA-F0-9]{32}$')

with open('/home/kali/Desktop/Programming/Python/python-private/Hacking/chronossec/file.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not md5_pattern.match(line):
            print(line)

count = 0

string = "Hier steht ein beliebiger Text."


print("Anzahl der 'e' im text:", string.count('e'))

print(string.split()[0].upper() + ' '.join(string.split()[1:]).replace('i', '1'))
eingabe = input("Geben Sie eine Zahl oder ein Wort ein: ")

if eingabe.isdigit():
    print("Die Eingabe ist eine Zahl.")
    ergebnis = int(eingabe) * 2
    print("Das Doppelte der Zahl ist:", ergebnis)
elif eingabe.isalpha():
    count = 0
    print("Die Eingabe ist ein Wort.")
    for buchstabe in eingabe:
        count += 1
    print("Das Wort hat", count, "Buchstaben.")
else:
    print("Die Eingabe ist weder eine Zahl noch ein Wort.")
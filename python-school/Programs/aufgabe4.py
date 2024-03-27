sonntag = False  # Setze auf True, wenn heute Sonntag ist
feiertag = False  # Setze auf True, wenn heute ein Feiertag ist

print("Welcher Tag ist heute?")

tag = input()
tag = tag.lower()

if tag == "sonntag":
    sonntag = True

print("Ist heute ein Feiertag? (ja/nein)")

feiertagInput = input()
feiertagInput = feiertagInput.lower()

if feiertagInput == "ja":
    feiertag = True

if sonntag:
    print("Das Geschäft ist heute geschlossen. Einen schönen Sonntag!")
elif feiertag:
    print("Das Geschäft ist heute geschlossen.")
else:
    print("Das Geschäft ist heute geöffnet.")

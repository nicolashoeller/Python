def tupel1():

    philipp = ("Philipp", "Heidenberger", 16,)

    number = int(input("Geben Sie Ihre telefonnummer ein: "))
    philipp_neu = philipp + (number,)
    print(philipp_neu)

def tupel2():
    
    philipp = ("Philipp", "Heidenberger", [16],)

    number = int(input("Geben Sie Ihre telefonnummer ein: "))
    philipp_neu = philipp + (number,)
    philipp_neu[2][0] += 1
    print(philipp_neu)

def main():
    tupel1()
    tupel2()

if __name__ == "__main__":
    main()
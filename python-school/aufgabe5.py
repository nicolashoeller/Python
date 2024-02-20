def summe(numbers):
    return sum(numbers)
    
def getNumbers():
    numbers = []
    while True:
        try:
            number = input("Geben Sie eine Zahl ein: ")
            if number == 'q':
                break
            number = int(number)
            numbers.append(number)
        except ValueError:
            print("Das war keine Zahl!")
    return numbers

def main():
    numbers = getNumbers()
    print(summe(numbers))

if __name__ == "__main__":
    main()
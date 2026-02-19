while True:
    num1 = input("Zadaj prve cislo (alebo 'q' pre koniec): ")
    
    if num1 == "q":
        print("Program sa ukoncuje.")
        break
    
    num2 = input("Zadaj druhe cislo: ")
    operation = input("Zadaj operaciu (+, -, *, /): ")

    num1 = int(num1)
    num2 = int(num2)

    if operation == "+":
        print("Vysledok je:", num1 + num2)

    elif operation == "-":
        print("Vysledok je:", num1 - num2)

    elif operation == "*":
        print("Vysledok je:", num1 * num2)

    elif operation == "/":
        if num2 != 0:
            print("Vysledok je:", num1 / num2)
        else:
            print("Delenie nulou nie je povolene!")

    else:
        print("Neplatna operacia!")
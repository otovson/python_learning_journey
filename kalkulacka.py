num1 = int(input("Zadaj prve cislo: "))
num2 = int(input("Zadaj druhe cislo: "))

operation = input("Zadaj operaciu (+, -, *, /): ")

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
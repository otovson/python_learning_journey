name = input("Zadaj svoje meno: ")
year_of_birth = input("Zadaj rok narodenia: ")

year_of_birth = int(year_of_birth)

current_year = 2025
age = current_year - year_of_birth

print("Ahoj", name)
print("Mas", age, "rokov")
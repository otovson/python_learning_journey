name = input("Your name: ")
age = int(input("Your age: "))



if age < 13:
    print ("Hi", name, ", you are a child")
elif age >= 13:
    print ("Hi", name, ", you are a teenager")
elif age >= 18:
    print ("Hi", name, ", you are an adult")


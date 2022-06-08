nameInput = input("What is your name? ")
ageInput = input("What is your age? ")\

age = int(ageInput)

if age >= 18:
    print("Your name is %s and your age is %d" % (nameInput, age))
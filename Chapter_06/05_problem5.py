l = ["Harry", "Ron", "Hermione", "Draco", "Neville"]

name = input("Enter your name: ")

if ( name in l):
    print("Welcome to the Hogwarts School of Witchcraft and Wizardry, " + name + "!")
else:
    print("You are not a student of the Hogwarts School of Witchcraft and Wizardry, " + name + ".")
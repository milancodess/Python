class Employee:
    language ="Py" # This is a class attribute
    salary = 120000


milan = Employee()
milan.name = "Milan" # This is an instance attribuet
print(milan.name, milan.language, milan.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object attribute and salary and language are object attributes as they directly belong to the class
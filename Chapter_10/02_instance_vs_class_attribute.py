class Employee:
    language ="Python" # This is a class attribute
    salary = 120000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good morning")



milan = Employee()
# milan.language = "Javascript" # This is an instance attribuet
# print(milan.language, milan.salary)
milan.greet()
milan.getInfo()
# Employee.getInfo(milan)
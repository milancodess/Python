class Employee:
    language ="Python" # This is a class attribute
    salary = 120000

    def __init__(self, name, salary, language): # Dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(): # It is a static method, it doesn't need any object attribute
        print("Good morning")


milan = Employee("Milan", 130000, "JavaScript")
# milan.name = "Milan"
print(milan.name, milan.salary, milan.language)

# rohan = Employee()
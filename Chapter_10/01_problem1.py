class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
        

p = Programmer("Milan", 120000, 2063)
print(p.name, p.salary, p.pin, p.company)

r = Programmer("Rohan", 120000, 2064)
print(r.name, r.salary, r.pin, r.company)
class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because the instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is set
print(Demo.a) # Prints the class attribute
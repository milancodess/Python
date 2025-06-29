# a = 12
# b = 45
# c = 56

# average = (a + b + c) / 3
# print(average)

# Function definition
def avg():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    average = (a + b + c) / 3
    print(f"The average of {a}, {b}, and {c} is {average}")

# Function call
avg()
print("Thank you")
avg()
def inchToCms(inch):
    return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"{n} inches is {inchToCms(n)} cm")
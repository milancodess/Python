#5! = 1 * 2 * 3 * 4 * 5 = 120

n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):
    product = product * i

print(f"The factorial of {n} is {product}")
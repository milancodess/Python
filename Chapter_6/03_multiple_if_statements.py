a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("You have entered an even number.")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are above the age of consent.")
    print("Good to go!")

elif(a<0):
    print("Invalid age entering an invalid negative age.")

elif(a==0):
    print("You are entering 0, which is not a valid age.")

else:
    print("You are below the age of consent.")
# End of If statement no: 2

print("End of program.")
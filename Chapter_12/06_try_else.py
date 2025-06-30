try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I'm inside else")
    # Else works when try is succesfull
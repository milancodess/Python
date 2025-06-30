a = 89 # Global Variable


def fun():
    # global a # This will assign global variable on this func
    a = 3 # Local Variable
    print(a)

fun()
print(a)
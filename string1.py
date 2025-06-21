name = "Milan"
print(name)

nameshort = name[0:3]
print(nameshort)  # 3characters from index 0 to 2
nameshort = name[0:4]
print(nameshort)  # 4characters from index 0 to 3

print(name[-4:-1])  # 4characters from index -4 to -2
print(name[1:4])
print(name[1:])  # from index 1 to the end
print(name[:4])  # from the start to index 3
print(name[1:5]) # from index 1 to the end
print(name[1:5:2])  # from index 1 to the end, step of 2
print(name[::2])  # from the start to the end, step of 2
print(name[::-1])  # reverse the string
print(name[1:5:-2])  # this will not return anything as the step is negative and the start index is less than the end index
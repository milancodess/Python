a = (1, 45, 45, 567, False, "Hello", 3.14)
print(a)

no = a.count(45)  # Counting occurrences of 1 in the tuple
print(no)  # Display the count of 1

i = a.index(45)  # Finding the index of the first occurrence of 45
print(i)  # Display the index of 45

print(len(a))  # Display the length of the tuple 

my_tuple = (1, 2, 3)
repeated = my_tuple * 3 # Repeating the tuple 3 times
print(my_tuple)  # Display the original tuple
print(repeated)  # Display the tuple repeated 3 times
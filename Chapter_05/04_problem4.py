s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(s)  # Display the set after adding elements
print(len(s))  # Display the number of elements in the set
# Output:  
# {20, '20'}
# 2
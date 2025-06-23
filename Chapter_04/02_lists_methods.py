friends = ["Apple", "Banana", 23, 1, 3.14, True, None ]
print(friends)

friends.append("Orange")  # Adding a new element to the end of the list
print(friends)  # Display the updated list

numbers = [1, 2, 3, 4, 5, 11, 62, 89, 12]
# numbers.sort()  # Sorting the list in ascending order
# print(numbers)  # Display the sorted list

# numbers.reverse()  # Reversing the order of the list
# print(numbers)  # Display the reversed list

# numbers.insert(3, 33333)
# print(numbers)  # Display the list after inserting an element at index 3

# numbers.pop(3)  # Removing the element at index 3
# print(numbers)  # Display the list after popping an element

value =  numbers.pop(3)
print(value)  # Display the value that was popped
print(numbers)  # Display the list after popping an element

numbers.remove(89)  # Removing the first occurrence of 89
print(numbers)  # Display the list after removing an element
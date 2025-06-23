marks = {
    "Milan": 100,
    "Samir": 56,  
    "Amar": 23,
     0: "Zero",
}

# print(marks.items()) 
# print(marks.keys())  
# print(marks.values()) 
# marks.update({"Milan": 99, "Gaurab": 20})  # Update the value for the key "Milan"
# print(marks)

# print(marks.get("Milan2"))  # Prints None since "Milan2" is not a key in the dictionary
# print(marks["Milan2"])  # Return an error since "Milan2" is not a key in the dictionary
# print(marks.get("Gaurab", "Key not found"))  # Using get()
print(marks.pop("Milan"))  # Removes and returns the value associated with the key "Milan"
print(marks)
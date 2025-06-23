d = {}

name = input("Enter friends name: ")
lang = input("Enter language: ")
d.update({name: lang})  # Update the dictionary with the name and language

name = input("Enter friends name: ")
lang = input("Enter language: ")
d.update({name: lang})  # Update the dictionary with the name and language

name = input("Enter friends name: ")
lang = input("Enter language: ")
d.update({name: lang})  # Update the dictionary with the name and language

name = input("Enter friends name: ")
lang = input("Enter language: ")
d.update({name: lang})  # Update the dictionary with the name and language

print(d)  # Display the dictionary after adding all friends and their languages

# Output:
# Enter friends name: Milan
# Enter language: JS
# Enter friends name: Samir
# Enter language: Python
# Enter friends name: Amar
# Enter language: Kotlin
# Enter friends name: Gaurab
# Enter language: C
# {'Milan': 'JS', 'Samir': 'Python', 'Amar': 'Kotlin', 'Gaurab': 'C'}

# Output in case of duplicate names:
# Enter friends name: Milan
# Enter language: C
# Enter friends name: Milan
# Enter language: JS
# Enter friends name: Samir
# Enter language: Python
# Enter friends name: Amar
# Enter language: Java
# {'Milan': 'JS', 'Samir': 'Python', 'Amar': 'Java'}

# Output in case of duplicate languages:
# Enter friends name: Milan
# Enter language: C
# Enter friends name: Samir
# Enter language: C
# Enter friends name: Amar
# Enter language: Java
# Enter friends name: Gaurab
# Enter language: Python
# {'Milan': 'C', 'Samir': 'C', 'Amar': 'Java', 'Gaurab': 'Python'}

# Note: The dictionary will not allow duplicate keys, so if a name is entered again, it will update the existing entry.
# The values can be the same for different keys, but keys must be unique.
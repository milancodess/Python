name = "Milan"

print(len(name))  # Length of the string
print(name[0])  # First character of the string
print(name.capitalize())  # Capitalize the first letter of the string
print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase
print(name.endswith("an"))  # Check if the string ends with "an"
print(name.startswith("Mi"))  # Check if the string starts with "Mi"
print(name.find("la"))  # Find the index of "la" in the string
print(name.find("md"))  # Find the index of "md" in the string
print(name.replace("la", "lo"))  # Replace "la" with "lo"
print(name.split("l"))  # Split the string by "l"
print(name.isalpha())  # Check if all characters are alphabetic
name = "Milan123"
print(name.isalnum())  # Check if all characters are alphanumeric
print(name.isdigit())  # Check if all characters are digits
print(name.isnumeric())  # Check if all characters are numeric
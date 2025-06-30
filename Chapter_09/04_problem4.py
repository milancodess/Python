word = "Donkey"

with open("d.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")
with open("d.txt", "w") as f:
    f.write(contentNew)

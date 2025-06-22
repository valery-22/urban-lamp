text = "Python is fun!"
lowercase_count = 0

for char in text:
    if char.islower():
        lowercase_count += 1

print(lowercase_count)
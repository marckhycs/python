string = input("Enter here: ")
empty = []

for i in string:
    if i.isupper():
        empty.append(string.index(i))
print(empty)
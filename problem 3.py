s = input("Enter a string: ")

count = 0
for char in s:
    if char.isdigit():
        count += 1

print("Total digits are:", count)

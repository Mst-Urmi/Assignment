def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

s = input("Enter a string: ")
result = count_vowels(s)

print("Number of vowels:", result)

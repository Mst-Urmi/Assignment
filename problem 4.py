def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

s = input("Enter a string: ")
result = is_palindrome(s)

print(result)

def palindrome(s):
    if s == s[::-1]:
        print(True)
    else:
        print(False)
s = input("Enter a string")
palindrome(s)


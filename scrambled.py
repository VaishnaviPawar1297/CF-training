def scrambled(str1, str2):
    if sorted(str1) == sorted(str2):
        print("The given strings are scrambled")
    else:
        print("The given strings are not scramblede")

str1 = "python"
str2 = "ythpon"

scrambled(str1, str2)
    
def decimalTobinary(n):
    if n ==0 or n == 1:
        print(n, end = " ")
        return
    decimalTobinary(int(n/2))
    print(n%2, end = " ")

n = int(input("Enter decimal number : "))
print("The binary converted number is : ")
decimalTobinary(n)
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2
    

print("select the operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice (1, 2, 3, 4)")

    if choice in('1', '2', '3', '4'):
        
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))

        if choice == '1':
            print(num1, '+', num2, '=', add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, '=', sub(num1, num2))
        elif choice == '3':
            print(num1, '*', num2, '=', mul(num1, num2))
        elif choice == '4':
            print(num1, '/', num2, '=', div(num1, num2))
        
    else:
        print("Enter valid choice")


nterms = int(input("How many terms? "))

first = 0
second = 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")

else:
   print("Fibonacci sequence:")
   
   while count < nterms:
       print(first)
       nth = first + second
       first = second
       second = nth
       count = count + 1
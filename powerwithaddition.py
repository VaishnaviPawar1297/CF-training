n = 3
m = 4
p = n
for i in range(1,m):
    print("i", i)
    temp = p
    print("temp", temp)
    for j in range(1,n):
        print("j", j)
        p = p + temp
        print("p", p)
print('value of ' + str(n) + ' power ' + str(m) + ' is ' + str(p))
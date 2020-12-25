def search(list1, key):
    list2 = []
    flag  = False
    for i in range(len(list1)):
        if key == list1[i]:
            flag = True
            list2.append(i)
    if flag == True:
        print("Element is found at index  :")
        for i in list2:
            print(i)
    else:
        print("key is not found")

list1 = [34,23,5,6,7,1,23,6,8]
key = int(input("Enter the key element : "))
search(list1, key)
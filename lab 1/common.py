
def common(a,b):
    c =[]
    print("List 1 ",a)
    print("List 2 ",b)
    for i in a:
        if i in b:
            if i in c:
                continue
            c.append(i)
    print("The common elements in two list ",c)

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]      
common(list1,list2)

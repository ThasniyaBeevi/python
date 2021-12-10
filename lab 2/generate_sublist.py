
def sublist(lis):
    print("\n",lis)
    all_list = []
    for i in range(len(lis) + 1):
        for j in range(i):
            all_list.append(lis[j: i])
    print("All sublist : ",all_list)
list1 = [1,2,3,4,5]
list2 = ["a","b",2]
sublist(list1)
sublist(list2)
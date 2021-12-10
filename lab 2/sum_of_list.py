

def sum(lis):
	print("\n",lis)
	total = 0

	for i in range(0, len(lis)):
		total = total + lis[i]


	print("Sum of all items in list: ", total)

list1 = [1,2,3,4,5]
sum(list1)
list2 = [5,7,3,6,9]
sum(list2)
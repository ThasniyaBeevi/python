

def sum_of_list(lis):
	total = 0
	for i in range(0, len(lis)):
		total = total + lis[i]


	print("Sum of all items in list: ", total)

list1 = [1,2,3,4,5]
sum_of_list(list1)
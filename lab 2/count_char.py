

str1 = input("Enter a string : ")
count = dict()
for i in str1:
    if i in count:
        count[i] = count[i] + 1
    else:
        count[i] = 1
print(count)


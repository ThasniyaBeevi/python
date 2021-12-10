num = int(input("Enter a number : "))

count = 0
divisors =[]
print("divisors of ",num)
for i in range(1,num+1):
    if num % i == 0:
        count += 1
        divisors.append(i)
print(divisors)


    
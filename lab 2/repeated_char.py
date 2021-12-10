stringg = input("Enter a string : ")
print("Repeated Characters and their count")
for i in range(0, len(stringg)):  
    count = 1;  
    for j in range(i+1, len(stringg)):  
        if(stringg[i] == stringg[j] and stringg[i] != ' '):  
            count = count + 1;  
            stringg = stringg[:j] + '0' + stringg[j+1:];  
    
    if(count > 1 and stringg[i] != '0'):  
        print(stringg[i]," - ",count)
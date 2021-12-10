dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50,6:60}
dic4 = {}
print(dic1,'\n',dic2,'\n',dic3)
for dic in (dic1,dic2,dic3):
    dic4.update(dic)
print("Concatenation of 3 dictionary : ",dic4)
with open("sample.txt",'r') as file:
    Count = 0
    Content = file.read()
    List_content = Content.split("\n")
  
for i in List_content:
    if i:
        Count += 1
          
print("This is the number of lines in the file")
print(Count)

with open("sample.txt","a") as f:
    f.write("\nWe have added more contents to the file.")
with open("sample.txt","r") as f:
    
    print(f.read())
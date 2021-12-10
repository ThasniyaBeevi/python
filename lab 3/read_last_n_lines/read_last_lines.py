
def LastNlines(file, n):
    
    with open(file) as file:
     
        for line in (file.readlines() [-n:]):
            print(line, end ='')
LastNlines("sample.txt",4)


def firstNlines(file, n):
    
    with open(file) as file:
     
        for line in (file.readlines() [0:n]):
            print(line)
firstNlines("sample.txt",2)
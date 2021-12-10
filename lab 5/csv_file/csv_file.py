import csv

with open('sample.csv', 'r') as file:
    reader = csv.reader(file)


    i = 0

    for row in reader:
        if i == 2:
            print("This is the 3rd row of csv file:")
            print(row,"\n")
            break

        i += 1


with open("sample.csv") as f:
    reader = csv.reader(f)
    print("second column of csv file:")
    for row in reader:
        print(row[1])

with open('sample.csv', 'r') as file:
    reader = csv.reader(file)
    print("\nFirst 3 line of csv file :")

    i = 0

    for row in reader:
        if i>2:
            break
        print(row)
            

        i += 1
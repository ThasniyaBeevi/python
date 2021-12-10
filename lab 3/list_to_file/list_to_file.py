color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('sample.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('sample.txt')
print(content.read())

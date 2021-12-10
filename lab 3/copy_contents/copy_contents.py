
with open('sample.txt','r') as firstfile, open('second.txt','w') as secondfile:
	content = open('sample.txt')
	print("first file\n",content.read())
	for line in firstfile:

		secondfile.write(line)
content = open('second.txt')
print("second file\n",content.read())
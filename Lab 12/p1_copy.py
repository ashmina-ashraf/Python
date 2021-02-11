try:
	f1 = open('file1.txt')
	f2 = open('file2.txt','w')

	line = f1.readline()
	while line:
		f2.write(line+'\n')
		line = f1.readline()

except IOError as io:
	print(io)

finally:
	if f1: f1.close()
	if f2:f2.close()
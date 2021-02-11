try:
	f1 = open('file1.txt','a')
	line = input("Enter text:\t")
	while line:
		f1.write(line+'\n')
		line = input("Enter text:\t")

except IOError as io:
	print(io)

finally:
	if f1: 
		f1.close()

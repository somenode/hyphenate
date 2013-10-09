fin = open('/path/to/your/textfile')
fout = open('path/where/you_want/your_output', 'w')
for line in fin: #runs through each line
	word = line.strip() 
    	newline = word[0:2] + '-' + word[2:] + '\n' #this example inserts a hyphen after position 1 
    	fout.write(newline)

fin.close()
fout.close()
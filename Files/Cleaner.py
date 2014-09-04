lines = ''
with open('data.txt', 'r') as filein:
	for line in filein:
		lines = lines + line
newLines = lines.split('[')
with open('cleaned.txt', 'w') as fileout:
	for line in newLines:
		fileout.write('[' + line + '\n')

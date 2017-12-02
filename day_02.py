f= open("input_02.txt")
sheet= f.readlines()
f.close()

numSheet= []
checksum= 0
for line in sheet:
	numbers= sorted(map(int, line.strip().split("\t")), reverse= True)
	numSheet.append(numbers)
	nMin= min(numbers)
	nMax= max(numbers)
	checksum+= nMax - nMin
	
print "Part 1: ", checksum

divs= 0
for line in numSheet:
	for i in range(len(line)):
		for j in range(i+1, len(line)):
			if line[i]%line[j] == 0:
				divs+= line[i]/line[j]

print "Part 2: ", divs

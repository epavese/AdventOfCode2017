fIn= open("input_08.txt")
inStr= fIn.readline().strip()
fIn.close()

i= 0
score= 0
totalScore= 0
totalGarbage= 0

newInStr= ""
while i < len(inStr):
	if inStr[i] == '!':
		i+= 2
	else:
		newInStr+= inStr[i]
		i+= 1

i= 0
inStr= newInStr
while i < len(inStr):
	if inStr[i] == '{':
		score+= 1
		i+= 1
	elif inStr[i] == '}':
		totalScore+= score
		score-= 1
		i+= 1
	elif inStr[i] == '<':
		nextI= inStr.find('>', i+1) + 1 
		totalGarbage+= nextI - i - 2 
		i= nextI
	else:
		i+= 1

print "Part 1:", totalScore
print "Part 2:", totalGarbage

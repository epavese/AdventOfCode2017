fIn= open("input_19.txt")
labyrinth= map(lambda x: list(x[:-1]), fIn.readlines())
fIn.close()

def chooseDirection(labyrinth, curDir, i, j):
	curPos= labyrinth[i][j]
	if curPos == '|' or curPos == '-' or curPos.isalpha():
		return curDir
	assert(curPos == '+')
	if curDir == "S" or curDir == "N":
		if j > 0 and labyrinth[i][j-1] != ' ':
			curDir= "W"
		else:
			curDir= "E"
	elif curDir == "E" or curDir == "W":
		if i > 0 and labyrinth[i-1][j] != ' ':
			curDir= "N"
		else:
			curDir= "S"	
	else:
		raise Error("Invalid direction " + curDir)
	return curDir

# enter the path
path= ""
i= 0
j= labyrinth[i].index('|')
i+= 1
height= len(labyrinth)
width= len(labyrinth[0])
direction= "S"
curPos= labyrinth[i][j]
totalSteps= 1

while curPos != ' ':
	curPos= labyrinth[i][j]
	if curPos.isalpha():
		path+= curPos
	direction= chooseDirection(labyrinth, direction, i, j)
	if direction == "S":
		i+= 1
	elif direction == "N":
		i-=1
	elif direction == "E":
		j+= 1
	elif direction == "W":
		j-= 1
	else:
		raise Error("Invalid direction " + direction)
	if i < 0 or j < 0:
		break
	totalSteps+= 1
	curPos= labyrinth[i][j]

print "Part 1:", path
print "Part 2:", totalSteps

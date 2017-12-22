def updatePos(pos, direction):
	if direction == "U":
		return (pos[0]-1,pos[1])
	elif direction == "R":
		return (pos[0],pos[1]+1)
	elif direction == "D":
		return (pos[0]+1,pos[1])
	elif direction == "L":
		return (pos[0],pos[1]-1)

def right(direction):
	if direction == "U":
		return "R"
	elif direction == "R":
		return "D"
	elif direction == "D":
		return "L"
	elif direction == "L":
		return "U"

def left(direction):
	if direction == "U":
		return "L"
	elif direction == "R":
		return "U"
	elif direction == "D":
		return "R"
	elif direction == "L":
		return "D"

fIn= open("input_22.txt")
grid= map(lambda x: x.strip(), fIn.readlines())
fIn.close()

infected= set()
upLim= len(grid)/2
downLim= -upLim
row= 0
for i in range(downLim, upLim+1):
	col= 0
	for j in range(downLim, upLim+1):
		if grid[row][col] == '#':
			infected.add((i,j))
		col+= 1
	row+= 1

pos= (0,0)
looking= "U"

moves= 0
infections= 0
while True:
	if pos in infected:
		looking= right(looking)
		infected.remove(pos)
	else:
		looking= left(looking)
		infected.add(pos)
		infections+= 1
	pos= updatePos(pos, looking)
	moves+= 1
	if moves == 10000:
		break

print "Part 1:", infections

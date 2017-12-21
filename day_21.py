def initGrid(size):
	row= list('*'*size)
	return list(row[:] for i in range(size))

def getSlice(grid, size, i, j):
	startRow= i*size
	startCol= j*size
	aSlice= []
	for k in range(size):
		aSlice.append(grid[startRow][startCol:startCol+size])
		startRow+= 1
	return aSlice

def putSlice(grid, theSlice, i, j):
	row= 0
	for posI in range(i*len(theSlice), i*len(theSlice)+len(theSlice)):
		col= 0
		for posJ in range(j*len(theSlice), j*len(theSlice)+len(theSlice)):
			grid[posI][posJ]= theSlice[row][col]
			col+= 1
		row+= 1

def flipH(grid):
	res= map(lambda x: x[:], grid)
	for line in res:
		line.reverse()
	return res

def flipV(grid):
	res= map(lambda x: x[:], grid)
	res.reverse()
	return res

def rotate(grid):
	size= len(grid)
	res= map(lambda x: x[:], grid)

	for j in range(size):
		for i in range(size):
			res[i][j]= grid[j][i]

	return flipH(res)

def printGrid(grid):
	for row in grid:
		print "".join(row)

def getEnhancement(theSlice, rulesMap):
	variants= [theSlice, rotate(theSlice), rotate(rotate(theSlice)), rotate(rotate(rotate(theSlice)))]
	flips= map(lambda x: flipV(x), variants) + map(lambda x: flipH(x), variants)
	variants+= flips
	res= None
	for grid in variants:
		res= rulesMap.get(str(grid), None)
		if res is not None:
			break
	return res

fIn= open("input_21.txt")
rules= map(lambda x: x.strip().split(" => "), fIn.readlines())
fIn.close()

rulesMap= {}
for rule in rules:
	pre= map(list, rule[0].strip().split("/"))
	pos= map(list, rule[1].strip().split("/"))
	rulesMap[str(pre)]= pos

grid= [['.','#','.'],['.','.','#'],['#','#','#']]

iters= 0
while True:
	failed= False
	newGrid= []
	size= 0
	if len(grid) % 2 == 0:
		newGrid= initGrid(len(grid)/2*3)
		size= 2
	else:
		newGrid= initGrid(len(grid)/3*4)
		size= 3

	i= 0
	while i < len(grid)/size:
		j= 0
		while j < len(grid)/size:
			theSlice= getSlice(grid, size, i, j)
			enh= getEnhancement(theSlice, rulesMap)
			if enh is None:
				failed= True
				break
			else:
				putSlice(newGrid, enh, i, j)
			j+= 1
		if failed:
			break
		i+= 1
	
	if failed:
		break
	grid= newGrid
	iters+= 1

	print iters
	if iters == 5:
		print "Part 1:", sum(map(lambda z: reduce(lambda x, y: x + 1 if y == '#' else x, z, 0), grid))
	if iters == 18:
		print "Part 2:", sum(map(lambda z: reduce(lambda x, y: x + 1 if y == '#' else x, z, 0), grid))
		break

print "Reached limit (18) or failed enhancement at", iters, "iterations"

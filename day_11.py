fIn= open("input_11.txt")
path= fIn.readline().strip()
fIn.close()

path= path.split(",")
curX= 0.0
curY= 0.0

maxDist= 0.0
for step in path:
	if step == "s":
		curY-= 1
	elif step == "sw":
		curX-= 0.5
		curY-= 0.5
	elif step == "nw":
		curX-= 0.5
		curY+= 0.5
	elif step == "n":
		curY+= 1
	elif step == "ne":
		curX+= 0.5
		curY+= 0.5
	elif step == "se":
		curX+= 0.5
		curY-= 0.5
	else:
		assert(False)
	if abs(curX)+abs(curY) > maxDist:
		maxDist= abs(curX)+abs(curY)

print "Part 1:", abs(curX)+abs(curY)
print "Part 2:", maxDist

def gridSpiral():
	ring= 1
	while True:
		for i in range(-ring+1, ring+1):
			yield (ring, i)
		
		for i in reversed(range(-ring, ring)):
			yield (i, ring)
		
		for i in reversed(range(-ring, ring)):
			yield (-ring, i)

		for i in range(-ring+1, ring+1):
			yield(i, -ring)
		ring+= 1

inValue= 265149

# Assume square 1 is located at (0,0) at ring 0
# Each "ring" i>0 allocates 8*i squares, located in rows -i, +i, and columns -i and +i

ring= 0
lastSq= 1
sqPerRing=0 

# Likely easier with closed geometric series formula, but hey it works
while lastSq < inValue:
	ring+= 1
	sqPerRing+= 8
	lastSq+= sqPerRing

# find exact spot in ring
# ring i goes counterclockwise
# - from (+i,-(i-1)) to (+i,+i) (2i elems)
# - from (+i-1,+i) to (-i,+i) (2i elems)
# - from (-i,+i-1) to (-i,-i) (2i elems)
# - from (-i+1,-i) to (+i,-i) (2i elems)
sq= lastSq-sqPerRing
side= 0 # 0 East, 1 North, 2 West, 3 South
while sq+2*ring < inValue:
	sq+= 2*ring
	side+= 1

offset= inValue-sq-1
pos= (0,0)
if side==0:
	pos= (ring,-i+1+offset)
if side==1:
	pos= (ring-1-offset, ring)
if side==2:
	pos= (-ring,ring-1-offset)
if side==3:
	pos= (-ring+1+offset,-ring)

print "Part 1: ", abs(pos[0])+abs(pos[1])

# For Part 2 just generate it...
gridValues= {}
gridValues[(0,0)]= 1
it= gridSpiral()

while True:
	newPos= it.next()
	value= gridValues.get((newPos[0]-1,newPos[1]+1), 0) + gridValues.get((newPos[0],newPos[1]+1), 0) + gridValues.get((newPos[0]+1,newPos[1]+1), 0) + gridValues.get((newPos[0]-1,newPos[1]), 0) + gridValues.get((newPos[0]+1,newPos[1]), 0) + gridValues.get((newPos[0]-1,newPos[1]-1), 0) + gridValues.get((newPos[0],newPos[1]-1), 0) + gridValues.get((newPos[0]+1,newPos[1]-1), 0)
	gridValues[newPos]= value

	if value > inValue:
		print "Part 2: ", value
		break


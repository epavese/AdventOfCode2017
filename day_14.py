#!/usr/local/bin/python

def chewUpSection(cells, toChewUp):
	while len(toChewUp) > 0:
		chew= toChewUp.pop()
		neighbors= cells.intersection(set([(chew[0], chew[1]-1), (chew[0], chew[1]+1), (chew[0]-1,chew[1]), (chew[0]+1, chew[1])]))
		cells.difference_update(neighbors)
		toChewUp= toChewUp.union(neighbors)
	return cells
	
def calculateHash(inputStr):
	skipLen= 0
	cur= 0
	numbers= range(256)
	stdSuffix= [17, 31, 73, 47, 23]
	lengths= map(ord, list(inputStr)) + stdSuffix

	for i in range(64):
		(numbers, cur, skipLen)= executeRound(numbers, lengths, cur, skipLen)

	denseHash= []
	for i in range(16):
		denseHash.append(reduce(lambda x,y: x^y, numbers[16*i:16*(i+1)], 0))

	knotHash= ""
	for num in denseHash:
		if len(hex(num)) != 4:
			knotHash+= "0"
		knotHash+= str(hex(num))[2:]

	assert(len(knotHash)) == 32
	return knotHash

def executeRound(numbers, lengths, cur, skipLen):
	for l in lengths:
		if cur + l <= len(numbers):
			numbers= numbers[:cur] + list(reversed(numbers[cur:cur+l])) + numbers[cur+l:]
		else:	
			l2= (cur + l)%len(numbers)
			revList= list(reversed(numbers[cur:] + numbers[:l2]))
			numbers= revList[-l2:] + numbers[l2:cur] + revList[:len(numbers)-cur]

		cur= (cur + l + skipLen)%len(numbers)
		skipLen+= 1

		assert(len(numbers) == 256)
	return (numbers, cur, skipLen)



numbers= range(256)
inStr= "jxqlasbh"

gridHashes= []
for i in range(128):
	gridHashes.append(calculateHash(inStr + "-" + str(i)))

# So small I just rather hardcode it
bitsPerHex= {'0': 0, '1': 1, '2': 1, '3': 2, '4': 1, '5': 2, '6': 2, '7': 3, '8': 1, '9': 2, 'a': 2, 'b': 3, 'c': 2, 'd': 3, 'e': 3, 'f': 4}
gridHashesBits= map(lambda x: map(lambda y: bitsPerHex[y], list(x)), gridHashes)
# All this lambda'ing would be easier with a functional language...Maybe I'll rewrite everything in F# for fun?

occupied= 0
for hsh in gridHashesBits:
	occupied+= sum(hsh)

print "Part 1:", occupied

# Obviously that wouldn't fly for part 2...
translatedHex= {'0': "0000", '1': "0001", '2': "0010", '3': "0011", '4': "0100", '5': "0101", '6': "0110", '7': "0111", '8': "1000", '9': "1001", 'a': "1010", 'b': "1011", 'c': "1100", 'd': "1101", 'e': "1110", 'f': "1111"}
gridHashesBits= map(lambda z: "".join(z), map(lambda x: map(lambda y: translatedHex[y], list(x)), gridHashes))

# Some weird list comprehension would work here too. Too lazy to get it right now
occupiedCells= set()
for i in range(128):
	for j in range(128):
		if gridHashesBits[i][j] == '1':
			occupiedCells.add((i,j))

assert len(occupiedCells) == occupied

sections= 0
while len(occupiedCells) > 0:
	sections+= 1
	nextSection= occupiedCells.pop()
	occupiedCells= chewUpSection(occupiedCells, set([nextSection]))

print "Part 2:", sections


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

lengths= [34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167]
numbers= range(256)
skipLen= 0
cur= 0

(numbers, cur, skipLen)= executeRound(numbers, lengths, cur, skipLen)
print "Part 1:", numbers[0]*numbers[1]

fIn= open("input_10.txt")
strNumbers= fIn.readline().strip()
fIn.close()
stdSuffix= [17, 31, 73, 47, 23]

numbers= range(256)
lengths= map(ord, strNumbers) + stdSuffix
skipLen= 0
cur= 0

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
print "Part 2:", knotHash

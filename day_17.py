buf= [0]
cur= 0
step= 355
maxSteps= 2018

for i in range(1,maxSteps):
	cur=(cur+step)%len(buf)
	buf= buf[:cur+1] + [i] + buf[cur+1:]
	cur= (cur+1)%len(buf)

print "Part 1:", buf[(cur+1)%len(buf)]
curNext0= buf[1]

maxSteps= 50000000
bufLen= 1
next0= -1
cur= 0
for i in range(maxSteps):
	cur= (cur+step)%bufLen
	if cur == 0:
		next0= i+1
	cur+= 1
	bufLen+= 1

print "Part 2:", next0

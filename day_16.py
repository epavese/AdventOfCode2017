#!/usr/local/bin/python
import sys
def swap(prgs, pos1, pos2):
	swp= prgs[pos1]
	prgs[pos1]= prgs[pos2]
	prgs[pos2]= swp
	return prgs

def dance(prgs, moves):
	for m in moves:
		if m[0] == 's':
			sz= int(m[1:])
			prgs= prgs[-sz:]+prgs[:-sz]
		elif m[0] == 'x':
			pos= map(int, m[1:].split("/"))
			prgs= swap(prgs, pos[0], pos[1])
		elif m[0] == 'p':
			names= m[1:].split("/")
			prgs= swap(prgs, prgs.index(names[0]), prgs.index(names[1]))
		else:
			print "Error", m
			sys.exit(0)
	return prgs

fIn= open("input_16.txt")
moves= fIn.readline().strip().split(",")
fIn.close()

prgs= list("abcdefghijklmnop")
seen= {"".join(prgs): 0}
seenNdx= {0: "".join(prgs)}
prgs= dance(prgs, moves)
print "Part 1:", "".join(prgs)

seen= {"".join(prgs): 1}
seenNdx= {1: "".join(prgs)}
i= 2
firstSeen= 0
now= 0

iters= 1000000000-2
# I'm guessing it cycles...
cycled= False
while i < iters:
	prgs= dance(prgs, moves)
	if "".join(prgs) in seen.keys():
		firstSeen= seen["".join(prgs)]
		now= i
		cycled= True
		break
	else:
		seen["".join(prgs)]= i
		seenNdx[i]= "".join(prgs)
		i+= 1

if (cycled):
	iters= 1000000000
	print "Part 2:", seenNdx[firstSeen+(iters-firstSeen)%(now-firstSeen)]
else:
	print "Part 2:", progs

import re

inFile= open("input_07.txt")
programs= map(lambda x: x.strip(), inFile.readlines())
inFile.close()

programInfo= {}
programs= map(lambda x: re.match("([a-z]+) (\(\d+\))(.*)", x), programs)

for program in programs:
	name= program.groups()[0]
	size= program.groups()[1][1:-1]
	holding= program.groups()[2]
	if holding != "":
		holding= set(holding[4:].split(", "))
	programInfo[name]= {"size":int(size), "holding": holding}

# Part 1 : return the program that is not held by any other program
print "Part 1: ", set(programInfo.keys()).difference(reduce(lambda x,y: x.union(y), (z["holding"] for z in programInfo.values()), set())).pop()

# For Part 2 we have to traverse the tree anyway
unseenNodes= set(programInfo.keys())
mismatchFound= False
while len(unseenNodes) > 0 and not mismatchFound:
	nextLvlPrograms= filter(lambda x: "heldWeight" not in programInfo[x].keys() and \
								(len(programInfo[x]["holding"]) == 0 or all(map(lambda y: "heldWeight" in programInfo[y], programInfo[x]["holding"]))), \
							programInfo.keys())
	unseenNodes= unseenNodes.difference(nextLvlPrograms)
	for program in nextLvlPrograms:
		childWeights= list(({"name":x, "weight": programInfo[x]["size"] + programInfo[x]["heldWeight"]}) for x in programInfo[program]["holding"])
		childWeightsList= list((x["weight"] for x in childWeights))
		if len(set(childWeightsList)) > 1:
			# Guaranteed to be the first since we are going up
			light= min(childWeightsList)
			heavy= max(childWeightsList)
			if childWeightsList.count(light) > childWeightsList.count(heavy):
				# wrong size is too heavy
				wrongProgram= filter(lambda x: x["weight"]==heavy, childWeights)[0]["name"]
				print "Part 2:", programInfo[wrongProgram]["size"] - (heavy-light)
			else:
				# too light
				wrongProgram= filter(lambda x: x["weight"]==light, childWeights)[0]["name"]
				print "Part 2:", programInfo[wrongProgram]["size"] + (heavy-light)
			mismatchFound= True
			break

		programInfo[program]["heldWeight"]= sum((programInfo[x]["size"] + programInfo[x]["heldWeight"] for x in programInfo[program]["holding"]))

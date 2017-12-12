import re

def connectedComponentForNode(graph, node):
	worklist= set([node])
	visited= set()
	cc= set([node])

	while len(worklist) > 0:
		nextNode= worklist.pop()
		visited.add(nextNode)

		connected= set(graph[nextNode])
		cc= cc.union(connected)
		worklist= worklist.union(connected.difference(visited))

	return cc

fIn= open("input_12.txt")
lines= map(lambda x: x.strip(), fIn.readlines())
fIn.close()

for i in range(len(lines)):
	match= re.match("(\d+) \<\-\> (.*)", lines[i])
	lines[i]= (int(match.groups()[0]), map(lambda x: int(x.strip()), match.groups()[1].split(",")))

# Build graph
graph= {}
for line in lines:
	graph[line[0]]= set(line[1])

cc= connectedComponentForNode(graph, 0)
print "Part 1:", len(cc)

ccCount= 0
while (len(graph) > 0):
	cc= connectedComponentForNode(graph, graph.keys()[0])
	ccCount+= 1
	for n in cc:
		graph.pop(n)

print "Part 2:", ccCount

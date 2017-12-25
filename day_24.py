fIn= open("input_24.txt")
pieces= map(lambda y: ((int(y[0]), int(y[1]))), map(lambda x: x.strip().split("/"), fIn.readlines()))
fIn.close()

longest= 0
longestBridgesMaxW= 0
maxW= 0
# remainingPieces, last, totalWeight, len
queue= [(set(pieces), 0, 0, 0)]
while len(queue) > 0:
	it= queue.pop()
	for piece in filter(lambda x: x[0] == it[1] or x[1] == it[1], it[0]):
		remPieces= set(it[0])
		remPieces.remove(piece)
		w= it[2] + piece[0] + piece[1]
		maxW = maxW if maxW > w else w
		newLen= it[3] + 1
		if newLen > longest:
			longest= newLen
			longestBridgesMaxW= w
		elif newLen == longest and w > longestBridgesMaxW:
			longestBridgesMaxW= w
		queue.append( (remPieces, piece[1] if piece[0] == it[1] else piece[0], w, newLen ) )

print "Part 1:", maxW
print "Part 2:", longestBridgesMaxW, longest

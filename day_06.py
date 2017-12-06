membank= [4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]
steps= 0
configs= {}

while str(membank) not in configs.keys():
	configs[str(membank)]= steps
	bank= membank.index(max(membank))
	blocks= membank[bank]
	membank[bank]= 0
	membank= map(lambda x: x+ blocks/len(membank), membank)
	for i in range(bank+1, bank + 1 + blocks%len(membank)):
		membank[i%len(membank)]+= 1
	steps+= 1

print "Part 1:", steps
print "Part 2:", steps - configs[str(membank)]

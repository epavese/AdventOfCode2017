f= open("input_04.txt")
phrases= map(lambda x: sorted(x.strip().split(" ")), f.readlines())
f.close()

bad= 0
for phrase in phrases:
	for i in range(len(phrase)-1):
		if phrase[i] == phrase[i+1]:
			bad+= 1
			break

print "Part 1:", len(phrases)-bad

for i in range(len(phrases)):
	phrases[i]= sorted(map(lambda x: sorted(x), phrases[i]))

bad= 0
for phrase in phrases:
	for i in range(len(phrase)-1):
		if phrase[i] == phrase[i+1]:
			bad+= 1
			break

print "Part 2:", len(phrases)-bad

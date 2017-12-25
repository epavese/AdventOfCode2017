machine= {}
machine['a']= {}
machine['b']= {}
machine['c']= {}
machine['d']= {}
machine['e']= {}
machine['f']= {}

machine['a'][0]= (1,1,'b')
machine['a'][1]= (0,-1,'c')
machine['b'][0]= (1,-1,'a')
machine['b'][1]= (1,1,'d')
machine['c'][0]= (0,-1,'b')
machine['c'][1]= (0,-1,'e')
machine['d'][0]= (1,1,'a')
machine['d'][1]= (0,1,'b')
machine['e'][0]= (1,-1,'f')
machine['e'][1]= (1,-1,'c')
machine['f'][0]= (1,1,'d')
machine['f'][1]= (1,1,'a')

steps= 0
state= 'a'
cur= 0
ones= set()
while True:
	step= machine[state][1 if cur in ones else 0]
	state= step[2]
	if step[0] == 0:
		ones.discard(cur)
	else:
		ones.add(cur)
	cur+= step[1]

	steps+= 1
	if steps == 12481997:
		break

print "Part 1:", len(ones)

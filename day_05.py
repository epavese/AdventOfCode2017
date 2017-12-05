def stepsToExit(program, inc= lambda x: x+1):
	i= 0
	steps= 0
	while i < len(program):
		nextI= i + program[i]
		program[i]= inc(program[i])
		i= nextI
		steps+= 1
	return steps

f= open("input_05.txt")
program= map(lambda x: int(x.strip()), f.readlines())
f.close()
steps= stepsToExit(list(program))
print "Part 1:", steps

steps= stepsToExit(list(program), lambda x: x+1 if x < 3 else x-1)
print "Part 2:", steps

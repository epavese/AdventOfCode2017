fIn= open("input_18.txt")

def runLine(sndPrg, regs, queue, ip):
	toPush= None
	waiting= False
	if ip < len(sndPrg):
		instr= sndPrg[ip]
		value= 0
		if instr[0] == "snd":
			try:
				value= int(instr[1])
			except ValueError:
				value= regs.get(instr[1], 0)
			toPush= value
		elif instr[0] == "set":
			value= 0
			try:
				value= int(instr[2])
			except ValueError:
				value= regs.get(instr[2], 0)
			regs[instr[1]]= value
		elif instr[0] == "add":
			value= regs.get(instr[1], 0)
			try:
				value+= int(instr[2])
			except ValueError:
				value+= regs.get(instr[2], 0)
			regs[instr[1]]= value
		elif instr[0] == "mul":
			value= regs.get(instr[1], 0)
			try:
				value*= int(instr[2])
			except ValueError:
				value*= regs.get(instr[2], 0)
			regs[instr[1]]= value
		elif instr[0] == "mod":
			value= regs.get(instr[1], 0)
			try:
				value= value % int(instr[2])
			except ValueError:
				value= value % regs.get(instr[2], 0)
			regs[instr[1]]= value
		elif instr[0] == "rcv":
			if len(queue) == 0:
				waiting= True
			else:
				regs[instr[1]]= queue.pop(0)
		elif instr[0] == "jgz":
			jmp= 0
			control= -1
			try:
				control= int(instr[1])
			except ValueError:
				control= regs.get(instr[1], 0)
	
			if control > 0:
				try:
					jmp= int(instr[2])
				except ValueError:
					jmp= regs.get(instr[2], 0)
				ip+= jmp-1
	
		if not waiting:
			ip+= 1
	else: # ip > len(sndPrg):
		waiting= True

	return ip, toPush, waiting

sndPrg= map(lambda x: x.strip().split(), fIn.readlines())
fIn.close()

regs0= {"p": 0}
regs1= {"p": 1}
queue0= []
queue1= []
ip0= 0
ip1= 0
wait0= False
wait1= False
sent0= 0
sent1= 0
finished= False

while not finished:
	# Interleave one line each program. Could minimise busy wait by running each program as much as they can each time
	ip0, toPush0, wait0= runLine(sndPrg, regs0, queue0, ip0)
	if toPush0 is not None:
		queue1.append(toPush0)
		sent0+= 1

	ip1, toPush1, wait1= runLine(sndPrg, regs1, queue1, ip1)
	if toPush1 is not None:
		queue0.append(toPush1)
		sent1+= 1

	if wait0 and wait1:
		finished= True

print "Part 2:", sent1

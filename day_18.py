fIn= open("input_18.txt")
sndPrg= map(lambda x: x.strip().split(), fIn.readlines())
fIn.close()

regs= {}
lastFreq= -1
ip= 0

while ip < len(sndPrg):
	valueRecovered= False
	rcv= 0
	instr= sndPrg[ip] 
	if instr[0] == "snd":
		freq= 0
		try:
			freq= int(instr[1])
		except ValueError:
			freq= regs.get(instr[1], 0)
		lastFreq= freq
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
		control= 0
		try:
			control= int(instr[1])	
		except ValueError:
			control= regs.get(instr[1], 0)
		if control != 0:
			valueRecovered= True
			rcv= lastFreq
			print "Part 1:", rcv
			break
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
			ip+= jmp
			continue

	ip+= 1

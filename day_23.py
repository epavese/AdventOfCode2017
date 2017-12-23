fIn= open("input_23.txt")
sndPrg= map(lambda x: x.strip().split(), fIn.readlines())
fIn.close()

regs= {}
ip= 0
muls= 0

while ip < len(sndPrg):
	valueRecovered= False
	rcv= 0
	instr= sndPrg[ip] 
	if instr[0] == "set":
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
	elif instr[0] == "sub":
		value= regs.get(instr[1], 0)
		try:
			value-= int(instr[2])
		except ValueError:
			value-= regs.get(instr[2], 0)
		regs[instr[1]]= value
	elif instr[0] == "mul":
		value= regs.get(instr[1], 0)
		try:
			value*= int(instr[2])
		except ValueError:
			value*= regs.get(instr[2], 0)
		regs[instr[1]]= value
		muls+= 1
	elif instr[0] == "jnz":
		jmp= 0
		control= -1
		try:
			control= int(instr[1])
		except ValueError:
			control= regs.get(instr[1], 0)

		if control != 0:
			try:
				jmp= int(instr[2])
			except ValueError:
				jmp= regs.get(instr[2], 0)
			ip+= jmp
			continue
	ip+= 1

print "Part 1:", muls
print "Part 2:", regs.get('h',0)

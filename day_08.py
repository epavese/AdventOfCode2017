import re

def execInstr(instr, cpu):
	reg= instr[0]
	condReg= instr[3]
	regVal= cpu.get(reg, 0)
	condOpVal= cpu.get(condReg, 0)
	if instr[4](condOpVal, instr[5]):
		regVal= instr[1](regVal, instr[2])
	cpu[reg]= regVal
	return regVal

fIn= open("input_08.txt")
program= map(lambda x: x.strip(), fIn.readlines())
fIn.close()

funs= {"inc": (lambda x,y: x+y), "dec": (lambda x,y: x-y), "==": (lambda x,y: x==y), "<=": (lambda x,y: x<=y), ">=": (lambda x,y: x>=y), "!=": (lambda x,y: x!=y), "<": (lambda x,y: x<y), ">": (lambda x,y: x>y)}

parsedProgram= []
cpu= {}
for line in program:
	match= re.match("([a-z]+) (inc|dec) (\-?\d+) if ([a-z]+) (\<\=|\>\=|\<|\>|\!\=|\=\=) (\-?\d+)", line)
	parsedProgram.append((match.groups()[0], funs[match.groups()[1]], int(match.groups()[2]), match.groups()[3], funs[match.groups()[4]], int(match.groups()[5])))

maxVal= 0
for line in parsedProgram:
	val= execInstr(line,cpu)
	maxVal= maxVal if maxVal > val else val

print "Part 1:", max(cpu.values())
print "Part 2:", maxVal

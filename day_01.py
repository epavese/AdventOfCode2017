f= open("input_01.txt")
digits= f.readlines()[0].strip()
f.close()

res= 0
for i in range(len(digits)):
	if digits[i] == digits[(i+1)%len(digits)]:
		res= res + int(digits[i])

print "Part A: ", res

res= 0
for i in range(len(digits)):
	if digits[i] == digits[(i+len(digits)/2)%len(digits)]:
		res= res + int(digits[i])

print "Part B: ", res

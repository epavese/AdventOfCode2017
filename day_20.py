import operator

# Particle = [pos, vel, acc]
def updateParticle(particle):
	particle[1]= map(operator.add, particle[1], particle[2])
	particle[0]= map(operator.add, particle[0], particle[1])
	return particle

def sameSign(v1, v2):
	for i in range(len(v1)):
		if (v1[i] > 0 and v2[i] < 0) or (v1[i] < 0 and v2[i] > 0):
			return False
	return True

def cmpFurther(p1, p2):
	acc1= sum(map(abs, p1[2]))
	acc2= sum(map(abs, p2[2]))
	vel1= sum(map(abs, p1[1]))
	vel2= sum(map(abs, p2[1]))
	d1= sum(map(abs, p1[0]))
	d2= sum(map(abs, p2[0]))

	if acc1 < acc2:
		return -1
	elif acc1 > acc2:
		return 1
	elif vel1 < vel2:
		return -1
	elif vel1 > vel2:
		return 1
	elif d1 < d2:
		return -1
	elif d1 > d2:
		return 1
	else:
		return 0


fIn= open("input_20.txt")
particles= map(lambda x: x.strip().split(","), fIn.readlines())
fIn.close()

for i in range(len(particles)):
	line= particles[i]
	pos= map(lambda x: int(x.replace("p=<","").replace(">","").strip()), line[:3])
	vel= map(lambda x: int(x.replace("v=<","").replace(">","").strip()), line[3:6])
	acc= map(lambda x: int(x.replace("a=<","").replace(">","").strip()), line[6:])
	particles[i]= [pos, vel, acc]

# First each particle will be (maybe) decelerated and then actually irreversibly accelerated
# 	A particle is accelerated when its velocity sign matches its acceleration sign (all coords)
# Then a particle might still be moving towards <0,0,0>.
# 	A particle will definitely be moving away from <0,0,0> when its position sign matches its velocity sign
# At this point we compare first accelerations, then speeds, then positions

decelerating= True
while decelerating:
	decelerating= False
	for i in range(len(particles)):
		newPart= updateParticle(particles[i])
		if not sameSign(newPart[1], newPart[2]):
			decelerating= True
		particles[i]= newPart

movingCloser= True
while movingCloser:
	movingCloser= False
	for i in range(len(particles)):
		newPart= updateParticle(particles[i])
		if not sameSign(newPart[0], newPart[1]):
			movingCloser= True
		particles[i]= newPart

partMap= {}
for i in range(len(particles)):
	partMap[str(particles[i])]= i

particles= sorted(particles, cmpFurther)
print "Part 1:", partMap[str(particles[0])]

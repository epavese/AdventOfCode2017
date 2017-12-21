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

fIn= open("input_20.txt")
particles= map(lambda x: x.strip().split(","), fIn.readlines())
fIn.close()

for i in range(len(particles)):
	line= particles[i]
	pos= map(lambda x: int(x.replace("p=<","").replace(">","").strip()), line[:3])
	vel= map(lambda x: int(x.replace("v=<","").replace(">","").strip()), line[3:6])
	acc= map(lambda x: int(x.replace("a=<","").replace(">","").strip()), line[6:])
	particles[i]= [pos, vel, acc]

particleMap= {}
for i in range(len(particles)):
	particleMap[i]= particles[i]

# For each pair of particles we create a vector which represents the distance (along with speed and acceleration) between them as
# well as how fast they close to each other. At this point we can forget about the particles themselves
# If this difference reaches <0,0,0>, they have collided
# If this difference no longer decelerates and no longer moves closer to <0,0,0>, they have escaped collision forever

collParticles= []
for i in range(len(particles)):
	for j in range(i+1, len(particles)):
		collision= [i, j, [map(operator.sub, particles[i][0], particles[j][0]), map(operator.sub, particles[i][1], particles[j][1]), map(operator.sub, particles[i][2], particles[j][2])]]
		collParticles.append(collision)

print "Built collision particles", len(collParticles)
ticks= 1
decelerating= True
while decelerating and len(collParticles) > 0:
	decelerating= False
	for i in range(len(collParticles)):
		newPart= updateParticle(collParticles[i][2])
		if not sameSign(newPart[1], newPart[2]):
			decelerating= True
		collParticles[i]= [collParticles[i][0], collParticles[i][1], newPart]

	# check and purge collisions
	collided= set()
	for i in range(len(collParticles)):
		p1= collParticles[i][0]
		p2= collParticles[i][1]
		position= collParticles[i][2][0]
		if position == [0,0,0]:	# collided!
			print "Collision!:", p1, p2
			collided.add(p1)
			collided.add(p2)
	# purge particles from map
	for part in collided:
		particleMap.pop(part)
		# purge particles from collisions
		collParticles= filter(lambda x: x[0] != part and x[1] != part, collParticles)
	print "Particles remain at tick:", ticks, len(particleMap)
	ticks+= 1

print "All stopped decelerating"
movingCloser= True
while movingCloser and len(collParticles) > 0:
	movingCloser= False
	for i in range(len(collParticles)):
		newPart= updateParticle(collParticles[i][2])
		if not sameSign(newPart[0], newPart[1]):
			movingCloser= True
		collParticles[i]= [collParticles[i][0], collParticles[i][1], newPart]
	
	# check and purge collisions
	collided= set()
	for i in range(len(collParticles)):
		p1= collParticles[i][0]
		p2= collParticles[i][1]
		position= collParticles[i][2][0]
		if position == [0,0,0]:	# collided!
			print "Collision!:", p1, p2
			collided.add(p1)
			collided.add(p2)
	# purge particles from map
	for part in collided:
		particleMap.pop(part)
		# purge particles from collisions
		collParticles= filter(lambda x: x[0] != part and x[1] != part, collParticles)
	print "Particles remain at tick:", ticks, len(particleMap)
	ticks+= 1

print "Part 2:", len(particleMap)

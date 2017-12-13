#!/usr/local/bin/python

def getDangerPeriod(layersCfg):
	danger= {}
	for l in layersCfg:
		danger[l]= 2*layersCfg[l]-2
	return danger

def caught(startTime, layersCfg, earlyStop= False):
	danger= getDangerPeriod(layersCfg)
	maxLayer= max(layersCfg.keys())
	severity= 0
	caught= False
	for i in range(maxLayer+1):
		if i in layersCfg and (startTime+i)%danger[i] == 0:
			severity+= i*layersCfg[i]
			caught= True
			if earlyStop:
				break
	return (caught, severity, i)

def getScannerPosition(time, layerSize):
	mvmtRange= 2*layerSize-2
	position= time % mvmtRange
	if position > layerSize:
		position= 2*layerSize - 2 - position

	return position

fIn= open("input_13.txt")
layers= map(lambda x: [int(x.strip().split(":")[0].strip()), int(x.strip().split(":")[1].strip())], fIn.readlines())
fIn.close()

layersCfg= {}
for l in layers:
	layersCfg[l[0]]= l[1]


print "Part 1:", caught(0, layersCfg)[1]

# Bruteforcing for part 2, slow. Chinese remainder theorem should apply here, I'll see to it later
startTime= 0 
danger= getDangerPeriod(layersCfg)
while True:
	gotcha= caught(startTime, layersCfg, True)
	if not gotcha[0]:
		break
	startTime+= 1

print "Part 2:", startTime

#!/usr/local/bin/python

seedA= 618
prevA= seedA
seedB= 814
prevB= seedB
factorA= 16807
factorB= 48271
divisor= 2147483647 # Hm, this is 2**31-1. Probably an efficient way to calculate mod without dividing exists
mask= 2**16-1
iters= 40000000
equalCnt= 0
for i in range(iters):
	prevA= (prevA*factorA)%divisor
	prevB= (prevB*factorB)%divisor

	if prevA & mask == prevB & mask:
		equalCnt+= 1

print "Part 1:", equalCnt

fourMulMask= 3
eightMulMask= 7
pairCnt= 0
iters= 5000000
equalCnt= 0

while pairCnt < iters:
	prevA= (prevA*factorA)%divisor
	while (prevA & fourMulMask):
		prevA= (prevA*factorA)%divisor

	prevB= (prevB*factorB)%divisor
	while (prevB & eightMulMask):
		prevB= (prevB*factorB)%divisor

	if prevA & mask == prevB & mask:
		equalCnt+= 1

	pairCnt+= 1

print "Part 2:", equalCnt

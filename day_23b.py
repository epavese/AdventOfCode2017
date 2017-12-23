# g= 1
# a= 1
# b= 107900
# c= 124900
# while b != c:	# this loop runs 1000 times
#	f= 1
#	d= 2
#	while g != 0: # this loop runs 107898 times, d goes 1-wise between 2 and 107900
#		e= 2
#		while g != 0:	# this loop runs 107898 times. e goes 1-wise between 2 and 107900
#			if d*e == b:
#				f= 0
#			e+= 1
#			g= e
#			g-= b
#		d+= 1
#		g= d
#		g-= b
#	if f == 0
#		h+= 1
#	g= b-c
#	b+= 17

# it seems to be analysing numbers between 107900 and 124900, in 17 step increments, counting how many of those are not prime
import math

def isPrime(x):
	stop= math.sqrt(x)
	i= 2
	while i < stop:
		if x%i == 0:
			return False
		i+= 1
	return True

x= 107900
h= 0
for i in range(1001):
	if not isPrime(x):
		h+= 1
	x+= 17

print h

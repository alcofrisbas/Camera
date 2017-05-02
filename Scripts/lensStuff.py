def focalLength(r1, r2, ior, ):
	if r1 == "p":
		rR1 = 0
	else:
		rR1 = 1.0/r1

	if r2 == "p":
		rR2 = 0
	else:
		rR2 = 1.0/r2

	rF = (ior - 1)*(rR1-rR2)
	
	return 1/rF

def distanceImage(f1, do1):
	return 1.0/((1.0/f1)-(1.0/do1))


def twoLensImageDistance(f1, f2, do1, L):
	#print f1
	#print do1
	di1 = 1.0/((1.0/f1)-(1.0/do1))
	#print 1.0/di1
	do2 = L - di1
	
	di2 = 1.0/((1.0/f2)-(1.0/do2))

	return di2


def threeLensImageDistance(f1, f2, f3, do1, L1, L2):
	#print f1
	#print do1
	di1 = 1.0/((1.0/f1)-(1.0/do1))
	#print 1.0/di1
	do2 = L1 - di1
	
	di2 = 1.0/((1.0/f2)-(1.0/do2))

	do3 = L2 - di2

	di3 = 1.0/((1.0/f3)-(1.0/do3))

	

	return di3



def twoLenses(f1,f2,d,s1):
	rF1 = 1.0/f1
	rF2 = 1.0/f2
	rS1 = 1.0/s1
	#print rF1+rF2
	#print (d/(f1*f2))

	
	rF = rF1 + rF2 - (d/(rF1*rF2))

	f = 1/rF
	
	#first image distance
	rS1p = rF1-rS1
	print rS1p
	s1p = 1/rS1p
	print s1p
	

	

	#rS2 = rS1 - rF
	#s2 = 1/rS2
	print "f "+str(f)
	#print "s2 "+str(s2)

#f1 = focalLength(51.68, "p", 1.5168)
#f2 = focalLength(25.84, -25.84, 1.5168)

#twoLenses(10, 5, 7, 8)

distances = [500, 600, 700, 800, 900, 1000, 1200, 1500, 2000, 3000, 5000, 10000]

#print twoLensImageDistance(100, 150,600, 400)

for i in distances:
	print i, distanceImage(50, i)
	#print i,twoLensImageDistance(50, 40, i, 10)
	#print i, threeLensImageDistance(50, -155.04, 50, i, 16, 9.5)

 
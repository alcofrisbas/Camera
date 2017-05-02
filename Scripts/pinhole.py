#focal length of lens according to stanford site: (size of pinhole mm)^2*750

#"""""""""""""""""""" according to diy photography: (diameter mm/0.03679)^2
#we're going with connors formula(diyPhoto)
import math

def stanfordNums(D, const):
	return D**2 * const
	
def connorsFormula(D, const):
	return (D/const)**2
	
	#f = (D/c)^2
	#rt(f) = D/c
	#c(rt(f)) = D
	
def viewAngle(D, t):
	return math.degrees(math.atan((D/2)/(t/2)))*2
	
def imageDiameter(f, vA):
	return 2 * f * math.tan(math.radians(vA/2))

def fStop(f, D):
	return f/D
	
def focalToDiameter(f, c):
	return  c * math.sqrt(f)
	
if __name__ == "__main__":
	#print stanfordNums(0.3, 750)
	'''D = 0.3
	f = connorsFormula(D, 0.03679)
	vA = viewAngle(D, 0.0762)
	iD = imageDiameter(f, vA)
	fS = fStop(f, D)
	print f, vA, iD, fS'''
	
	connorsConst = 0.03679
	t = 0.097
	fList = [29,31,35]
	
	for i in fList:
		D = focalToDiameter(i, connorsConst)
		vA = viewAngle(D, t)
		iD = imageDiameter(i, vA)
		fS = fStop(i, D)
		print i, D, iD, fS
		
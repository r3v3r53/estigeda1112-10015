
def kdTree(P, depth):
	if len(P) == 1:
		return P
	elif depth % 2 == 0:
		P1 = P[:len(P)/2]
		P2 = P[len(P)/2:len(P)]
	else:
		median = floor(len(P)/2)+1
		V = P[median]
		P1 = P[:median]
		P2 = P[median:]
		
	return x

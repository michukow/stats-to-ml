import math
def ile_rekordow(p,margines):
	return math.ceil((1.96**2*p*(1-p))/margines**2)
print(ile_rekordow(0.04,0.01))
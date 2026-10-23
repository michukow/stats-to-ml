import numpy as np
import matplotlib.pyplot as plt
N=10000
def f(x):
	return x**2/9
def g(x):
	return 1
def calka(f,a,b,N):
	delta=(b-a)/N
	pole=0
	punkty=np.linspace(a,b,N+1)
	srodki=(punkty[:-1]+punkty[1:])/2
	for i in range(N):
		pole+=f(srodki[i])*delta
	return pole

def mediana(f,a,b,tol):
	iteracje=0
	lewy=a
	prawy=b
	while(prawy-lewy)>tol:
		srodek=(prawy+lewy)/2
		p=calka(f,a,srodek,N)
		iteracje+=1
		if p<0.5:
			lewy=srodek
		else:
			prawy=srodek
	return (lewy+prawy)/2,iteracje
M,iteracje=mediana(f,0,3,0.000001)

def medianka():
	rng=np.random.default_rng(42)
	u=rng.uniform(0,1,10000)
	x=3*u**(1/3)
	return x,np.median(x)

x,_=medianka()

def wykres():
	siatka=np.linspace(0,3,200)
	plt.hist(x,bins=50,density=True) 
	plt.plot(siatka,f(siatka))     
	plt.show()

print(f"Wynik I: {M}")
print(13.5 ** (1/3))
print(f"Iteracje: {iteracje}")
print(f"Wynik II: {medianka()[1]}")
print(f"Średnia: {x.mean():.4f}")
print(f"P(X > 2): {(x > 2).mean():.4f}")
wykres()



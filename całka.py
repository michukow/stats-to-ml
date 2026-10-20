import numpy as np
N=100
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
print(calka(f,1,2,N))
print(calka(f,2,3,N))
print(calka(f,0,3,N))
print(round(abs(calka(f, 1, 2, N) - 7/27),2))
print(round(abs(calka(f, 1, 2, 10) - 7/27),2))
print(round(abs(calka(f, 1, 2, 100) - 7/27),2))
print(round(abs(calka(f, 1, 2, 1000) - 7/27),2))
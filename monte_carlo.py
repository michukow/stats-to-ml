import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(42)
x=rng.uniform(0,10,120)
ilosc_losowan=10000
wyniki=np.zeros(ilosc_losowan)
def mnk(x,y):
		X=np.column_stack((np.ones(len(y)),x))
		Xtx=X.T@X
		Xty=X.T@y
		b=np.linalg.inv(Xtx)@Xty
		y_hat=X@b
		e=y-y_hat
		SS_calk=((y-y.mean())**2).sum()
		SS_wyj=((y_hat-y.mean())**2).sum()
		SS_re=(e**2).sum()
		R2=SS_wyj/SS_calk
		n=len(y)
		k=X.shape[1]-1
		R2_adj=1-((SS_re*(n-1))/(SS_calk*(n-k-1)))
		return b[1]
for i in range (ilosc_losowan):
	eps=rng.normal(0,2,120)
	y=1+2*x+eps
	wyniki[i]=mnk(x,y)
print(f"Średnia: {wyniki.mean()}")
print(f"Odchylenie standardowe: {wyniki.std()}")
plt.hist(wyniki,bins=40)
plt.title("Wykres gęstości")
plt.show()
import statsmodels.api as sm
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

d=sm.datasets.macrodata.load_pandas().data
dochod=np.diff(np.log(d["realdpi"].to_numpy()))
stopa=d["realint"].to_numpy()[1:]
x=np.column_stack((dochod,stopa))
y=np.diff(np.log(d["realcons"].to_numpy()))
def regression(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	Xtx=X.T@X
	Xty=X.T@y
	b=np.linalg.inv(Xtx)@Xty
	return b

def errors(x,y):
	b=regression(x,y)
	X=np.column_stack((np.ones(len(x)),x))
	y_hat=X@b
	e=y-y_hat
	return e

def n_k(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	n=len(x)
	k=X.shape[1]-1
	v=n-k-1
	return n,k,v

def R(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	b=regression(x,y)
	n,k,_=n_k(x,y)
	y_hat=X@b
	e=y-y_hat
	SS_calk=(y-y.mean())**2
	SS_wyj=(y_hat-y.mean())**2
	SS_re=(e**2)
	R2=SS_wyj.sum()/SS_calk.sum()
	R2_adj=1-((SS_re.sum()*(n-1))/(SS_calk.sum()*(n-k-1)))
	return R2,R2_adj

e=errors(x,y)
R2,R2_adj=R(x,y)
print(f"Korelacja: {round(np.corrcoef(e[1:],e[:-1])[0, 1],2)}")
print(f"Statystyka DW: {round(((np.diff(e)**2).sum())/(e**2).sum(),2)}")
print(f"R2: {round(R2,2)}")
print(f"R2_adj: {round(R2_adj,2)}")
plt.plot(e)
plt.axhline(0,color="black")
plt.show()
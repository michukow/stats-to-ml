import statsmodels.api as sm
import numpy as np
from scipy import stats

d=sm.datasets.macrodata.load_pandas().data
x=np.column_stack((np.log(d["realdpi"]),d["realint"]))
y=np.log(d["realcons"])
def regression(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	Xtx=X.T@X
	Xty=X.T@y
	b=np.linalg.inv(Xtx)@Xty
	return b

def standard_error(x):
	X=np.column_stack((np.ones(len(x)),x)) 
	se=np.diag(np.linalg.inv(X.T@X))
	return se[0],se[1],se[2]

def n_k(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	n=len(x)
	k=X.shape[1]-1
	v=n-k-1
	return n,k,v

def R(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	b=regression(x,y)
	y_hat=X@b
	e=y-y_hat
	SS_calk=(y-y.mean())**2
	SS_wyj=(y_hat-y.mean())**2
	SS_re=(e**2)
	R2=SS_wyj.sum()/SS_calk.sum()
	R2_adj=1-((SS_re.sum()*(n-1))/(SS_calk.sum()*(n-k-1)))
	return R2,R2_adj

const1,ln_dochod,stopa=regression(x,y)
n,k,v=n_k(x,y)
se0,se1,se2=standard_error(x)
macierz=standard_error(x)
R2,R2_adj=R(x,y)

print("Slopes:")
print(f"b0: {round(const1,4)}")
print(f"b1: {round(ln_dochod,4)}")
print(f"b2: {round(stopa,4)}\n")

print("Standard Errors (SE):")
print(f"SE(b0): {se0}")
print(f"SE(b1): {se1}")
print(f"SE(b2): {se2}\n")

print(f"t-stats:")
print(f"t0: {const1/se0}")
print(f"t1: {ln_dochod/se1}")
print(f"t2: {stopa/se2}\n")

print(f"p-values:")
print(f"p-value: {2*(1-stats.t.cdf(const1/se0,n-k-1))}")
print(f"p-value: {2*(1-stats.t.cdf(ln_dochod/se1,n-k-1))}")
print(f"p-value: {2*(1-stats.t.cdf(stopa/se2,n-k-1))}\n")

print("Summary:")
print(f"n={n}")
print(f"k={k}")
print(f"Degrees of freedom (df): {v}")
print(f"R2: {R2}")
print(f"R2_adjusted: {R2_adj}")


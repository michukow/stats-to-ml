import numpy as np
from scipy import stats

rng=np.random.default_rng(42)
n=100
x=rng.uniform(0,10,n)
y=1+2*x+rng.normal(0,0.1*x**2)

X=np.column_stack([np.ones(n),x])
b=np.linalg.lstsq(X,y,rcond=None)[0]
e=y-X@b

Z=np.column_stack([np.ones(n),x,x**2])
e2=e**2
g=np.linalg.lstsq(Z,e2,rcond=None)[0]
reszty_pom=e2-Z@g
SS_res=(reszty_pom**2).sum()
SS_calk=((e2-e2.mean())**2).sum()
R2=1-SS_res/SS_calk

LM=n*R2
p=1-stats.chi2.cdf(LM,2)
print(f"LM = {LM:.2f}, p = {p:.2e}")
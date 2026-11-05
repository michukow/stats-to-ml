import numpy as np
import statsmodels.api as sm
from scipy import stats

d=sm.datasets.macrodata.load_pandas().data
y=np.diff(np.log(d["realcons"].to_numpy()))
dochod=np.diff(np.log(d["realdpi"].to_numpy()))
stopa=d["realint"].to_numpy()[1:]
n=len(y)

def ss_res(zmienne):
    X=np.column_stack([np.ones(n)]+zmienne)
    b=np.linalg.inv(X.T@X)@X.T@y
    e=y-X@b
    return (e**2).sum()

def test_F(okroj,pelny,q,df):
    F=((okroj-pelny)/q)/(pelny/(df))
    p=1-stats.f.cdf(F,q,df)
    return F,p

pelny=ss_res([dochod,stopa])
df=n-3

F1,p1=test_F(ss_res([]),pelny,2,df)
print(f"Test 1 (dochód i stopa razem): F = {F1:.2f}, p = {p1:.2e}")

F2,p2=test_F(ss_res([dochod]),pelny,1,df)
print(f"Test 2 (sama stopa): F = {F2:.2f}, p = {p2:.3f}")
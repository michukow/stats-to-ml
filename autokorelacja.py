import statsmodels.api as sm
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

d=sm.datasets.macrodata.load_pandas().data
x=np.column_stack((np.log(d["realdpi"]),d["realint"]))
y=np.log(d["realcons"])
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
	e=y-y_hat
	return e

e=errors(x,y)
print(f"Korelacja: {round(np.corrcoef(e[1:],e[:-1])[0, 1],2)}")
print(f"Statystyka DW: {round(((np.diff(e)**2).sum())/(e**2).sum(),2)}")
plt.plot(e)
plt.axhline(0,color="black")
plt.show()
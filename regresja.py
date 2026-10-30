import statsmodels.api as sm
import numpy as np
d=sm.datasets.macrodata.load_pandas().data
x=np.column_stack((np.log(d["realdpi"]),d["realint"]))
y=np.log(d["realcons"])
def regression(x,y):
	X=np.column_stack((np.ones(len(x)),x))
	Xtx=X.T@X
	Xty=X.T@y
	b=np.linalg.inv(Xtx)@Xty
	return b[0],b[1],b[2]
const1,ln_dochod,stopa=regression(x,y)
print("Slope:")
print(f"b0: {round(const1,4)}")
print(f"b1: {round(ln_dochod,4)}")
print(f"b2: {round(stopa,4)}")


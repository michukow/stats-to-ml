import statsmodels.api as sm
import numpy as np
d=sm.datasets.macrodata.load_pandas().data
X=np.column_stack((np.log(d["realdpi"]),d["realint"]))
y=np.array(d["realcons"])


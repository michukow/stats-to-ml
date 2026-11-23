import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white

df=pd.read_csv("C:\\Users\\micha\\Desktop\\Python\\stats-to-ml\\rowery-kraków\\rowery_pogoda.csv",parse_dates=["data"])

df=df[df["Bulwary"]>0] 
dni=pd.get_dummies(df["data"].dt.day_of_week,prefix="dzien",drop_first=True,dtype=float)
X=sm.add_constant(pd.concat([df[["temp_srednia","opad_suma"]],dni],axis=1))
y=np.log(df["Bulwary"])
model=sm.OLS(y,X).fit(cov_type="HAC",cov_kwds={"maxlags":7})
procenty=(np.exp(model.params)-1)*100
print(procenty.round(1))
print(f"R² = {model.rsquared:.3f}")

#reszty
plt.scatter(model.fittedvalues,model.resid,s=4,alpha=0.4)
plt.axhline(0,color="black")
plt.xlabel("przewidywany ruch")
plt.ylabel("reszta")
plt.savefig("reszty_bulwary.png",dpi=150,bbox_inches="tight")
plt.show()

lm, p, _, _=het_white(model.resid,X)
print(f"White: LM = {lm:.1f}, p = {p:.2e}")

#Newey–West
model_nw=sm.OLS(y,X).fit(cov_type="HAC",cov_kwds={"maxlags": 7})

porownanie=pd.DataFrame({"SE zwykłe":model.bse,"SE Newey-West":model_nw.bse,"p zwykłe":model.pvalues,"p Newey-West":model_nw.pvalues,})
print(porownanie.round(3))
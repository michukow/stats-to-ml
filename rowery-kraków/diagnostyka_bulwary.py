import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_white

df=pd.read_csv("C:\\Users\\micha\\Desktop\\Python\\stats-to-ml\\rowery-kraków\\rowery_pogoda.csv",parse_dates=["data"])

df["padalo"]=(df["opad_suma"]>0).astype(float)
dni=pd.get_dummies(df["data"].dt.day_of_week,prefix="dzien",drop_first=True,dtype=float)
X=sm.add_constant(pd.concat([df[["temp_srednia","padalo"]],dni],axis=1))
y=df["Bulwary"]
model=sm.OLS(y,X).fit()

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
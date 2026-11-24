import numpy as np
import pandas as pd
import statsmodels.api as sm

df=pd.read_csv("rowery_pogoda.csv",parse_dates=["data"])

dni=pd.get_dummies(df["data"].dt.day_of_week,prefix="dzien",drop_first=True,dtype=float)
X_wszystko = pd.concat([df[["temp_srednia","opad_suma"]],dni],axis=1)

wyniki={}
for licznik in ["Bulwary","Mogilska"]:
    ok=df[licznik]>0
    X=sm.add_constant(X_wszystko[ok])
    y=np.log(df.loc[ok,licznik])
    model=sm.OLS(y,X).fit(cov_type="HAC",cov_kwds={"maxlags": 7})
    wyniki[licznik]=((np.exp(model.params)-1)*100).round(1)

tabela=pd.DataFrame(wyniki).drop("const")
print(tabela)
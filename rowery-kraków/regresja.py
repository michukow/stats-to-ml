import pandas as pd
import statsmodels.api as sm

df=pd.read_csv("rowery_pogoda.csv",parse_dates=["data"])

df["padalo"]=(df["opad_suma"] > 0).astype(float)
dni=pd.get_dummies(df["data"].dt.dayofweek, prefix="dzien", drop_first=True, dtype=float)

X=pd.concat([df[["temp_srednia","padalo"]], dni],axis=1)
X=sm.add_constant(X)
y=df["Bulwary"]

model=sm.OLS(y,X).fit()
print(model.summary())
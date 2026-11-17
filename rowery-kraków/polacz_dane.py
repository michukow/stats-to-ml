import sys
import pandas as pd
from pobierz_pogode import pobierz_pogode

liczniki=pd.read_csv("liczniki_czyste.csv",parse_dates=["data"])
pogoda=pobierz_pogode("2016-11-18", "2026-10-31")
pogoda["data"]=pd.to_datetime(pogoda["data"])
pogoda=pogoda.rename(columns={"temp_2m_srednia":"om_temp","opad_suma":"om_opady"})
df=liczniki.merge(pogoda[["data","om_temp","om_opady"]],on="data",how="left")

oba=df["temp_srednia"].notna()
print("Korelacja temperatur:",df.loc[oba,["temp_srednia","om_temp"]].corr().iloc[0, 1].round(3))
print("Różnica temp (ZTP - OM): ",(df.loc[oba, "temp_srednia"]-df.loc[oba, "om_temp"]).mean().round(2))
print((df.loc[oba, "temp_srednia"]-df.loc[oba,"om_temp"]).describe().round(2))
print("Korelacja opadów:",df.loc[oba, ["opad_suma","om_opady"]].corr().iloc[0,1].round(3))

df["temp_srednia"]=df["temp_srednia"].fillna(df["om_temp"]-0.25)
df["opad_suma"]=df["opad_suma"].fillna(df["om_opady"])
print("Braki po uzupełnieniu:",df[["temp_srednia","opad_suma"]].isna().sum().tolist())
df.to_csv("rowery_pogoda.csv",index=False)
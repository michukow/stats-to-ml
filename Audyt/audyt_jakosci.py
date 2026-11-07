import pandas as pd
df=pd.read_csv("dane_pola.csv")
print(df.head())
print(df.describe()) #Istnieje pole, które ma ujemną wartość w ha
#print(df.shape)
#print(df.isna().sum()) #pokazuje braki w danych
#print(df.duplicated().sum()) #pokazuje zdublowane dane
df["data_zbioru"]=pd.to_datetime(df["data_zbioru"])
df["uprawa"]=df["uprawa"].str.strip().str.lower()
print(df["uprawa"].value_counts())
print(f"Minimum: {df["data_zbioru"].min()}, Maksimum: {df["data_zbioru"].max()}")
print(df.isna().sum())
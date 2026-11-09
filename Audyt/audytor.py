import pandas as pd

def braki(df):
    a=df.isna().sum()
    return a[a>0]

def duplikaty(df):
    return df.duplicated().sum()

def ujemne(df):
    wynik={}
    for kol in df.select_dtypes("number").columns:
        liczba=(df[kol]<0).sum()
        if liczba>0:
            wynik[kol]=int(liczba)
    return wynik

def outliery(df):
    wynik={}
    for kol in df.select_dtypes("number").columns:
        q1=df[kol].quantile(0.25)
        q3=df[kol].quantile(0.75)
        iqr=q3-q1
        za_male=df[kol]<q1-3*iqr
        za_duze=df[kol]>q3+3*iqr
        liczba=za_male.sum()+za_duze.sum()
        if liczba>0:
            wynik[kol]=int(liczba)
    return wynik

def niespojny_zapis(df):
    wynik={}
    for kol in df.select_dtypes(include=["object","string"]).columns:
        przed=df[kol].nunique()
        po=df[kol].str.strip().str.lower().nunique()
        if po<przed:
            wynik[kol]=przed-po
    return wynik

def daty_z_przyszlosci(df):
    dzis=pd.Timestamp.today()
    wynik={}
    for kol in df.select_dtypes(include=["object","string"]).columns:
        daty=pd.to_datetime(df[kol],errors="coerce")
        udane=daty.notna().mean()      
        if udane>0.9:
            liczba=(daty>dzis).sum()
            if liczba>0:
                wynik[kol]=int(liczba)
    return wynik

def raport(df):
    print(f"Wiersze: {len(df)} kolumny: {df.shape[1]}\n")
    print(f"Braki:\n {braki(df)}\n")
    print(f"Duplikaty: {duplikaty(df)}\n")
    print(f"Ujemne: {ujemne(df)}\n")
    print(f"Outlier-y: {outliery(df)}\n")
    print(f"Niespójny zapis: {niespojny_zapis(df)}\n")
    print("Daty z przyszłości:",daty_z_przyszlosci(df))

if __name__=="__main__":
    df=pd.read_csv(r"C:\Users\micha\Desktop\Python\Audyt\dane_pola.csv")
    raport(df)
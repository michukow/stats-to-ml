import sys
import pandas as pd
import matplotlib.pyplot as plt
sys.path.append("../Audyt")
from audytor import braki, duplikaty, ujemne, outliery, raport
plik="dane/liczniki_krakow.csv"
df=pd.read_csv(plik,decimal=",")

kol="Dworzec Główny"
#zle = df[kol][pd.to_numeric(df[kol],errors="coerce").isna() & df[kol].notna()]
#print(repr(zle.tolist()),df.loc[zle.index,"Date"].tolist())

df[kol]=pd.to_numeric(df[kol],errors="coerce")
# 2. Daty
df["Date"]=pd.to_datetime(df["Date"])
df = df.rename(columns={
    "Date": "data",
    "Maksymalna temperatura dobowa [°C]": "temp_max",
    "Minimalna temperatura dobowa [°C]": "temp_min",
    "Średnia temperatura dobowa [°C]": "temp_srednia",
    "Temperatura minimalna przy gruncie [°C]": "temp_grunt",
    "Suma dobowa opadów [mm]": "opad_suma"
})

df.to_csv("liczniki_czyste.csv", index=False)
print(df.dtypes)

for licznik in ["Bulwary", "Mogilska"]:
    plt.plot(df[licznik].rolling(30).mean(), label=licznik)

plt.title("Ruch rowerowy w Krakowie (średnia z 30 dni)")
plt.ylabel("rowery na dobę")
plt.legend()
plt.savefig("ruch_w_czasie.png",dpi=150,bbox_inches="tight")
plt.show()
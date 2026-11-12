import os
import requests
import pandas as pd

URL="https://archive-api.open-meteo.com/v1/archive"
SZER=50.06
DLUG=19.94
START="2022-01-01"
KONIEC="2025-12-31"
PLIK="dane/pogoda_krakow.csv"

def pobierz_pogode(start,koniec):
    """Dzienna pogoda dla Krakowa z archiwum OpenMeteo."""
    params={
        "latitude": SZER,
        "longitude": DLUG,
        "start_date": start,
        "end_date": koniec,
        "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max",
        "timezone": "Europe/Warsaw",
    }
    r=requests.get(URL,params=params,timeout=30)
    r.raise_for_status()
    df=pd.DataFrame(r.json()["daily"])
    df=df.rename(columns={
        "time":"data",
        "temperature_2m_mean": "temp_2m_srednia" ,
        "precipitation_sum": "opad_suma" ,
        "wind_speed_10m_max": "wiatr_predkosc_max" ,
    })
    return df

if __name__ == "__main__":
    os.makedirs("dane",exist_ok=True)
    df=pobierz_pogode(START,KONIEC)
    df.to_csv(PLIK,index=False)
    print(df.head())
    print(df.shape)
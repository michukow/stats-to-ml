import streamlit as st
import pandas as pd
from audytor import braki, duplikaty, ujemne, outliery, niespojny_zapis, daty_z_przyszlosci

st.title("Audyt danych")
st.write("Witaj w aplikacji do audytu danych! Wybierz plik CSV, aby rozpocząć analizę.")

plik = st.file_uploader("Wgraj plik CSV",type="csv")

if plik is not None:
    df=pd.read_csv(plik)
    k=st.slider("Próg outlierów", 1.5, 5.0, 3.0)
    st.write("Aktualne k:", k)

    kol1,kol2, kol3=st.columns(3)
    kol1.metric("Wiersze",len(df))
    kol2.metric("Kolumny",len(df.columns))
    kol3.metric("Duplikaty",duplikaty(df))

    st.subheader("Braki")
    b=braki(df)
    st.write(b[b>0])

    st.subheader("Wartości ujemne")
    st.write(ujemne(df))

    st.subheader("Outliery")
    st.write(outliery(df,k))

    st.subheader("Niespójny zapis")
    st.write(niespojny_zapis(df))

    st.subheader("Daty z przyszłości")
    st.write(daty_z_przyszlosci(df))

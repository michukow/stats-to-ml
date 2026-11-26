import re
import numpy as np
wagi=[1,3,7,9,1,3,7,9,1,3]

def pesel_poprawny(numer):
    cyfry=np.array(list(numer),dtype=int)
    suma=sum(cyfry[:10]*wagi)
    kontrolna=(10-suma%10)%10 
    return kontrolna==int(numer[10])

def znajdz_pesele(tekst):
    kandydaci=re.findall(r"\b\d{11}\b",tekst)
    return [k for k in kandydaci if pesel_poprawny(k)==True]

tekst = ("Klient Jan K., PESEL 44051401458, tel. 600 123 456, "
         "faktura nr 12345678901, zamówienie 02070803628.")

print("Kandydaci:",re.findall(r"\b\d{11}\b",tekst))
print("Prawdziwe PESEL-e:",znajdz_pesele(tekst))
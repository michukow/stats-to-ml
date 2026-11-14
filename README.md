# Od statystyki do ML

Moja ścieżka nauki od klasycznej ekonometrii do podstaw uczenia maszynowego. Każdą metodę najpierw wyprowadzam ręcznie (na tablecie), a potem implementuję od zera w NumPy i sprawdzam z profesjonalnymi bibliotekami (`statsmodels`, `scipy`).

Równolegle buduję narzędzia do **oceny jakości i wartości danych**: moduły A–E.

**Stan:** fazy 1–4 zamknięte, moduły A i B gotowe, w trakcie projekt „Ruch rowerowy w Krakowie a pogoda”.

## Najważniejsze projekty

### Audytor jakości danych (aplikacja Streamlit)
**Wersja online:** [audytor-danych.streamlit.app](https://audytor-danych.streamlit.app/)

`Audyt/app.py`: wgrywasz dowolny plik CSV, a aplikacja sama wykrywa:
- braki danych,
- zduplikowane wiersze,
- wartości ujemne w kolumnach liczbowych,
- outliery (reguła k·IQR, próg ustawiany suwakiem),
- niespójny zapis kategorii (wielkość liter, spacje),
- daty z przyszłości.

Na testowym zbiorze rolniczym (`Audyt/generuj_dane.py`) z celowo wprowadzonymi wadami audytor wykrywa wszystkie 6 rodzajów wad. Te same kontrole zrobione w SQL przez DuckDB (`Audyt/audyt_sql.py`) dają identyczne wyniki.

Uruchomienie lokalne:
```
cd Audyt
python -m streamlit run app.py
```

### Funkcja konsumpcji USA: dlaczego R² = 0,998 kłamało
Własna tabelka regresji (`regresja.py`: współczynniki, błędy standardowe, t, p, R²), zgodna ze `statsmodels` co do ostatniej cyfry, na kwartalnych danych makro USA 1959–2009.

| Model | R² | Durbin–Watson | Elastyczność konsumpcji | Stopa procentowa |
|---|---|---|---|---|
| Poziomy | 0,998 | 0,24 | 1,03 | „istotna” (p = 0,006) |
| Różnice | 0,20 | 1,89 | 0,34 [0,24; 0,43] | nieistotna (p = 0,24) |

W modelu w poziomach reszty są silnie autokorelowane (DW = 0,24), więc błędy standardowe są zaniżone, a istotność pozorna. Model w różnicach usuwa problem i pokazuje, że konsumpcja reaguje na kwartalny wzrost dochodu tylko w około 1/3, czyli ludzie wygładzają wydatki.

### Ruch rowerowy w Krakowie a pogoda (w trakcie)
Folder `rowery_krakow/`. Dane: dzienne pomiary z 20 automatycznych liczników rowerowych ZTP Kraków (listopad 2016 – październik 2026) połączone z dzienną pogodą.

- [x] pobieranie historycznej pogody dla Krakowa z API OpenMeteo (`pobierz_pogode.py`)
- [x] źródło danych o ruchu rowerowym: [ZTP Kraków – pomiary ruchu rowerowego](https://ztp.krakow.pl/rower/pomiary-ruchu-rowerowego/dane-tabelaryczne)
- [ ] wczytanie i audyt jakości danych z liczników
- [ ] połączenie z pogodą (uzupełnienie brakującej pogody za 2026 z OpenMeteo)
- [ ] wykresy eksploracyjne
- [ ] regresja: ruch ~ temperatura + opady + dzień tygodnia
- [ ] diagnostyka: autokorelacja, heteroskedastyczność, odporne SE
- [ ] porównanie trasy rekreacyjnej (Bulwary) z dojazdową (Mogilska)

## Faza 1: Metoda najmniejszych kwadratów
- Wyprowadzenie MNK z minimalizacji sumy kwadratów reszt, własności $\sum e_i = 0$ i $\sum x_i e_i = 0$.
- Zapis macierzowy $b = (X^TX)^{-1}X^Ty$, R² i skorygowane R².
- Symulacja Monte Carlo rozkładu $b_1$ (`monte_carlo.py`): rozrzut rośnie proporcjonalnie do σ i maleje jak $1/\sqrt{n}$.

![Histogram oszacowań b1](histogram.png)

## Faza 2: Zmienne losowe ciągłe
Gęstość $f(x) = x^2/9$ na $[0, 3]$:
- całkowanie numeryczne metodą punktu środkowego (`całka.py`), błąd maleje jak $1/N^2$,
- mediana metodą bisekcji: 22 iteracje dla tolerancji $10^{-6}$,
- losowanie metodą odwracania dystrybuanty (`mediana_rozklad.py`),
- wartość oczekiwana 2,25 i wariancja 0,3375, sprawdzone całką i próbą.

![Histogram próby i gęstość](histogram_gestosc.png)

## Faza 3: Wnioskowanie
- Nieobciążoność $b_1$ i wzór $SE(b_1) = \sigma / \sqrt{\sum (x_i - \bar x)^2}$, zweryfikowane symulacją (teoria 0,1255, Monte Carlo 0,1259).
- Test t i p-value (`test_t.py`), symulacja znaczenia p-value.
- Przedziały ufności.
- Test F (`test_F.py`): model konsumpcji istotny łącznie (F = 24,6), stopa procentowa sama nie (F = 1,37 = t²).

### Moduł A: audyt próbkowy
Jak oszacować odsetek wadliwych rekordów w dużym zbiorze bez sprawdzania wszystkich:
- przedział ufności dla odsetka (`Audyt/audyt_probkowy.py`),
- symulacja trafności: przedział „95%” trafia w 94,5% przypadków przy n = 400, ale tylko w 77,5% przy n = 50, bo w małej próbie często nie ma ani jednej wady,
- kalkulator wielkości próby (`Audyt/wielkosc_proby.py`): ±0,5 pp przy 4% wad wymaga 5901 rekordów.

## Faza 4: Diagnostyka
Każdy problem pokazany symulacją, w której znam prawdziwe parametry:

| Problem | Co się psuje | Wynik symulacji | Plik |
|---|---|---|---|
| Autokorelacja | SE zaniżone | DW = 0,24 w modelu konsumpcji, 1,89 po przejściu na różnice | `autokorelacja.py` |
| Heteroskedastyczność | SE zaniżone | prawdziwy rozrzut b₁ = 0,191, wzór daje 0,150 (−21%) | `heteroskedastycznosc.py` |
| ↳ naprawa: odporne SE White'a | | 0,181 (−5%) | `odporne_se.py` |
| ↳ wykrywanie: test White'a od zera | | LM = 19,96, p = 4,6·10⁻⁵, zgodne z `het_white` ze statsmodels | `test_white.py` |
| Współliniowość | SE zawyżone √VIF razy | VIF = 63 → rozrzut b₁ rośnie ok. 6 razy | `wspolliniowosc.py` |
| Zmienne pominięte | b obciążone | b₁ = 3,26 zamiast 2,00; wzór β₁ + β₂·δ przewiduje 3,256 | `zmienne_pominiete.py` |

Wniosek z fazy: autokorelacja, heteroskedastyczność i współliniowość psują **pewność** wyników (SE, t, p), ale nie same oszacowania. Zmienne pominięte psują **same oszacowania** i tego nie naprawią żadne odporne błędy standardowe.

## Plan

- [x] **Faza 1:** MNK: wyprowadzenie, zapis macierzowy, R², implementacja
- [x] **Faza 2:** zmienne ciągłe: gęstość, całkowanie numeryczne, mediana, wariancja, losowanie z rozkładu
- [x] **Faza 3:** wnioskowanie: SE, test t, przedziały ufności, test F
  - [x] **Moduł A: audyt próbkowy**
- [x] **Faza 4:** diagnostyka: autokorelacja, heteroskedastyczność, współliniowość, zmienne pominięte
  - [x] **Moduł B: audytor jakości danych** (pandas + Streamlit, wdrożony online, wersja SQL w DuckDB)
  - [ ] **Moduł C: wycena danych regresją.** Regresja hedoniczna ceny zbioru od jego cech
- [ ] **Projekt: ruch rowerowy w Krakowie a pogoda** (w trakcie)
- [ ] **Faza 5:** szeregi czasowe: stacjonarność, ADF, ARIMA, bootstrap reszt, prognozy Monte Carlo
- [ ] **Moduł D: wykrywanie danych osobowych.** PESEL, NIP, e-mail, telefon; potem nazwy własne w tekście
- [ ] **Faza 6:** wstęp do ML: funkcja straty, gradient descent, Ridge i Lasso, walidacja krzyżowa
  - [ ] **Moduł E: wartość danych dla modelu.** Krzywe uczenia, model z danym zbiorem i bez niego
- [ ] **Tor równoległy:** SQL (DuckDB), R jako kontrola wyników

## Wymagania

```
pip install numpy pandas scipy matplotlib statsmodels streamlit duckdb requests
```
import duckdb
plik="'C:/Users/micha/Desktop/Python/stats-to-ml/Audyt/dane_pola.csv'"
def zapytanie(sql):
    print(duckdb.sql(sql))

zapytanie(f"SELECT COUNT(*) AS wiersze FROM {plik}")
zapytanie(f"SELECT COUNT(*) AS braki_plon FROM {plik} WHERE plon_t_ha IS NULL")
zapytanie(f"SELECT COUNT(*) AS ujemne FROM {plik} WHERE powierzchnia_ha<0")
zapytanie(f"SELECT uprawa, COUNT(*) AS liczba FROM {plik} GROUP BY uprawa ORDER BY liczba ASC")
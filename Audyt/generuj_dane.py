import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 1000

df = pd.DataFrame({
    "id_pola": np.arange(1, N + 1),
    "uprawa": rng.choice(["pszenica", "kukurydza", "rzepak", "jęczmień"], N),
    "powierzchnia_ha": rng.normal(12, 4, N).round(2),
    "plon_t_ha": rng.normal(6, 1.2, N).round(2),
    "cena_zl_t": rng.normal(900, 120, N).round(0),
    "data_zbioru": pd.to_datetime("2024-07-01") + pd.to_timedelta(rng.integers(0, 90, N), unit="D"),
})

# Wady celowo wprowadzone (nie podglądaj, jeśli chcesz zgadywać!):
df.loc[rng.choice(N, 60, replace=False), "plon_t_ha"] = np.nan
df.loc[rng.choice(N, 25, replace=False), "cena_zl_t"] = np.nan
df.loc[rng.choice(N, 8, replace=False), "powierzchnia_ha"] *= -1
df.loc[rng.choice(N, 5, replace=False), "plon_t_ha"] = 95.0
df.loc[rng.choice(N, 4, replace=False), "data_zbioru"] = pd.Timestamp("2031-08-15")
df.loc[rng.choice(N, 6, replace=False), "uprawa"] = "Pszenica "
df = pd.concat([df, df.sample(15, random_state=1)], ignore_index=True)

df.to_csv("dane_pola.csv", index=False)
print(f"Zapisano dane_pola.csv: {len(df)} wierszy")
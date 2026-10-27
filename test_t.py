import numpy as np
from scipy import stats

b1=0.8
se=0.283
n=5

t=b1/se
stopnie_swobody=n-2
p=2*(1-stats.t.cdf(t,stopnie_swobody))

print(f"Wynik: {t}")
print(f"Wartość p: {p}")
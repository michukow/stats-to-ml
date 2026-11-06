import numpy as np

n_zbior=1000000
wady=0.03 #secret
n_probka=50
liczba_symulacji=2000
rng=np.random.default_rng(42)
zbior=rng.random(n_zbior)<wady
prawda=zbior.mean()
trafienia=0
for i in range(liczba_symulacji):
	probka=rng.choice(zbior,n_probka,replace=False)
	p=probka.mean()
	se=(p*(1-p)/n_probka)**(0.5)
	dolna=p-1.96*se
	gorna=p+1.96*se
	if prawda>dolna and prawda<gorna:
		trafienia+=1
print(f"n={n_probka}: przedział trafił w {trafienia/liczba_symulacji:.1%} przypadków")
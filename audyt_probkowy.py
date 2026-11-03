import numpy as np

n_zbior=1000000
wady=0.03 #secret
n_probka=400
rng=np.random.default_rng(42)
zbior=rng.random(n_zbior)<wady
probka=rng.choice(zbior,n_probka,replace=False)
p=probka.mean()
se=(p*(1-p)/n_probka)**(0.5)
dolna=p-1.96*se
gorna=p+1.96*se

print(f"Odsetek wad w próbie: {p:.2%}")
print(f"95% przedział: [{dolna:.2%}, {gorna:.2%}]")
print(f"Prawdziwy odsetek w zbiorze: {zbior.mean():.2%}")
import numpy as np

N_OBS=100
N_SYM=2000
rng=np.random.default_rng(42)

x1=rng.normal(0,1,N_OBS)

def symulacja(x1,x2):
    X=np.column_stack([np.ones(N_OBS),x1,x2])
    wyniki=np.zeros((N_SYM,3))
    for i in range(N_SYM):
        y=1+2*x1+3*x2+rng.normal(0,1,N_OBS)
        wyniki[i]=np.linalg.lstsq(X,y,rcond=None)[0]
    return wyniki

for szum_x2 in [1.0,0.1]:
    x2=x1+rng.normal(0,szum_x2, N_OBS)
    r=np.corrcoef(x1,x2)[0,1]
    vif=1/(1-r**2)
    wyniki=symulacja(x1,x2)
    print(f"r={r.round(3)}, VIF={vif.round(3)}")
    print(f"Średnie b: {wyniki.mean(axis=0).round(3)}")
    print(f"Rozrzut b: {wyniki.std(axis=0).round(3)}")
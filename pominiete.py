import numpy as np

N_OBS=200
N_SYM=2000
rng=np.random.default_rng(42)

x1=rng.normal(0,1,N_OBS)
x2=0.5*x1+rng.normal(0,1,N_OBS)

X_pelny=np.column_stack([np.ones(N_OBS),x1,x2])
X_krotki=np.column_stack([np.ones(N_OBS),x1])

b1_pelny=np.zeros(N_SYM)
b1_krotki=np.zeros(N_SYM)
for i in range(N_SYM):
    y=1+2*x1 +3*x2+rng.normal(0,2,N_OBS)
    b1_pelny[i]=np.linalg.lstsq(X_pelny,y,rcond=None)[0][1]
    b1_krotki[i]=np.linalg.lstsq(X_krotki,y,rcond=None)[0][1]

delta=np.polyfit(x1,x2,1)[0]
print(f"Pełny model: b1 = {b1_pelny.mean():.3f}")
print(f"Bez x2: b1 = {b1_krotki.mean():.3f}")
print(f"Ze wzoru: b1 = {2+3*delta:.3f}")
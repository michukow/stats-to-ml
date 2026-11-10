import numpy as np
import matplotlib.pyplot as plt

N_OBS=100
N_SYM=2000
rng=np.random.default_rng(42)
x=rng.uniform(0,10,N_OBS)
x_odch=x-x.mean()
SS_x=(x_odch**2).sum()

def szum(x):
    return rng.normal(0,0.1*x**2)

#PART 1
y=np.array(1+2*x+szum(x))
X=np.column_stack([np.ones(N_OBS),x])
Xtx=X.T@X
Xty=X.T@y
b=np.linalg.inv(Xtx) @ Xty
b0,b1=b
e=y-X@b
plt.scatter(x,e)
plt.axhline(0,color="black")
plt.xlabel("x")
plt.ylabel("reszta")
plt.show()

#PART 2
wyniki_b1=np.zeros(N_SYM)
wyniki_se=np.zeros(N_SYM)
for i in range(N_SYM):
    y=1+2*x+szum(x)
    Xty=X.T@y
    b=np.linalg.inv(Xtx)@Xty
    b0,b1=b
    e=y-X@b
    s2=(e**2).sum()/(N_OBS-2)
    wyniki_b1[i]=b1
    wyniki_se[i]=np.sqrt(s2/SS_x)

print(f"Średnia b1: {wyniki_b1.mean():.3f}")
print(f"Prawdziwy rozrzut b1: {wyniki_b1.std():.3f}")
print(f"Średnie SE ze wzoru: {wyniki_se.mean():.3f}")
import numpy as np
x=np.array([1, 2, 3, 4, 5])
y=np.array([2, 4, 5, 4, 6])
X=np.column_stack((np.ones(5),x))
print(X)
print(X.shape)
Xtx=X.T@X
print(Xtx)
Xty=X.T@y
print(X.T@y)
b=np.linalg.inv(Xtx)@Xty
print(f'b= {b}')
print("----------------------")
y_hat=X@b
e=y-y_hat
print(X.T@e)
SS_calk=(y-y.mean())**2
SS_wyj=(y_hat-y.mean())**2
SS_re=(e**2)
R2=SS_wyj.sum()/SS_calk.sum()
print(R2)
n=len(y)
k=X.shape[1]-1
R2_adj=1-((SS_re.sum()*(n-1))/(SS_calk.sum()*(n-k-1)))
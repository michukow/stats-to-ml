import numpy as np
x=np.array([1, 2, 3, 4, 5])
y=np.array([2, 4, 5, 4, 6])
x_diff=x-x.mean()
w=x_diff/(x_diff**2).sum()
print(f"Sprawdzanie: {(w**2).sum()})
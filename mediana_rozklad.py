import numpy as np
import matplotlib.pyplot as plt
rng=np.random.default_rng(42)
u=rng.uniform(0,1,10000)
x=3*u**(1/3)
print(x)
print(f"Mediana: {np.median(x)}") 
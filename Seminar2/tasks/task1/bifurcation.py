import matplotlib.pyplot as plt
import numpy as np

def logistic_map_step(x, r):
    return r * x * (1 - x)

N = 1000
M = 500
L = 2000
rhs = 2.0000
rh = 0.001

p = np.empty(N)

r_start = rhs
r = np.linspace(r_start, r_start, N)

p[0] = 0.2

for j in range(L):
    r = np.linspace(r_start, r_start, N)
    for i in range(0, len(p)-1):
        p[i+1] = logistic_map_step(p[i], r[i])

    plt.plot(r[M:], p[M:], ',', color='k')
    r_start+=rh

plt.xlabel("r")
plt.ylabel("points")
plt.show()

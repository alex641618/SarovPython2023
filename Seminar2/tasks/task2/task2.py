import matplotlib.pyplot as plt
from numba import njit
import numpy as np
import imageio

@njit
def check(Rez0, Imz0, max_iter, threshold, ReC, ImC):
	
	Rez_d = np.empty(max_iter + 1, dtype=np.double)
	Imz_d = np.empty(max_iter + 1, dtype=np.double)

	Imz_d[0] = Imz0
	Rez_d[0] = Rez0

	for i in range(1, max_iter):
			Rez_d[i] = Rez_d[i-1]**2-Imz_d[i-1]**2 + ReC
			Imz_d[i] = 2*Rez_d[i-1]*Imz_d[i-1] + ImC
			absv = np.sqrt(Rez_d[i]**2+Imz_d[i]**2)
			if (absv > threshold):
				return i
			
	return max_iter

@njit
def get_it(max_iter, threshold, ReC, ImC):
	it = np.empty((N,N), dtype=np.intc)

	for k in range(N):
		for j in range(N):
			it[k,j] = check(Rez[j], Imz[k], max_iter, threshold, ReC, ImC)

	return it

@njit
def create_fractal(max_iter, threshold, ReC, ImC, frames, N):

	it = np.empty((frames, N, N), dtype=np.intc)

	for i in range(frames):
		it[i] = get_it(max_iter, threshold, ReC[i], ImC[i])

	return it


N = 1024
frames = 100

Imz_max = 2
Imz_min = -2
Rez_max = 2
Rez_min = -2

max_iter = 20
threshold = 8

ReC_phase = 0
ImC_phase = 0

ReC_ampl = 1
ImC_ampl = 1

Imz = np.linspace(Imz_min, Imz_max, N, dtype=np.double)
Rez = np.linspace(Rez_min, Rez_max, N, dtype=np.double)

a = np.linspace(0, 2*np.pi, frames)
ReC = ReC_ampl*np.cos(a + ReC_phase)
ImC = ImC_ampl*np.sin(a + ImC_phase) 

it = create_fractal(max_iter, threshold, ReC, ImC, frames, N)

imageio.mimsave('movie.gif', np.ndarray.tolist(it*int(255/max_iter)), duration=1, loop=0)
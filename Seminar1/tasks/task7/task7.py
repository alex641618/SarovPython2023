import matplotlib.pyplot as plt
import numpy as np

class EyeMatrix:

	def __init__(self, n = 10):
		self.matrix = np.eye(n)

	def draw(self):
		plt.imshow(self.matrix, extent = (0, 1, 0, 1))
		plt.show()

	def zeros(self):
		self.matrix *= 0

	def print(self):
		print(f'trace = {np.trace(self.matrix)}')


print('item 1, 2:')
e1 = EyeMatrix()
print('matrix 1:')
print(e1.matrix)

print('item 3:')
print('drawing matrix 1...')
e1.draw()

print('item 4:')
e1.zeros()
print('writing zeros in matrix 1...')
print('redrawing matrix 1...')
e1.draw()

print('item 5:')
e2 = EyeMatrix()
print('matrix 2:')
print(e2.matrix)
print('printing trace of matrix 2...')
e2.print()

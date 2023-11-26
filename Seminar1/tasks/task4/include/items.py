import matplotlib.pyplot as plt
import random as r
import numpy as np
import pickle
import math
import cv2

#item 1
def random_matrix_generator(ntuple):
    ndarray = np.random.sample(ntuple)    
    return ndarray.astype(np.single)

#item 2
def get_max(arg_ndarray):
    return arg_ndarray.max()

#item 3
def create_matrix_im(arg_ndarray, flag):
    N = len(arg_ndarray)
    ax = plt.imshow(arg_ndarray, cmap = 'hot', extent = (0, N, 0, N))
    plt.colorbar()
    i, j = np.unravel_index(arg_ndarray.argmax(), arg_ndarray.shape)
    if (flag):
        plt.scatter(j + 0.5, N - i - 0.5, s = 100, c = 'b', marker = '.')
    return ax

#item 4
def update_matrix_im(ax):
    plt.xlabel('x', fontsize = 12)
    plt.ylabel('y', fontsize = 12)
    plt.scatter(plt.xlim()[1]/2, plt.ylim()[1]/5, c = 'g', marker = 'x')
    return ax

#item 5
def cut_circle(arg_ndarray):
    ndarray = arg_ndarray.copy()
    N = len(ndarray)
    cv2.circle(ndarray,(int(N/2+0.5), int(N/2+0.5)),int(N/4),(0,0,0),-1)

    return ndarray


def show_plot(ax):
    temp = pickle.dumps(ax)
    plt.show()
    ax = pickle.loads(temp)
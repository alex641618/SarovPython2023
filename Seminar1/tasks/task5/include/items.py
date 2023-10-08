import matplotlib.pyplot as plt
import numpy as np
import pickle

#item 1
def draw_yt(t, y):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title('signal')
    plt.plot(t, y, label = 'signal')
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('y', fontsize = 12)

    return fig

def create_t():
    grid_min = -20 * 2 * np.pi
    grid_max = 20 * 2 * np.pi

    return np.linspace(grid_min, grid_max, 4*1024)

def create_y(t):
    duration = 5 * np.pi

    return np.exp(-t**2/2/duration**2) * np.sin(t)

#item 2
def draw_spectr(w, s, fig):  
    fig.axes[0].set_position([0.125, 0.535, 0.775, 0.375])
    fig.add_subplot(2, 1, 2)
    fig.axes[1].set_title('signal spectrum')
    plt.plot(w, s, label = "signal spectrum")
    plt.xlabel('w', fontsize = 12)
    plt.ylabel('s', fontsize = 12)

def create_w(t):
    N = len(t)
    dw = (2*np.pi)/(N*(t[1]-t[0]))

    return np.arange(-N/2 * dw, N/2 * dw, dw)

def create_spectr(y):
    N = len(y)
    Norm = (N/2)**2

    return np.fft.fftshift((np.absolute(np.fft.fft(y)))**2)/Norm

def show_figure(fig):
    temp = pickle.dumps(fig)
    fig.show()
    plt.pause(0)
    figr = pickle.loads(temp)

    return figr
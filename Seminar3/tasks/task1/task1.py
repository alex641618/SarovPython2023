import matplotlib.pyplot as plt
import numpy as np

def create_t(Nt):
    grid_min = -20 * 2 * np.pi
    grid_max = 20 * 2 * np.pi

    return np.linspace(grid_min, grid_max, Nt)

def create_y(t):
    duration = 5 * np.pi

    return np.exp(-(t+20)**2/2/duration**2) * np.sin(20*t) + np.exp(-(t-20)**2/2/(duration/2)**2) * np.cos(10*t)

def draw_yt(t, y):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    ax.set_title('signal')
    plt.plot(t, y, label = 'signal')
    plt.xlabel('t', fontsize = 12)
    plt.ylabel('y', fontsize = 12)

    return fig

def create_w(t):
    N = len(t)
    dw = (2*np.pi)/(N*(t[1]-t[0]))

    return np.arange(-N/2 * dw, N/2 * dw, dw)

def create_spectr(y):
    N = len(y)
    Norm = (N/2)**2

    return np.fft.fftshift((np.absolute(np.fft.fft(y)))**2)/Norm

def draw_spectr(w, s, fig):  
    fig.axes[0].set_position([0.125, 0.535, 0.775, 0.375])
    fig.add_subplot(2, 1, 2)
    fig.axes[1].set_title('signal spectrum')
    plt.plot(w, s, label = "signal spectrum")
    plt.xlabel('w', fontsize = 12)
    plt.ylabel('s', fontsize = 12)

def create_spectrogram(y, window_width, t, w):
	
	window_position = t
	spectrgramm = np.zeros((len(w),len(t)))

	for i in range(len(t)):	
		window_function = np.exp(-(t[i]-window_position)**2/2/window_width**2)
		spectrgramm[i] = create_spectr(y*window_function)

	return spectrgramm.T

def draw_spectrogram(t, w, spectrogram):
	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)

	ax.set_title('spectrogram')
	plt.imshow(spectrogram[:int(len(w)/2)], extent=[t[0],t[len(t)-1],0,w[len(w)-1]])
	
	w_ticks = np.empty(10)
	x_ticks = np.empty(10)

	plt.xlabel('t', fontsize = 12)
	plt.ylabel('w', fontsize = 12)

	return fig

Nt = 4*1024
t = create_t(Nt)
y = create_y(t)

window_width=1.0*np.pi

print('drawing signal...')
draw_yt(t, y)
plt.show()

print('drawing spectrogram...')
w = create_w(t)
spectrogram = create_spectrogram(y, window_width, t, w)
draw_spectrogram(t, w, spectrogram)
plt.show()

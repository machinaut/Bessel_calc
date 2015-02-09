#!/usr/bin/env python
# science.py - use SciPy to draw Bessel Filters

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

plt.xlim(10,1000)
b, a = signal.butter(4, (140,160), 'bandpass', analog=True)
w, h = signal.freqs(b, a)
plt.plot(w, 20 * np.log10(np.abs(h)), color='silver', ls='dashed')
b, a = signal.bessel(4, (140,160), 'bandpass', analog=True)
w, h = signal.freqs(b, a)
plt.semilogx(w, 20 * np.log10(np.abs(h)))
plt.title('Bessel filter frequency response (with Butterworth)')
plt.xlabel('Frequency [radians / second]')
plt.ylabel('Amplitude [dB]')
plt.margins(0, .1)
plt.grid(which='both', axis='both')
plt.show()

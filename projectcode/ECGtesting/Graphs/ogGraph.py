#########Plot of 1 signal/category########
import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import signal
from scipy import fft #fast fourier transform
import numpy as np
import itertools
from scipy.signal import butter, lfilter
import scipy.io

###################################Load data: Normal/Schizophrenia EEG###########################
def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut /nyq
    high = highcut/nyq
    b, a = butter(order, [low, high], btype='band')
    #print(b,a)
    y = lfilter(b, a, data)
    return y

x1 = []
x2 = []


mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/100m (0).mat')
x1.append(mat['val'])
x1 = np.array(x1)

print(x1)


mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/4 AFIB/201m (4).mat')
x2.append(mat['val'])
x2 = np.array(x2)


s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For normal signal (x1)
s3 = np.empty([0]) # For AFIB signal (x2)


fs = 360
time = 10

start = 0
#stop = fs + (4097-fs) + 1
stop = 10
sub1 = np.arange(start, stop, 10/3600)
sub2 = x1 + np.random.randn(len(sub1))
sub3 = x2 + np.random.randn(len(sub1))


s1 = np.append(s1, sub1)
s2 = np.append(s2, sub2)
s3 = np.append(s3, sub3)


plt.subplot(211)
plt.plot(s1,s2)
plt.ylabel(u'Amplitude(\u03bcV)')
plt.xlabel('Time(s)')


plt.subplot(212)
plt.plot(s1,s3)
plt.ylabel(u'Amplitude(\u03bcV)')
plt.xlabel('Time(s)')


plt.tight_layout()
plt.show()

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

def butter_lowpass(data, cutoff, sample_rate, order=2):
    nyq = 0.5 * sample_rate
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, data)
    return y



x1 = []


mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/100m (0).mat')
x1.append(mat['val'])
x1 = np.array(x1)

fs = 360
time = 10
cutoff_low = 50 #get the ECG from 0.05Hz up to 150Hz
cutoff_high = 0.05
order = 2

#x2 = filtered signal
x2 = butter_bandpass_filter(x1, cutoff_high, cutoff_low, fs, order)
#x2 = butter_lowpass(x1, cutoff_high, fs, order)

s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For original(raw) signal (x1)
s3 = np.empty([0]) # For filtered signal (x2)


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



plt.plot(s1,s2)
plt.plot(s1,s3)
plt.legend(["Raw ECG signal", "Filtered ECG signal"])
plt.ylabel(u'Amplitude(\u03bcV)')
plt.xlabel('Time(s)')


#plt.tight_layout()
plt.show()

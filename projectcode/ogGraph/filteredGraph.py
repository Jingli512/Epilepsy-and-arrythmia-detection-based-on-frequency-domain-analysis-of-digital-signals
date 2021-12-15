#########Plot of 1 signal/category########
import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import signal
from scipy import fft #fast fourier transform
import numpy as np
import itertools
from scipy.signal import butter, lfilter

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

with open('/Users/jingli/Desktop/EpEEG/Z/Z001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))

x1 = np.array(x1)

fs = 173.61
time = 23.6
cutoff_low = 60 #get the EEG from 0.1Hz up to 60Hz
cutoff_high = 0.1
order = 2
#x2 = filtered signal
x2 = butter_bandpass_filter(x1, cutoff_high, cutoff_low, fs, order)

s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For original signal
s3 = np.empty([0]) # For filtered signal


start = 0
#stop = fs + (4097-fs) + 1
stop = 23.6
sub1 = np.arange(start, stop, 23.6/4097)
sub2 = x1 + np.random.randn(len(sub1))
sub3 = x2 + np.random.randn(len(sub1))


s1 = np.append(s1, sub1)
s2 = np.append(s2, sub2)
s3 = np.append(s3, sub3)



plt.plot(s1,s2)

plt.plot(s1,s3)
plt.legend(["Raw EEG signal", "Filtered EEG signal"])
plt.xlabel('Time(s)')
plt.ylabel(u'Amplitude(\u03bcV)')



#plt.tight_layout()
plt.show()

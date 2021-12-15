import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import signal
from scipy import fft #fast fourier transform
import itertools
from scipy.signal import butter, lfilter

###########################Function For Filtering Raw signal##################################
def butter_bandpass_filter(data, lowcut, highcut, fs, order=2):
    nyq = 0.5 * fs
    low = lowcut /nyq
    high = highcut/nyq
    b, a = butter(order, [low, high], btype='band')
    #print(b,a)
    y = lfilter(b, a, data)
    return y

x = []
with open('/Users/jingli/Desktop/EpEEG/Z/Z001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))

out = np.array(x)

fs = 173.61
cutoff_low = 70
cutoff_high = 0.1
order = 2

#########Filter the data########
filteredOut = butter_bandpass_filter(out, cutoff_high, cutoff_low, fs, order)

s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal

start = 1
stop = 4097 + 1

sub1 = np.arange(start, stop, 1)
sub2 = filteredOut + np.random.randn(len(sub1))

s1 = np.append(s1, sub1)

s2 = np.append(s2, sub2)


plt.subplot(211)

plt.plot(s1,s2)

plt.xlabel('Sample')

plt.ylabel('Amplitude')




# Plot the spectrogram

plt.subplot(212)

powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(s2, Fs=fs)
plt.colorbar()
plt.xlabel('Time in s')
plt.ylabel('Frequency in Hz')
#plt.tight_layout()
plt.show()

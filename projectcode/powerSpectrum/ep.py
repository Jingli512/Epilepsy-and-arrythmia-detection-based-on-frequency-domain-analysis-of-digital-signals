#########Power spectrum plot for normal/schizophrenia EEG signals##############
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

x = []

with open('/Users/jingli/Desktop/EpEEG/S/S001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))

out = np.array(x)

#mean = np.mean(out)
#print(mean)

fs = 173.61
cutoff_low = 60 #get the EEG from 0.1Hz up to 60Hz
cutoff_high = 0.1
order = 2

#########Filter the data########
filteredOut = butter_bandpass_filter(out, cutoff_high, cutoff_low, fs, order)


s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal

start = 1
stop = fs + (4097-fs) + 1

sub1 = np.arange(start, stop, 1)
sub2 = filteredOut + np.random.randn(len(sub1))

s1 = np.append(s1, sub1)

s2 = np.append(s2, sub2)


plt.subplot(211)
plt.plot(s1,s2)
plt.title('Epilepsy Signal(Filtered)')
plt.xlabel('Sample')
plt.ylabel(u'Amplitude in \u03bcV')

time = np.arange(0,23.6) # 8s对应1024个sample
#fourier_transform = np.fft.rfft(out)
fourier_transform = np.fft.rfft(filteredOut)

abs_fourier_transform = np.abs(fourier_transform)

power_spectrum = np.square(abs_fourier_transform)

frequency = np.linspace(0, 60, len(power_spectrum)) #250
#frequency = np.linspace(0, fs/2, len(power_spectrum))
plt.subplot(212)
plt.plot(frequency, power_spectrum)
plt.title('Power Spectrum')
plt.xlabel('Frequency in Hz')
plt.ylabel(u'Power spectral density in \u03bcV^2/Hz')

plt.tight_layout()
plt.show()

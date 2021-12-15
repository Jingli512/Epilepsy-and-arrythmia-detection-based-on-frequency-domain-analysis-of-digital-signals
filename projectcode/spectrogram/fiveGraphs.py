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

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []

with open('/Users/jingli/Desktop/EpEEG/Z/Z001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))

x1 = np.array(x1)

with open('/Users/jingli/Desktop/EpEEG/O/O001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(float(row[0]))

x2 = np.array(x2)

with open('/Users/jingli/Desktop/EpEEG/N/N001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append(float(row[0]))

x3 = np.array(x3)

with open('/Users/jingli/Desktop/EpEEG/F/F001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x4.append(float(row[0]))

x4 = np.array(x4)

with open('/Users/jingli/Desktop/EpEEG/S/S001.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x5.append(float(row[0]))

x5 = np.array(x5)


#mean = np.mean(out)
#print(mean)

fs = 173.61
cutoff_low = 60 #get the EEG from 0.1Hz up to 60Hz
cutoff_high = 0.1
order = 2

#########Filter the data########
filteredOut1 = butter_bandpass_filter(x1, cutoff_high, cutoff_low, fs, order)
filteredOut2 = butter_bandpass_filter(x2, cutoff_high, cutoff_low, fs, order)
filteredOut3 = butter_bandpass_filter(x3, cutoff_high, cutoff_low, fs, order)
filteredOut4 = butter_bandpass_filter(x4, cutoff_high, cutoff_low, fs, order)
filteredOut5 = butter_bandpass_filter(x5, cutoff_high, cutoff_low, fs, order)


s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal Z
s3 = np.empty([0]) # For signal O
s4 = np.empty([0]) # For signal N
s5 = np.empty([0]) # For signal F
s6 = np.empty([0]) # For signal S

start = 1
stop = fs + (4097-fs) + 1

sub1 = np.arange(start, stop, 1)
sub2 = filteredOut1 + np.random.randn(len(sub1))
sub3 = filteredOut2 + np.random.randn(len(sub1))
sub4 = filteredOut3 + np.random.randn(len(sub1))
sub5 = filteredOut4 + np.random.randn(len(sub1))
sub6 = filteredOut5 + np.random.randn(len(sub1))

s1 = np.append(s1, sub1)
s2 = np.append(s2, sub2)
s3 = np.append(s3, sub3)
s4 = np.append(s4, sub4)
s5 = np.append(s5, sub5)
s6 = np.append(s6, sub6)




# Plot the spectrogram

plt.subplot(511)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(s2, Fs=fs)
plt.colorbar()

plt.subplot(512)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(s3, Fs=fs)
plt.colorbar()

plt.subplot(513)
plt.ylabel('Frequency in Hz')
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(s4, Fs=fs)
plt.colorbar()

plt.subplot(514)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(s5, Fs=fs)
plt.colorbar()

plt.subplot(515)
powerSpectrum, freqenciesFound, time, imageAxis = plt.specgram(s6, Fs=fs)
plt.colorbar()


plt.xlabel('Time in s')
#plt.ylabel('Frequency in Hz')
plt.tight_layout()
plt.show()

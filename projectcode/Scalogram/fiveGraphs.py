import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import signal
from scipy import fft #fast fourier transform
import itertools
from scipy.signal import butter, lfilter
import pywt
import pywt.data

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





# Plot the scalogram
scales = np.arange(1, 32)
coef, freq = pywt.cwt(filteredOut1, scales, 'gaus1')

#plt.figure(figsize=(15,10))
plt.subplot(511)
plt.imshow(abs(coef), extent = [0, 24, 30, 1], interpolation = 'bilinear', cmap = 'bone', aspect = 'auto', vmax = abs(coef).max(), vmin = -abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 32, 4))
plt.xticks(np.arange(0, 24, 1))#8s-1024  960s-122880


coef, freq = pywt.cwt(filteredOut2, scales, 'gaus1')
plt.subplot(512)
plt.imshow(abs(coef), extent = [0, 24, 30, 1], interpolation = 'bilinear', cmap = 'bone', aspect = 'auto', vmax = abs(coef).max(), vmin = -abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 32, 4))
plt.xticks(np.arange(0, 24, 1))#8s-1024  960s-122880


coef, freq = pywt.cwt(filteredOut3, scales, 'gaus1')
plt.subplot(513)
plt.imshow(abs(coef), extent = [0, 24, 30, 1], interpolation = 'bilinear', cmap = 'bone', aspect = 'auto', vmax = abs(coef).max(), vmin = -abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 32, 4))
plt.xticks(np.arange(0, 24, 1))#8s-1024  960s-122880
plt.ylabel('Scales a')

coef, freq = pywt.cwt(filteredOut4, scales, 'gaus1')
plt.subplot(514)
plt.imshow(abs(coef), extent = [0, 24, 30, 1], interpolation = 'bilinear', cmap = 'bone', aspect = 'auto', vmax = abs(coef).max(), vmin = -abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 32, 4))
plt.xticks(np.arange(0, 24, 1))#8s-1024  960s-122880


coef, freq = pywt.cwt(filteredOut5, scales, 'gaus1')
plt.subplot(515)
plt.imshow(abs(coef), extent = [0, 24, 30, 1], interpolation = 'bilinear', cmap = 'bone', aspect = 'auto', vmax = abs(coef).max(), vmin = -abs(coef).max())
plt.gca().invert_yaxis()
plt.yticks(np.arange(1, 32, 4))
plt.xticks(np.arange(0, 24, 1))#8s-1024  960s-122880
plt.xlabel('Time in s')

plt.tight_layout()
plt.show()

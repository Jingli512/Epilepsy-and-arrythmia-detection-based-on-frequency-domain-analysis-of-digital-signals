#This program draws the original graphs of the EEG signals from all categories
#One graph/category and therefore 5 graohs in total

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


s1 = np.empty([0]) # For samples
s2 = np.empty([0]) # For signal Z
s3 = np.empty([0]) # For signal O
s4 = np.empty([0]) # For signal N
s5 = np.empty([0]) # For signal F
s6 = np.empty([0]) # For signal S

fs = 173.61
time = 23.6

start = 0
#stop = fs + (4097-fs) + 1
stop = 23.6
sub1 = np.arange(start, stop, 23.6/4097)
sub2 = x1 + np.random.randn(len(sub1))
sub3 = x2 + np.random.randn(len(sub1))
sub4 = x3 + np.random.randn(len(sub1))
sub5 = x4 + np.random.randn(len(sub1))
sub6 = x5 + np.random.randn(len(sub1))

s1 = np.append(s1, sub1)
s2 = np.append(s2, sub2)
s3 = np.append(s3, sub3)
s4 = np.append(s4, sub4)
s5 = np.append(s5, sub5)
s6 = np.append(s6, sub6)


plt.subplot(511)
plt.plot(s1,s2)


plt.subplot(512)
plt.plot(s1,s3)


plt.subplot(513)
plt.plot(s1,s4)

plt.ylabel(u'Amplitude(\u03bcV)')

plt.subplot(514)
plt.plot(s1,s5)

plt.subplot(515)
plt.plot(s1,s6)
plt.xlabel('Time(s)')


plt.tight_layout()
plt.show()

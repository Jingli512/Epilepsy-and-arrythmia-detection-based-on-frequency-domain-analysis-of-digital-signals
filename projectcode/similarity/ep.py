import csv
import numpy as np
from scipy import signal, fft
import itertools
import math
from scipy.linalg import norm
from scipy.spatial.distance import euclidean

##########################Hellinger Distance Function###################
_SQRT2 = np.sqrt(2)
def hellinger1(p, q):
    return norm(np.sqrt(p) - np.sqrt(q)) / _SQRT2

def hellinger2(p, q):
    return euclidean(np.sqrt(p), np.sqrt(q)) / _SQRT2

def hellinger3(p, q):
    return np.sqrt(np.sum((np.sqrt(p) - np.sqrt(q)) ** 2)) / _SQRT2

###########################################################################


#########################Templates###################
x= []

########Z001 to Z009######
for i in range(1, 10):
    with open('/Users/jingli/Desktop/EpEEG/Z/Z00'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

########Z010 to Z050#######
for i in range(10, 51):
    with open('/Users/jingli/Desktop/EpEEG/Z/Z0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

out = np.array(x)
out = out.reshape(-1, 4097)
out = out*0.000001
###########################################################################

##################################Testing Signal###########################
test = []
with open('/Users/jingli/Desktop/EpEEG/S/S005.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        test.append(float(row[0]))

#print(test)
test = np.array(test)
test = test*0.000001

###########################################################################

##################################Calculate similarity score###########################
score = []

#The power_spectrum of the testing signal

for i in range(0, 50):

    fourier_transform = np.fft.rfft(out[i])
    abs_fourier_transform = np.abs(fourier_transform)
    power_spectrum = np.square(abs_fourier_transform)

    fourier_transform1 = np.fft.rfft(test)
    abs_fourier_transform1 = np.abs(fourier_transform1)
    power_spectrum1 = np.square(abs_fourier_transform1)

    hellinger = hellinger3(power_spectrum, power_spectrum1)
    score.append(1/hellinger)

score = np.array(score)
max = np.max(score)
print('Normal Score:')
print(max)

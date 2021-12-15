import csv
import numpy as np
from scipy import signal, fft
import itertools
import math
from scipy.linalg import norm
from scipy.spatial.distance import euclidean
import scipy.io

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

########100m (0)-(9)######
########101m (0)-(9)######
########103m (0)-(9)######
########105m (0)-(9)######
########106m (0)-(9)######
for i in range(0, 10):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/100m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 10):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/101m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 10):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/103m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 10):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/105m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 10):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/106m (' + str(i)+ ').mat')
    x.append(mat['val'])


out = np.array(x)
out = out.reshape(-1, 3600)
out = out*0.000001
###########################################################################

##################################Testing Signal###########################
test = []
########106m (10)-(18)###### Amount: 9
########108m (0)-(20)###### Amount: 21
########112m (0)-(17)###### Amount: 18
########113m (0)-(1)###### Amount: 2
for i in range(10, 19):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/106m (' + str(i)+ ').mat')
    test.append(mat['val'])

for i in range(0, 21):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/108m (' + str(i)+ ').mat')
    test.append(mat['val'])

for i in range(0, 18):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/112m (' + str(i)+ ').mat')
    test.append(mat['val'])

for i in range(0, 2):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/1 NSR/113m (' + str(i)+ ').mat')
    test.append(mat['val'])

#print(test)
test = np.array(test)
test = test*0.000001
test = test.reshape(-1, 3600)

###########################################################################

##################################Calculate similarity score###########################
scoretemp = []
score = []
#The power_spectrum of the testing signal

for i in range(0, 50):
    for ii in range(0, 50):
        fourier_transform = np.fft.rfft(out[ii]) #template
        abs_fourier_transform = np.abs(fourier_transform)
        power_spectrum = np.square(abs_fourier_transform)

        fourier_transform1 = np.fft.rfft(test[i]) #testing signals
        abs_fourier_transform1 = np.abs(fourier_transform1)
        power_spectrum1 = np.square(abs_fourier_transform1)

        hellinger = hellinger3(power_spectrum, power_spectrum1)
        scoretemp.append(1/hellinger)

scoretemp = np.array(scoretemp)
scoretemp = scoretemp.reshape(-1, 50)

for i in range(0, 50):
    score.append(np.max(scoretemp[i]))

print(score)
score = np.array(score)
mean = np.mean(score)
median = np.median(score)
min = np.min(score)
print('Mean: ', mean)
print('Median: ', median)
print('Minimum: ', min)

'''
Mean:  11.582514273735669
Median:  12.417695829911814
Minimum:  3.4607077409566305
'''

#score = np.array(score)
#max = np.max(score)
#print('Normal Score:')
#print(max)

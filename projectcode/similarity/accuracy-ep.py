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

'''
for i in range(1, 10):
    with open('/Users/jingli/Desktop/EpEEG/S/S00'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            test.append(float(row[0]))

for i in range(10, 51):
    with open('/Users/jingli/Desktop/EpEEG/S/S0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            test.append(float(row[0]))

'''

for i in range(51, 100):
    with open('/Users/jingli/Desktop/EpEEG/S/S0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            test.append(float(row[0]))

with open('/Users/jingli/Desktop/EpEEG/S/S100.txt','r') as csvfile:

    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        test.append(float(row[0]))
#print(test)
test = np.array(test)
test = test*0.000001
test = test.reshape(-1, 4097)

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

count = 0
threshold = 14

for j in range(0, 50):
    if score[j] < threshold:
        count = count+1
print(count)
accuracy = count/50
print(accuracy)

#Mean:  19.308604092679953
#Median:  18.851810122796127
#Minimum:  14.611060443466808


#score = np.array(score)
#max = np.max(score)
#print('Normal Score:')
#print(max)

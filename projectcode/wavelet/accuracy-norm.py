#A program to test the accuracy of the ApEn method
'''
Mean of D1s 1.8585500122447973
Minimum value of D1s 1.695602197625277
Median value of D1s 1.8611019359046947
'''
import matplotlib.pyplot as plt
import csv
import numpy as np
import pywt
import pywt.data
from scipy import io
from numpy import random

######Functions for finding approximate entropy(ApEn)#######
def ApEn(U, m, r):

    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0) for x_i in x]
        return (N - m + 1.0)**(-1) * sum(np.log(C))

    N = len(U)

    return abs(_phi(m + 1) - _phi(m))

def ApEn_new(U, m, r):
    U = np.array(U)
    N = U.shape[0]

    def _phi(m):
        z = N - m + 1.0
        x = np.array([U[i:i+m] for i in range(int(z))])
        X = np.repeat(x[:, np.newaxis], 1, axis=2)
        C = np.sum(np.absolute(x - X).max(axis=2) <= r, axis=0) / z
        return np.log(C).sum() / z

    return abs(_phi(m + 1) - _phi(m))
###############################################


x= []

#Z- eyes open
#O- eyes closed

########Z001 to Z009######
for i in range(1, 10):
    with open('/Users/jingli/Desktop/EpEEG/O/O00'+ str(i) +'.txt','r') as csvfile:
    #with open('/Users/jingli/Desktop/EpEEG/Z/Z00'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

########Z010 to Z050#######
for i in range(10, 51):
    with open('/Users/jingli/Desktop/EpEEG/O/O0'+ str(i) +'.txt','r') as csvfile:
    #with open('/Users/jingli/Desktop/EpEEG/Z/Z0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

'''
########Z051 to Z099#######
for i in range(51, 100):
    #with open('/Users/jingli/Desktop/EpEEG/O/O0'+ str(i) +'.txt','r') as csvfile:
    with open('/Users/jingli/Desktop/EpEEG/Z/Z0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

###########Z100#################
#with open('/Users/jingli/Desktop/EpEEG/O/O100.txt','r') as csvfile:
with open('/Users/jingli/Desktop/EpEEG/Z/Z100.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
'''

out = np.array(x)
out = out.reshape(-1, 4097)



#Wavelet transform of siganl level = 5

#fig, ax = plt.subplots(figsize=(6,1))
#ax.set_title("Original Chirp Signal: ")
#ax.plot(out)
#plt.show()

#data = out
waveletname = 'db4'

#Calculate approximate entropy for detail coefficients at level 1 i.e. D1's

entropyD = []

for i in range(50):
    data = out[i]

    (data, coeff_d) = pywt.dwt(data, waveletname)

    temp2 = np.array(coeff_d)
    apen_d = ApEn_new(temp2, 2, 0.15*np.std(temp2))
    entropyD.append(apen_d)

print(entropyD)
entropyD = np.array(entropyD)
threshold =   1.650 #1.8611019359046947 #1.695602197625277 #1.8585500122447973
count = 0

for i in range(50):
    if entropyD[i]>=threshold:
        count = count+1

accuracy = count/50
print("accuracy is: ", accuracy)

#A program to test the accuracy of the ApEn method
'''
Mean of A5: 0.7096954752300244
Max value of A5: 0.7850944444988275
Median value of A5: 0.5009646479129246
'''
import matplotlib.pyplot as plt
import csv
import numpy as np
import pywt
import pywt.data
import scipy.io
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

########201m (0)-(13)###### amount: 14
########202m (0)-(35)###### amount: 36

for i in range(0, 14):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/4 AFIB/201m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 36):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/4 AFIB/202m (' + str(i)+ ').mat')
    x.append(mat['val'])
'''
########202m (36)-(44)###### amount: 9
########203m (0)-(11)###### amount: 12
########210m (0)-(28)###### amount: 29
for i in range(36, 45):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/4 AFIB/202m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 12):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/4 AFIB/203m (' + str(i)+ ').mat')
    x.append(mat['val'])

for i in range(0, 29):
    mat = scipy.io.loadmat('/Users/jingli/Desktop/ECG/4 AFIB/210m (' + str(i)+ ').mat')
    x.append(mat['val'])
'''
out = np.array(x)
out = out.reshape(-1, 3600)



#Wavelet transform of siganl level = 5

#fig, ax = plt.subplots(figsize=(6,1))
#ax.set_title("Original Chirp Signal: ")
#ax.plot(out)
#plt.show()

#data = out
waveletname = 'db4'

#Calculate approximate entropy for detail coefficients at level 1 i.e. D1's

entropyA = []

for i in range(50):
    data = out[i]
    for ii in range(5):
        (data, coeff_d) = pywt.dwt(data, waveletname)
        #axarr[ii, 0].plot(data, 'r')
        temp = np.array(data)
        apen_a = ApEn_new(temp, 2, 0.15*np.std(temp))
        #only append the value of A5, ignore A1-A4
        if ii==4:
            entropyA.append(apen_a)

        #axarr[ii, 1].plot(coeff_d, 'g')
        temp2 = np.array(coeff_d)
        apen_d = ApEn_new(temp2, 2, 0.15*np.std(temp2))

print(entropyA)

Mean = 0.7096954752300244
Maximum = 0.7850944444988275
Median = 0.5009646479129246
Opthres = 0.621

entropyA = np.array(entropyA)
threshold = Opthres
count = 0

for i in range(50):
    if entropyA[i]>threshold:
        count = count+1

accuracy = count/50
print("accuracy is: ", accuracy)

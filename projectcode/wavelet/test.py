#A program to test the accuracy of the ApEn method
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


#################ROC Curve Plotting##################
def plot_roc_curve(fpr, tpr):
    plt.plot(fpr, tpr, color='orange', label='ROC')
    plt.plot([0, 1], [0, 1], color='darkblue', linestyle='--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend()
    plt.show()
###########################################################

x= []


########Z051 to Z099#######
for i in range(51, 100):
    with open('/Users/jingli/Desktop/EpEEG/Z/Z0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

######## Z100 #############
with open('/Users/jingli/Desktop/EpEEG/Z/Z100.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))

for i in range(51, 100):
    with open('/Users/jingli/Desktop/EpEEG/S/S0'+ str(i) +'.txt','r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            x.append(float(row[0]))

with open('/Users/jingli/Desktop/EpEEG/S/S100.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))

out = np.array(x)
out = out.reshape(-1, 4097)
#print(len(out))


#Wavelet transform of siganl level = 5

#fig, ax = plt.subplots(figsize=(6,1))
#ax.set_title("Original Chirp Signal: ")
#ax.plot(out)
#plt.show()

#data = out
waveletname = 'db4'

#Calculate approximate entropy for detail coefficients at level 1 i.e. D1's

entropyD = []

for i in range(100):
    data = out[i]

    (data, coeff_d) = pywt.dwt(data, waveletname)

    temp2 = np.array(coeff_d)
    apen_d = ApEn_new(temp2, 2, 0.15*np.std(temp2))
    entropyD.append(apen_d)


entropyD = np.array(entropyD)
entropyD = entropyD.reshape(-1, 50)

print("For normal", entropyD[0])
print("For epilepsy", entropyD[1])

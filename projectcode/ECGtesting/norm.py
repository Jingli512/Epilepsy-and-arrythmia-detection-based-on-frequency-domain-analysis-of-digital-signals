import matplotlib.pyplot as plt
import csv
import numpy as np
import pywt
import pywt.data
import scipy.io


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

#Wavelet transform of siganl level = 5

#fig, ax = plt.subplots(figsize=(6,1))
#ax.set_title("Original Chirp Signal: ")
#ax.plot(out)
#plt.show()

#data = out
waveletname = 'db4'

#Calculate approximate entropy for both approximation and detail coefficients
#From level 2 to level 5
entropyA = []
entropyD = []
A = [] #A5 values for all training normal signals
D = [] #D1-D5 values for all training normal signals
#fig, axarr = plt.subplots(nrows=5, ncols=2, figsize=(6,6))
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
        entropyD.append(apen_d)

    A.append(entropyA)
    D.append(entropyD)
    #axarr[ii, 0].set_ylabel("Level {}".format(ii + 1), fontsize=14, rotation=90)
    #axarr[ii, 0].set_yticklabels([])
    #if ii == 0:
        #axarr[ii, 0].set_title("Approximation coefficients", fontsize=14)
        #axarr[ii, 1].set_title("Detail coefficients", fontsize=14)
    #axarr[ii, 1].set_yticklabels([])
#plt.tight_layout()
#plt.show()
#print('Appromation Coefficient A5', entropyA)
#print('Detail Coefficients', entropyD)
A = np.array(A)
D = np.array(D)
A = A.reshape(-1, 1)
D = D.reshape(-1, 5)
#print(A)
#print(D)


#Calculate for the mean of A5
A5 = np.mean(A)
A5_median = np.median(A)
A5_max = np.max(A)
print('Mean of A5s: ', A5)
print('Median of A5s: ', A5_median)
print('Maximum of A5s: ', A5_max)

#Calculate for the mean of D1-D5
temp = []
for i in range(5):
    for j in range(50):
        temp.append(D[j][i])
temp = np.array(temp)
temp = temp.reshape(-1, 50)
D1 = np.mean(temp[0])
D2 = np.mean(temp[1])
D2med = np.median(temp[1])
D2max = np.max(temp[1])
D3 = np.mean(temp[2])
D4 = np.mean(temp[3])
D5 = np.mean(temp[4])

print('Mean of D2s', D2)
print('Maximum value of D2s', D2max)
print('Median value of D2s', D2med)
print('Mean of D3s', D3)
print('Mean of D4s', D4)
print('Mean of D5s', D5)

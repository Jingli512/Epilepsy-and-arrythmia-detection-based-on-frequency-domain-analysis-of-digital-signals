import matplotlib.pyplot as plt
import csv
import numpy as np
import pywt
import pywt.data
from scipy import io
from numpy import random

ApEn_norm = [0.4908254858161758, 0.4657842982534106, 0.4081368850048994, 0.43787383479379116, 0.5018429445153121, 0.34160987017367095, 0.45641735786282567, 0.5261006264410018, 0.4724804512391527, 0.3864254424075586, 0.3841580812403276, 0.44382760476853633, 0.4182749186348511, 0.4612498581963509, 0.4865975773512199, 0.4257013705991026, 0.6238892992709206, 0.5469933844621071, 0.4908582697911825, 0.5141813767761381, 0.3966093549008054, 0.5273847835406547, 0.5434146059949434, 0.4419438117330978, 0.5026578551703897, 0.5014631705442958, 0.44839330780749, 0.4092765309964914, 0.5190134968610312, 0.39303743882658626, 0.617345143268333, 0.5177598798064591, 0.5520645919498084, 0.6204644875665655, 0.5004661252815534, 0.5781268613766684, 0.43149570633989054, 0.5741499185047645, 0.558499984430278, 0.5609364530319665, 0.5907675462516888, 0.4314292008372993, 0.5142234203605232, 0.45134568739798375, 0.5559246214982823, 0.5578760579529396, 0.6153599629254285, 0.5861948966586348, 0.4646987369848148, 0.7850944444988275]
ApEn_AFib = [0.5849450880823941, 0.6393326315436467, 0.6764836097634799, 0.6764867962882506, 0.6547504661643848, 0.6245429303531043, 0.614182818249895, 0.7012698029461397, 0.6362716604220964, 0.5319305118983708, 0.7379734199261363, 0.4886791984688994, 0.632056795186779, 0.6070681637815225, 0.6914959041960587, 0.8374443699347007, 0.7280370121741164, 0.840296252361393, 0.7281957268249224, 0.7067003403421088, 0.7276198999950791, 0.7237998992050274, 0.6233215380450967, 0.7456399134967482, 0.7521078909130843, 0.6897090887087716, 0.7212767078155871, 0.8148510884094775, 0.6295606592103606, 0.7054022315499542, 0.6953507645713746, 0.8274620796515619, 0.7935062902058867, 0.7945437754575089, 0.6715535333679248, 0.820102499782347, 0.6284090078658067, 0.7559740936313677, 0.6946950551172151, 0.7795852847826925, 0.7237043771144043, 0.736899843003227, 0.7594419462842796, 0.7925023900977726, 0.8211530549220072, 0.6892836767960979, 0.8011602758067129, 0.7094557604817728, 0.7187615974263522, 0.7997960388773206]

ApEn_norm = np.array(ApEn_norm)
ApEn_AFib = np.array(ApEn_AFib)

# false positive rate
fpr = []
# true positive rate
tpr = []
# true negative rate
tnr = []
#total accuracy
accuracy = []
# Iterate thresholds from 1.600, 1.601, ... 1.900
thresholds = np.arange(0.5, 0.8, .001)

# iterate through all thresholds and determine fraction of true positives
# and false positives found at this threshold
for thresh in thresholds:
    FP=0
    TP=0
    for i in range(0, 50):
        if(ApEn_norm[i] >= thresh):
            FP = FP + 1

    for j in range(0, 50):
        if(ApEn_AFib[j] > thresh):
            TP = TP + 1
    fpr.append(FP/50)
    tnr.append((50-FP)/50)
    tpr.append(TP/50)
    accuracy.append((TP+(50-FP))/100)

plt.xlabel('FPR(False Positive Rate)')
plt.ylabel('TPR(True Positive Rate)')
plt.title('ROC curve')
plt.plot(fpr, tpr)
plt.show()

def annot_max(x,y, ax=None):
    xmax = x[np.argmax(y)]
    ymax = y.max()
    text= "x={:.3f}, y={:.3f}".format(xmax, ymax)
    if not ax:
        ax=plt.gca()
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=60")
    kw = dict(xycoords='data',textcoords="axes fraction",
              arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    ax.annotate(text, xy=(xmax, ymax), xytext=(0.94,0.96), **kw)

plt.plot(thresholds, tnr)
annot_max(thresholds, np.array(tnr))
plt.title('Accuracy of detecting normal signals')
plt.xlabel('Thresholds')
plt.ylabel('Accuracy')
plt.show()

plt.plot(thresholds, tpr)
annot_max(thresholds, np.array(tpr))
plt.title('Accuracy of detecting AFib signals')
plt.xlabel('Thresholds')
plt.ylabel('Accuracy')
plt.show()

plt.plot(thresholds, accuracy)
annot_max(thresholds, np.array(accuracy))
plt.title('Overall Accuracy')
plt.xlabel('Thresholds')
plt.ylabel('Accuracy')
plt.show()

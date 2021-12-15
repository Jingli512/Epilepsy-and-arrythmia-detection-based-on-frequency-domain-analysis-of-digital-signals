import matplotlib.pyplot as plt
import csv
import numpy as np
import pywt
import pywt.data
from scipy import io
from numpy import random

ApEn_norm = [0.7450456752939321, 0.8595630821152866, 0.8387898962677673, 0.8713349181197878, 0.8937583821264723, 0.7890193766612543, 0.8370599325943533, 0.795323291920671, 0.8800826811087759, 0.8904110666747425, 0.993463265978233, 1.1212321075533582, 1.2195264078450512, 1.227241841543143, 1.0855736263629758, 1.025573868703812, 1.251628394735215, 1.1876401647750057, 1.1532604177843107, 1.0766727840759631, 0.8192829356800573, 0.693573858348111, 0.6794503386202111, 0.7994766715503898, 0.7140630226065934, 0.7284005189377383, 0.6637755802053578, 0.8259534804180557, 0.7394090086283858, 0.8438844130520202, 1.3487724062673578, 1.3482186890317651, 1.4310994116796847, 1.348259342167193, 1.3726400343426874, 1.3942885618960599, 1.336039972201351, 1.3960409181112903, 1.36790464317483, 1.3273251432035593, 1.1879827058483707, 0.8015327219238371, 1.1662792545799858, 0.8678773884814328, 1.0749732054805916, 1.1631625967968766, 0.8546100169060682, 1.0304003733465987, 1.0221376990760018, 1.2207569717440445]
ApEn_AFib = [1.3061047875232417, 1.2345895190738494, 1.2980404054282504, 1.2653563961527174, 1.305032545322761, 1.2330550809448706, 1.278270555110229, 1.2223410559950656, 1.2391566705282413, 1.2262996257664804, 1.244237505612265, 1.28803853457259, 1.2752203901442973, 1.2735642137118637, 1.175350980538913, 1.1851912094919301, 1.1510360888609315, 1.1554328011832276, 1.2205642032214161, 1.184747441426687, 1.1067449742782194, 1.1552487508164893, 1.199441408314736, 1.0982011338745803, 1.1796920004819968, 1.1962118535393875, 1.2861104053867436, 1.168776137764465, 1.145877061450804, 1.2576264132443304, 1.2154498693030131, 1.2148279488404716, 1.1763764142146371, 1.227874959547849, 1.1477928006128657, 1.1283427307670175, 1.1851557954978906, 1.1836728460644599, 1.1548993700212833, 1.1540515041562553, 1.1466330257244417, 1.1507399522678634, 1.1734353937651614, 1.19935474667753, 1.1987464269211046, 1.185667635419681, 1.0632718069469371, 1.201890367933168, 1.1363802662751707, 1.1421594526665109]

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
thresholds = np.arange(1, 1.5, .001)

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

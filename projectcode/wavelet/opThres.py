import matplotlib.pyplot as plt
import csv
import numpy as np
import pywt
import pywt.data
from scipy import io
from numpy import random

ApEn_norm1 = [1.8395740279513202, 1.8388279502256122, 1.870293249580083, 1.8443223570672913, 1.8464421291429467, 1.8341776109848835, 1.8207849816469226, 1.8402435144681561, 1.8504075853448176, 1.8765076410897557, 1.868060616163592, 1.876584730473561, 1.8881781951407524, 1.8890482793820604, 1.85310136065097, 1.8713514556873188, 1.8949083977392487, 1.8182870678943184, 1.8878453213193067, 1.8479411156072256, 1.8899305408411617, 1.9181369300927482, 1.8243439930552032, 1.8827893375136933, 1.8667858339067163, 1.876939154197336, 1.695602197625277, 1.8733281938107966, 1.8483056459464686, 1.8648477170391153, 1.8707079082478915, 1.8724383729015788, 1.8460781221611908, 1.8641049310289501, 1.8441608577903938, 1.8513613793108163, 1.867757085117053, 1.869498704244287, 1.912592722112393, 1.8429096768576905, 1.8993868288524745, 1.8685637875551162, 1.8497617792756618, 1.8522866623129435, 1.817561628991971, 1.8496522554303052, 1.8538463799460398, 1.8580989407804394, 1.8843224376728527, 1.8545130200611606]
ApEn_norm2 = [1.8435670986948436, 1.8589371347814092, 1.856275591260835, 1.8439947002243864, 1.8499882792564337, 1.8606671022237524, 1.8652518736363648, 1.8492918502549154, 1.8592948466900792, 1.7934247425377343, 1.830379191811625, 1.7993094740117774, 1.8126223667979806, 1.828816530541423, 1.8225042063758616, 1.8433955694906166, 1.8264746135788643, 1.713012668198183, 1.866460440534178, 1.8999727075921005, 1.8862550949838166, 1.8115085240391675, 1.8331641445114286, 1.856358829177207, 1.8480618899421168, 1.8757671250947485, 1.8429376425920347, 1.858171072909891, 1.8617689919491465, 1.8625484248213198, 1.834311655060949, 1.8421825749359542, 1.6853815330263853, 1.7723747798684082, 1.8727693792662103, 1.8391978595180989, 1.8491971807621388, 1.802376629484459, 1.8338380011899407, 1.8389378621838457, 1.862396319811638, 1.8713261625320232, 1.8424078056051458, 1.8656184937293263, 1.908983075705481, 1.8616252325900629, 1.8458064990267502, 1.8873715944506282, 1.9239941305338055, 1.8856255388988838]
ApEn_inter1 = [1.8543408019687906, 1.766051123060456, 1.6920362227696208, 1.816816872950616, 1.6225520384787409, 1.8541780645248114, 1.8480106666659655, 1.8188755180383769, 1.121404603618302, 1.5646528837479372, 1.7978308019148734, 1.8208096428189817, 1.8664068696334564, 1.8530763899764633, 1.8492319269356576, 1.8724539572973598, 1.8683127685214886, 1.8522827638443111, 1.8579405799934943, 1.8568562163484117, 1.4548190752002395, 1.741993341585233, 1.842307651135708, 1.804548055902016, 1.8583195612354562, 1.8660531593068317, 1.8558878365250777, 1.8421496281879666, 1.8441206781670605, 1.79231765642285, 1.4957582312627853, 1.785600867689384, 1.8520788312474634, 1.8855361442531828, 1.9169123997717632, 1.9058741772631373, 1.7857029104871343, 1.874335931927515, 1.8561844600696418, 1.8556306538357896, 1.8758021400627927, 1.8719599413396146, 1.902290434949295, 1.8076723336708662, 1.8327185458666069, 1.8488219932141599, 1.8870282519925858, 1.897350703775766, 1.8486993021591394, 1.8609126699370853]
ApEn_inter2 = [1.8399864332155236, 1.8551848058200946, 1.8563635124656264, 1.91460411680068, 1.8539258979688045, 1.7093539077166913, 1.893957746182271, 1.8853996474107886, 1.827824065349307, 1.8485932975493533, 1.8417718097180806, 1.8801314828257842, 1.8640132566301082, 1.8322427804020807, 1.8470594096055395, 1.864637353506283, 1.877457214787004, 1.8557633906810107, 1.8704525069938498, 1.85818318440018, 1.87565965434242, 1.8601506601070916, 1.885797178763121, 1.931008946067954, 1.8893865597121797, 1.835988055050172, 1.8566546601991645, 1.87270329808445, 1.8409114217243463, 1.8664278381441726, 1.8893645762852804, 1.8611374384275567, 1.8568408504691787, 1.8787415040257613, 1.8829399835714655, 1.669292108361419, 1.8423294368350653, 1.9063414371745049, 1.8687891756202886, 1.8377525825014391, 1.8472205825104382, 1.8381175167520905, 1.814878171346705, 1.8842342156601486, 1.8543792364433411, 1.8752539513650675, 1.898536623629715, 1.8653273011114324, 1.8682942810777323, 1.843563982526609]
ApEn_ep = [1.1557464672604243, 1.5237891384321438, 1.316486959216018, 1.7502040718547338, 1.3999992136802861, 1.5994709245197898, 0.512312639878485, 1.7138221786540795, 1.697984055520104, 1.226657790824012, 1.2302760935537878, 1.1437070331094148, 1.3470343173799826, 1.3280393097319756, 1.2998096173771851, 1.669621936505079, 1.4319811155090632, 1.192159579834927, 1.5824665453278088, 1.5542806448595714, 1.294770420845313, 1.3841060171289836, 1.3276702449230227, 1.5798407970895, 1.0841338382281216, 1.590695747596084, 1.6244388524397557, 1.5438289055889118, 1.090940882488217, 1.2843057989852404, 1.3337370049945756, 1.4407284880108815, 1.6036124725287806, 1.3364466221419855, 1.6289687652384988, 1.5805826190303094, 1.03609380718422, 1.3026288527275742, 1.7782452554147454, 1.0417622255680934, 1.074032578390589, 1.6919831138605268, 1.8050503285345885, 1.724315259730334, 1.0066597759907125, 1.5328469477038418, 1.0188565259321756, 1.6494460654420404, 1.167935193943555, 1.4995744148039556]

ApEn_norm1 = np.array(ApEn_norm1)
ApEn_norm2 = np.array(ApEn_norm2)
ApEn_inter1 = np.array(ApEn_inter1)
ApEn_inter2 = np.array(ApEn_inter2)
ApEn_ep = np.array(ApEn_ep)

# false positive rate
fpr = []
# true positive rate
tpr = []
# true negative rate
tnr = []
#total accuracy
accuracy = []
# Iterate thresholds from 1.600, 1.601, ... 1.900
thresholds = np.arange(1.6, 1.901, .001)

# iterate through all thresholds and determine fraction of true positives
# and false positives found at this threshold
for thresh in thresholds:
    FP=0
    TP=0
    for i in range(0, 50):
        if(ApEn_norm1[i] < thresh):
            FP = FP + 1
    for ii in range(0, 50):
        if(ApEn_norm2[ii] < thresh):
            FP = FP + 1
    for iii in range(0, 50):
        if(ApEn_inter1[iii] < thresh):
            FP = FP + 1
    for iv in range(0, 50):
        if(ApEn_inter2[iv] < thresh):
            FP = FP + 1
    for j in range(0, 50):
        if(ApEn_ep[j] < thresh):
            TP = TP + 1
    fpr.append(FP/200)
    tnr.append((200-FP)/200)
    tpr.append(TP/50)
    accuracy.append((TP+(200-FP))/250)

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
plt.title('Accuracy of detecting epileptic signals')
plt.xlabel('Thresholds')
plt.ylabel('Accuracy')
plt.show()

plt.plot(thresholds, accuracy)
annot_max(thresholds, np.array(accuracy))
plt.title('Overall Accuracy')
plt.xlabel('Thresholds')
plt.ylabel('Accuracy')
plt.show()

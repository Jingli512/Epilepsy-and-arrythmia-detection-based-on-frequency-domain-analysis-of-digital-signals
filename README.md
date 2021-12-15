Language: Python
Author: Jing Li
Time: April 2021

For EEG dataset:
Source:
Andrzejak, Ralph G et al. “Indications of nonlinear deterministic and finite­dimensional structures in time series of brain electrical activity: Dependence on recording region and brain state”. In: Physical Review E 64.6 (2001), p. 061907.

Z- healthy patients with eyes open
O- healthy patients with eyes closed
N- epilepsy(interictal, seizure-free)
F- epilepsy(interictal, seizure-free)
S- epilepsy(ictal)

Note: recordings in file N were collected from the hippocampal formation of the opposite brain hemisphere, and those in file F were collected from the epileptogenic zone.

Sampling frequency at 173.61Hz
4079 samples/recording collected in a duration of 23.6s

For ECG dataset:
Source:
Plawiak, Pawel. “ECG signals (1000 fragments)”. In: Mendeley Data, v3 (2017).

1 NSR-normal ECG signals
4 AFib-atrial fibrillation signals

Sampling frequency at 360Hz
3600 samples/recording collected in a duration of 10s



Introduction: There are in total 7 folders included, with different functionalities each according to the folder name. For compilation, you need to change the dataset directory and run the following command from the shell:
"python3 filename.py"

ogGraph: 
1)graph.py: The code for graphing the original graphs of the EEG signals from all five categories
2)filteredGraph: The code for drawing the example graph of "original EEG signal vs. filtered EEG signal"

powerSpectrum:
1)norm.py & ep.py: The code for graphing the power spectrum of any given EEG signal
2)fiveGraphs.py: The code for graphing the power spectrums of the EEG signal from each category

spectrogram:
1)norm.py & ep.py: The code for graphing the spectrogram of any given EEG signal
2)fiveGraphs.py: The code for graphing the spectrograms of the EEG signal from each category

Scalogram: 
fiveGraphs.py: The code for graphing the scalograms of the EEG signal from each category

wavelet(Codes for detection method 1):
1)norm.py: The code for DWT and calculating the mean value of ApEn at each subband for normal EEG
2)ep.py: The code for DWT and calculating the mean value of ApEn at each subband for epileptic EEG
3)opThres.py: The code for optimising the threshold at subband D1
4)opThres-D2.py: The code for optimising the threshold at subband D2
5)accuracy-norm.py: The code for calculating the accuracy of detecting normal signals using ApEn at D1
6)accuracy-norm-D2.py: The code for calculating the accuracy of detecting normal signals using ApEn at D2
7)accuracy-inter.py: The code for calculating the accuracy of detecting epileptic signals at interictal state(considered as normal) using ApEn at D1
8)accuracy-inter-D2.py: The code for calculating the accuracy of detecting epileptic signals at interictal state(considered as normal) using ApEn at D2
9)accuracy-ep.py: The code for calculating the accuracy of detecting epileptic signals at ictal state using ApEn at D1
10)accuracy-ep-D2.py: The code for calculating the accuracy of detecting epileptic signals at ictal state using ApEn at D2

similarity(Codes for detection method 2):
1)norm.py: The code for finding the mean, median and minimum value of SS(input signal, template) for normal EEG
2)ep.py: The code for finding the mean, median and minimum value of SS(input signal, template) for epileptic EEG
3)opThres.py: The code for optimising the threshold
4)accuracy-norm.py: The code for calculating the accuracy of detecting normal signals
5)accuracy-inter.py: The code for calculating the accuracy of detecting epileptic signals at interictal state(seizure-free)
6)accuracy-ep.py: The code for calculating the accuracy of detecting epileptic signals at ictal state

ECGtesting(Codes for testing the applicability of the two detection methods to ECG signals):
1)norm.py: The code for DWT and calculating the mean value of ApEn at each subband for normal ECG
2)AFib.py: The code for DWT and calculating the mean value of ApEn at each subband for AFib ECG
3)opThres-A5.py: The code for optimising the threshold at subband A5
4)opThres-D2.py: The code for optimising the threshold at subband D2
5)accuracy-norm-A5.py: The code for calculating the accuracy of detecting normal signals using ApEn at A5
6)accuracy-norm-D2.py: The code for calculating the accuracy of detecting normal signals using ApEn at D2
7)accuracy-AFib-A5.py: The code for calculating the accuracy of detecting AFib signals using ApEn at A5
8)accuracy-AFib-D2.py: The code for calculating the accuracy of detecting AFib signals using ApEn at D2

Graphs: programs for visualising the graphs of the ECG signals

method2(Hellinger):
AFib.py: 
1)norm.py: The code for finding the mean, median and minimum value of SS(input signal, template) for normal ECG
2)AFib.py: The code for finding the mean, median and minimum value of SS(input signal, template) for AFib ECG

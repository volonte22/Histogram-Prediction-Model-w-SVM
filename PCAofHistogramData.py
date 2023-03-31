# AUTHOR : JACK VOLONTE
# CS 429 HW 4 - Part 1
# 10/30/2022
# Description: This program runs a PCA on the feature values contained within the AUrSVMHIstogramsNoFormat.dat file, containing the 806 training histograms data
# formatted and imported into this file by running the SVMWRiteHistogramData.py file, then by manually moving training and validation data to these files

import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import time

import numpy as np
import matplotlib.pyplot as plt
from sklearn import decomposition
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from matplotlib import cm


# loading in data
data = np.loadtxt("AurSVMHistogramsNoFormat.dat", delimiter=" ",dtype=float, comments='#')

print(np.shape(data))
X = data[:806]

pca_model = decomposition.PCA(n_components=5) # make PCA model with n number of components (max = 768 let it be)
variance = pca_model.fit(data) # setting variance to an object

# printing the explaination of variance
print(pca_model.explained_variance_)
print(pca_model.explained_variance_ratio_)
print(pca_model.explained_variance_.cumsum()) #lol?


#plotting the actual PCA model
pca_data = pca_model.transform(data) # getting the PCA data
#print(pca_data)


plt.pause(30)


#write new pca_data to file for SVM use
fileWrite = open("new_data_after_pca.txt", "w")

index = 1
count = 0
for i in pca_data:
    if index < 404:
        fileWrite.write('1 ')
    else:
        fileWrite.write('-1 ')
    for a in i:
        if count != 4:
            fileWrite.write(str(count+1)+':'+ str(a)+' ')
        else:
            fileWrite.write(str(count+1) +':' + str(a))
        count = count + 1
    fileWrite.write('\n')
    count = 0
    index = index + 1




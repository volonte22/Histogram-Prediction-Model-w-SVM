# AUTHOR : JACK VOLONTE
# CS 429 HW 4 - Part 1
# 10/30/2022
# This program reads in images, creates a histogram, and prints out this histogram of each images once per line in a SVM formatted fashion.
# - both nonNormalized and normalized histograms are created for use in the SVM later.

import cv2
import numpy as np
import matplotlib.pyplot as plt
import glob
import time



AurNo = glob.glob('./images/AurNo/*.png')
AurYes = glob.glob('./images/AurYes/*.png')

fileWrite = open("AurSVMHistogramsNoFormat.txt", "w")
#fileWrite2 = open("AurNonNormalizedSVMHistograms.txt", "w")
np.set_printoptions(suppress=True)

# No images histograms
for b in AurNo:
    x = b
    # load image using cv2
    image = cv2.imread(b)

    # create r,g,b arrays
    r = np.array(np.zeros(256))
    g = np.array(np.zeros(256))
    b = np.array(np.zeros(256))
    for i, j in np.ndindex(image.shape[:-1]):  # image.shape = (150,150)

        # get each r g b from each image
        r1 = image[i][j][0]
        g2 = image[i][j][1]
        b3 = image[i][j][2]

        # up the count for each pixel #
        r[r1] = r[r1] + 1
        g[g2] = g[g2] + 1
        b[b3] = b[b3] + 1

    # normalize arrays
    r2 = r
    g4 = g
    b5 = b
    r = ((r - min(r2)) / (max(r2) - min(r2))).round(4)
    g = ((g - min(g4)) / (max(g4) - min(g4))).round(4)
    b = ((b-min(b5)) / (max(b5) - min(b5))).round(4)




    # send to one array of 256*3 length
    rgb = np.array([])
    rgb = np.concatenate((r,g,b),axis=0)
    #print(rgb)
    #fileWrite.write('-1' + ' ')
    countt = 1
    for a in rgb:
        if countt != 768:
            fileWrite.write(str(a) + ' ')
        else:
            fileWrite.write(str(a))
        countt = countt + 1
    fileWrite.write('\n')
    #fileWrite.write('#<' + str(x) + '>\n')

# Yes images histograms
for b in AurYes:
    x = b
    # load image using cv2
    image = cv2.imread(b)

    # create r,g,b arrays
    r = np.array(np.zeros(256))
    g = np.array(np.zeros(256))
    b = np.array(np.zeros(256))
    for i, j in np.ndindex(image.shape[:-1]):  # image.shape = (150,150)

        # get each r g b from each image
        r1 = image[i][j][0]
        g2 = image[i][j][1]
        b3 = image[i][j][2]

        # up the count for each pixel #
        r[r1] = r[r1] + 1
        g[g2] = g[g2] + 1
        b[b3] = b[b3] + 1

    # normalize arrays
    r2 = r
    g4 = g
    b5 = b
    r = ((r - min(r2)) / (max(r2) - min(r2))).round(4)
    g = ((g - min(g4)) / (max(g4) - min(g4))).round(4)
    b = ((b-min(b5)) / (max(b5) - min(b5))).round(4)


    # send to one array of 256*3 length
    rgb = np.array([])
    rgb = np.concatenate((r,g,b),axis=0)
    #print(rgb)

    #fileWrite.write('+1' + ' ')
    countt = 1
    for a in rgb:
        if countt != 768:
            fileWrite.write(str(a) + ' ')
        else:
            fileWrite.write(str(a))
        countt = countt + 1
    fileWrite.write('\n')
    #fileWrite.write('#<' + str(x) + '>\n')





plt.show()

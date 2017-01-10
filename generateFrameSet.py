#Function for extracting individual frame from directory of TIFF files

import matplotlib.pyplot as plt
import glob
import os
import numpy as np
import scipy as sp

def FlattenTIFFData(TIFFdata): #TIFFdata - NumPy array of raw TIFF data

    flat = TIFFdata[:,:,2]
    return flat;

def generateFrameFromTIFF(filePath): #filePath - path of individual image file to load

    image = plt.imread(filePath)

    return image;

def generateFrameSet(filePath): #filePath - path of file directory containing TIFF files to load

    print ("TOP:    Loading script: generateFrameSet")
    print("LOG:    Start Frame Set Generation")
    frames = []
    fileList = glob.glob(filePath)
    print("LOG:       File list contains: " + str(len(fileList)) + " images")
    for file in fileList:
        print("LOG:    Load image Name: " + file)
        frames.append(generateFrameFromTIFF(file))

    return;

generateFrameSet("*.tif")




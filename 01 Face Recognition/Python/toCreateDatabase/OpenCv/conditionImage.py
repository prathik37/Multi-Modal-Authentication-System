#import cv2
#import cv2.cv as cv
import numpy as np
import random
import math
import os
import PIL                  #CAREFUL check if available for the board
from PIL import Image
import ImageOps

classes = 2
trainImg = 6

numRows = 92
numCols = 112

fileRead = 'D:\\Final Year Project\\Code\\RealWorldDatabase\\Original\\s'
pathWrite = 'D:\\Final Year Project\\Code\\RealWorldDatabase\\Conditioned\\s'


for classCounter in range(1,classes+1):
    path = pathWrite + str(classCounter)
    os.mkdir(path)
    for trainImgCounter in range(1,trainImg+1):
        rd = fileRead + str(classCounter) + '\\' + str(trainImgCounter) + '.jpg'
        wr = pathWrite + str(classCounter) + '\\' + str(trainImgCounter) + '.jpg'
        dst = Image.open(rd)
        dst = dst.resize((numRows,numCols))
        dst = ImageOps.grayscale(dst)
        #dst.show()
        dst.save(wr)

print 'CONDITIONED'

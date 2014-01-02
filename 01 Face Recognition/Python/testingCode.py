import cv2
import cv2.cv as cv
import numpy as np
import random
import math


classes = 2
trainImg = 6

imgRow = 50
imgCol = 50

subjectNo = 2
imgNo = 4


essenceVal = np.array(np.zeros((imgRow,imgCol),np.float32))
globalBest = np.array(np.zeros((imgRow,imgCol),np.int))
testImgFeature = np.array(np.zeros((imgRow,imgCol),np.float32))
recognitionMat = np.array(np.zeros((classes*trainImg)))
trainImgFeature = np.array(np.zeros((imgRow,imgCol)))


def dctImage(subjectNo, imgNo):

    global essenceVal

    #imgAddress = 'D:\Final Year Project\Code\Database\ORL\s'+str(subjectNo)+'\\'+str(imgNo)+'.jpg'  
    imgAddress = 'D:\Final Year Project\Code\RealWorldDatabase\Conditioned\s'+str(subjectNo)+'\\'+str(imgNo)+'.jpg'    
    img1 = cv2.imread(imgAddress, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    h, w = img1.shape[:2]
    vis0 = np.zeros((h,w), np.float32)
    vis0[:h, :w] = img1

    vis1 = cv2.dct(vis0)                        # DCT coefficients

    #img2 = cv.CreateMat(vis1.shape[0], vis1.shape[1], cv.CV_32FC3)
    #cv.CvtColor(cv.fromarray(vis1), img2, cv.CV_GRAY2BGR)
    #cv.SaveImage('C:\Users\Rahul Nafde\Desktop\output1.jpg', img2)

    #print vis1;
    #print h,'x',w

    #fileAddress = 'D:\Final Year Project\Code\DCTcoefficients'
    #fileName = fileAddress+'\s'+str(subjectNo)+'\\'+str(imgNo)+'.txt'

    #fo = open(fileName,"w+")
    #fo.write("###\n")

    #np.savetxt(fileName,vis1,fmt='%7.7e')        

    #fo.close()

    essenceVal[:imgRow,:imgCol] = vis1[:imgRow,:imgCol]
     
    return




def recognition():

    global classes, trainImg, testImg, recognitionMat, trainImgFeature
    counter = 0

    fileAddress = 'D:\Final Year Project\Code\FeatureGallery\s'

    for subjectCounter in range(0,classes):
        for imgCounter in range(0,trainImg):
            fileRead = fileAddress + str(subjectCounter+1) + '\\' + str(imgCounter+1) + '.txt'
            trainImgFeature = np.array(np.loadtxt(fileRead))
            temp = (testImgFeature - trainImgFeature)**2
            recognitionMat[counter] = sum(sum(temp))
            counter = counter + 1
            
    return


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN CODE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


dctImage(subjectNo,imgNo)

fileRead = 'D:\Final Year Project\Code\globalFeaturePositions.txt'
globalBest = np.array(np.loadtxt(fileRead),np.int)

testImgFeature = essenceVal * globalBest

recognition()

#recognitionMat = recognitionMat.reshape((-1,trainImg))

minValue = min(recognitionMat)

if (minValue < 8000000):
    identityIndex = np.argmin(recognitionMat)

    authenticate = identityIndex / (float)(trainImg)

    validateID = math.trunc(authenticate+1)
    print authenticate
    print 'Welcome user' + str(validateID) + '. Have a nice day !'

else:
    print 'Access Denied'


print 'DONE'

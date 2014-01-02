import cv2
import cv2.cv as cv
import numpy as np
import random
import math


#No. of  Subjects
classes = 2

#No. of Training images
trainImg = 6   

#Other Variables
imgRow = 50
imgCol =50
essenceVal = np.zeros((imgRow,imgCol), np.float32)
classMean = np.array(np.zeros((classes,imgRow*imgCol),np.float32))
classMeanParticle = np.array(np.zeros((classes,imgRow*imgCol),np.float32))
tempClassMean = np.array(np.zeros((classes,imgRow,imgCol),np.float32))
grandMean = np.array(np.zeros((imgRow*imgCol),np.float32))
grandMeanParticle = np.array(np.zeros((imgRow*imgCol),np.float32))
tempMean = np.array(np.zeros((imgRow,imgCol),np.float32))

#Variables for BPSO
vmax = 2.684
vmin = -2.684
iterations =100
dim = imgRow * imgCol
inertia = 0.6
correctionFactor = 2.0
numParticles = 30
binaryPosition = np.array(np.zeros((numParticles,dim),np.int))
vel = np.array(np.zeros((numParticles,dim)))
particleBest = np.array(np.zeros((numParticles,dim),np.int))
fitParticleBest = np.array(np.zeros(numParticles))
fitGlobalBest = 0.0
globalBest = np.array(np.zeros(dim),np.int)
finalGlobalBest = np.array(np.zeros((numParticles,dim),np.int))




def dctImage(subjectNo, imgNo):

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

    fileAddress = 'D:\Final Year Project\Code\DCTcoefficients'
    fileName = fileAddress+'\s'+str(subjectNo)+'\\'+str(imgNo)+'.txt'

    #fo = open(fileName,"w+")
    #fo.write("###\n")

    np.savetxt(fileName,vis1,fmt='%7.7e')        

    #fo.close()
     
    return





def getEssence(subjectNo, imgNo):

    fileAddressIn = 'D:\Final Year Project\Code\DCTcoefficients'
    fileAddressOut = 'D:\Final Year Project\Code\WorkingValues'
    
    fileNameIn = fileAddressIn+'\s'+str(subjectNo)+'\\'+str(imgNo)+'.txt'
    fileNameOut = fileAddressOut+'\s'+str(subjectNo)+'\\'+str(imgNo)+'.txt'

    value = np.loadtxt(fileNameIn,skiprows=0)
    essenceVal[:imgRow,:imgCol] = value[:imgRow,:imgCol]

    np.savetxt(fileNameOut,essenceVal,fmt='%7.7e')

    return
  





def meanClasses(subjectNo):

    global trainImg, classes, classMean

    f1 = 'D:\Final Year Project\Code\WorkingValues\s'+str(subjectNo+1)+'\\1.txt'
    f2 = 'D:\Final Year Project\Code\WorkingValues\s'+str(subjectNo+1)+'\\2.txt'
    f3 = 'D:\Final Year Project\Code\WorkingValues\s'+str(subjectNo+1)+'\\3.txt'
    f4 = 'D:\Final Year Project\Code\WorkingValues\s'+str(subjectNo+1)+'\\4.txt'
    f5 = 'D:\Final Year Project\Code\WorkingValues\s'+str(subjectNo+1)+'\\5.txt'
    f6 = 'D:\Final Year Project\Code\WorkingValues\s'+str(subjectNo+1)+'\\6.txt'
    
 
    tempClassMean[subjectNo,:,:] = np.array(np.loadtxt(f1)+np.loadtxt(f2)+np.loadtxt(f3)+np.loadtxt(f4)+np.loadtxt(f5)+np.loadtxt(f6))
    tempClassMean[subjectNo,:,:] /= (float)(trainImg)
    tempMean[:,:] += tempClassMean[subjectNo,:,:]
    tempMean[:,:] /= (float)(classes) ;
   # print classMean[subjectNo,:,:]
    
    classMean[subjectNo] = np.transpose(np.reshape(tempClassMean[subjectNo],2500))
     
    return






def BPSOFitness(stringPosition,tempGrandMeanParticle,fitnessFunctionValue):

    for counter in range(0,classes):
        classMeanParticle[counter,:] = classMean[counter,:]*stringPosition   
    
    
   
    for counter in range(0,classes):
        mat1 = np.matrix(classMeanParticle[counter,:]-tempGrandMeanParticle)
        mat2 = mat1.T
        fitnessFunctionValue = fitnessFunctionValue + (mat1*mat2)

    result = math.sqrt(fitnessFunctionValue)

    #print result
      
    return result





    
def BPSO(grandMean):

    global globalBest, fitParticleBest, particleBest, grandMeanParticle, binaryPosition, inertia, correctionFactor, vel, vmax, vmin, finalGlobalBest

    #print grandMean

    for particleCounter in range(0,numParticles):
        for dimensionCounter in range(0,dim):
            if (random.random() > 0.5):
                        binaryPosition[particleCounter,dimensionCounter]=1
            else:
                        binaryPosition[particleCounter,dimensionCounter]=0
            vel[particleCounter,dimensionCounter] = random.random()
            particleBest[particleCounter,dimensionCounter] = binaryPosition[particleCounter,dimensionCounter]

        grandMeanParticle = grandMean*binaryPosition[particleCounter,:];

        #print grandMean
        #print grandMeanParticle

        fitnessFunctionValue = 0;
        fitParticleBest[particleCounter] = BPSOFitness(binaryPosition[particleCounter,:],grandMeanParticle,fitnessFunctionValue)

    #To find best fit
    fitGlobalBest = max(fitParticleBest)
    index = np.argmax(fitParticleBest)

    #print fitGlobalBest
    #print index


    globalBest = particleBest[index,:]

    #print len(globalBest)
    #print globalBest
    #print particleBest[:,:]

    #print particleBest[1,:]
    #print globalBest

    for iterCounter in range(0,iterations):
        for particleCounter in range(0,numParticles):
           fitnessFunctionValue = 0;
           f = BPSOFitness(binaryPosition[particleCounter,:],grandMeanParticle,fitnessFunctionValue)
           #print 'fitParticleBest=',fitParticleBest[particleCounter]
           if (f > fitParticleBest[particleCounter]):
              #print 'f=',f
              fitParticleBest[particleCounter] = f
              #print 'before'
              #print binaryPosition[particleCounter,:]
              #print 'Modify'
              #print  particleBest[particleCounter,:]
              particleBest[particleCounter,:] = binaryPosition[particleCounter,:]
              #print  particleBest[particleCounter,:]
              #print 'Yes'

           fitGlobalBest = max(fitParticleBest)
           index = np.argmax(fitParticleBest)
           globalBest[:] = particleBest[index,:]


           for dimCounter in range(0,dim):  
               vel[particleCounter,dimCounter] = (inertia)*vel[particleCounter,dimCounter] + (correctionFactor)*(particleBest[particleCounter,dimCounter] - binaryPosition[particleCounter,dimCounter])*random.random() + correctionFactor*(globalBest[dimCounter] - binaryPosition[particleCounter,dimCounter])*random.random()

               if(vel[particleCounter,dimCounter] > vmax):
                   vel[particleCounter,dimCounter] = vmax

               if(vel[particleCounter,dimCounter] < vmin):
                   vel[particleCounter,dimCounter] = vmin


               temp = 1 / ( 1 + math.exp(-vel[particleCounter,dimCounter]))

               if (random.random() > temp):
                   binaryPosition[particleCounter,dimCounter] = 1

               else:
                   binaryPosition[particleCounter,dimCounter] = 0
        
        finalGlobalBest = globalBest.reshape((-1,50))   



    return



def createFeatureGallery():

    global classes, trainImg, finalGlobalBest

    fileAddress = 'D:\Final Year Project\Code\FeatureGallery\s'
    for classCounter in range(0,classes):
        for imgNo in range(0,trainImg):
            fileWrite = fileAddress + str(classCounter+1) +'\\' + str(imgNo+1) + '.txt'
            fileRead = 'D:\Final Year Project\Code\WorkingValues\s' + str(classCounter+1) + '\\' + str(imgNo+1) + '.txt'
            temp = np.array(np.loadtxt(fileRead))

            #np.savetxt(fileName,vis1,fmt='%7.7e')
            #print len(temp)
            #print len(temp[0])
            #print temp

            feature = temp * finalGlobalBest
            np.savetxt(fileWrite,feature,fmt='%7.7e')

    #print 'finalGlobalBest:'
    #print len(finalGlobalBest)
    #print len(finalGlobalBest[0])
    #print finalGlobalBest
    #print 'feature'
    #print len(feature)
    #print len(feature[0])
    #print feature
    
    return



#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% MAIN CODE STARTS HERE%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#DO NOT RUN THIS EVERYTIME !!!! [Modifies Disk Memory]
#for i in range(1,classes+1):
  #for j in range(1,trainImg+1):
     #dctImage(i,j)
     #getEssence(i,j)

for count in range (1,classes+1):
    #print count
    meanClasses(count-1)
    #print 'not missed'

grandMean = np.transpose(np.reshape(tempMean,2500))
BPSO(grandMean)

#print globalBest

fileWrite = 'D:\Final Year Project\Code\globalFeaturePositions.txt'
np.savetxt(fileWrite,finalGlobalBest,fmt='%d')

createFeatureGallery()

print 'TRAINING DONE'


#Calculates DCT for the training recordings

import cv2
import cv
import wave
import numpy as np
import struct
import array
import math

from scipy import fftpack

dct = lambda x: fftpack.dct(x, norm='ortho')

subjects = 2
training = 10

dcttemp = np.array(np.zeros((2500),np.float32))
fileaddress = '/home/ubuntu/recordings/s'

for SCounter in range(0,subjects):
 for Counter in range (0,training):
  left = np.array(np.zeros((30000),np.float32))
  filename = fileaddress + str(SCounter+1) + '/' + str(Counter+1) + '.wav' 
  wav = wave.open (filename, "r")
  (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams ()
  frames = wav.readframes (nframes * nchannels)
  out = struct.unpack_from ("%dh" % nframes * nchannels, frames)
  
  threshold = 5000
  out = np.array(filter(lambda x: x>=threshold,out))
  # Convert 2 channles to numpy arrays
  sz = np.size (out)
  left[:sz] = np.array (out)
  
  #left = np.array(out)
  
  left = np.array(left,np.float32)
  dcttemp[:2500]=left[:2500]
  dctl = dct(dcttemp)

  fileName1 = '/home/ubuntu/recordings/features/s' + str(SCounter+1) + '/' + str(Counter+1) + '.txt'
  np.savetxt(fileName1,dctl,fmt='%7.7e')




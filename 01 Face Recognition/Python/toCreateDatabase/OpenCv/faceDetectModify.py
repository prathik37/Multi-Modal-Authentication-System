import cv2
import cv2.cv as cv
import sys
import numpy as np
import PIL
from PIL import Image,ImageOps

deviceID = 0
xCoordinate = 0
yCoordinate = 0
roiHeight = 0
roiWidth = 0

numRows = 92
numCols = 112

##cv.NamedWindow('camera',deviceID)
##capture = cv.CaptureFromCAM(0)

##while True:
##    img = cv.QueryFrame(capture)
##    cv.ShowImage("camera",img)
##    
##    if cv.WaitKey(10) == 27:
##        cv.SaveImage('D:\\Final Year Project\\Code\\faceDetect.jpg',img)
##        print 'Saving...'
##        del(capture)
##        break
##cv.DestroyAllWindows()


def detect(image):
    global xCoordinate, yCoordinate, roiHeight, roiWidth
    image_size = cv.GetSize(image)

    cv.SaveImage('D:\\Final Year Project\\Code\\faceDetect.jpg',image)

    # create grayscale version
    grayscale = cv.CreateImage(image_size, 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    # create storage
    storage = cv.CreateMemStorage(0)

    # equalize histogram
    cv.EqualizeHist(grayscale, grayscale)

    # show processed image
    #cv.ShowImage('Processed', grayscale)

    # detect objects
    cascade = cv.Load('C:\\OpenCV\\data\\haarcascades\\haarcascade_frontalface_alt.xml')
    faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING)

    if faces:
        for i in faces:
##            xCoordinate = i[0][0]
##            yCoordinate = i[0][1]
##            roiWidth = i[0][0] + i[0][2]
##            roiHeight = i[0][1] + i[0][3]
            cv.Rectangle(image,
                         (i[0][0], i[0][1]),
                         (i[0][0] + i[0][2], i[0][1] + i[0][3]),
                         (0, 255, 0),
                         3,
                         8,
                         0)
            xCoordinate = i[0][0]
            yCoordinate = i[0][1]
            roiWidth = i[0][0] + i[0][2]
            roiHeight = i[0][1] + i[0][3]
            

if __name__ == "__main__":

    wtolerance = 5
    htolerance = 5
    
    print "Press ESC to take snapshot ..."

    # create windows
    cv.NamedWindow('Face View', cv.CV_WINDOW_AUTOSIZE)
    #cv.NamedWindow('Processed', cv.CV_WINDOW_AUTOSIZE)

    # create capture device
    # assume we want first device
    capture = cv.CaptureFromCAM(deviceID)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_WIDTH, 640)
    cv.SetCaptureProperty(capture, cv.CV_CAP_PROP_FRAME_HEIGHT, 480)

    # check if capture device is OK
    if not capture:
        print "Error opening capture device"
        sys.exit(1)

    while 1:
        # do forever

        # capture the current frame
        frame = cv.QueryFrame(capture)
        
        if frame is None:
            break

        # mirror
        cv.Flip(frame, None, 1)

        # face detection
        detect(frame)

        # display webcam image
        cv.ShowImage('Face View', frame)

        # handle events
        k = cv.WaitKey(10)

        if k == 0x1b: # ESC
            print 'ESC pressed. Exiting ...'
            cv.DestroyAllWindows()
            cv.SaveImage('D:\\Final Year Project\\Code\\faceDetected.jpg',frame)
            
            del(capture)
            break
        
if ((xCoordinate == 0) & (yCoordinate == 0)):
   print 'Retake Snapshot'
else:
    print 'Saving...'
    box = (xCoordinate+wtolerance,yCoordinate+htolerance, roiWidth+wtolerance, roiHeight+htolerance)
    img = Image.open('D:\\Final Year Project\\Code\\faceDetect.jpg')
    imgRoi = img.crop(box)
    imgRoi = imgRoi.resize((numRows,numCols))
    imgRoi = ImageOps.grayscale(imgRoi)
    imgRoi.save('D:\\Final Year Project\\Code\\face.jpg')
    print 'X='+str(xCoordinate)+'Y='+str(yCoordinate)+'width='+str(roiWidth)+'height='+str(roiHeight)
    print 'Authenticating...'

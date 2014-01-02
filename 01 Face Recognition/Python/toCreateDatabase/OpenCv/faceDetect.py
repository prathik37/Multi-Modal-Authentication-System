#
# Python 2.6 and OpenCV 2.0 face detection
#
# Detects face(s) visible to a webcam using a bright green border
#
# Haar casade file is required:
#


# import required libraries
import sys
import cv2
import cv2.cv as cv

# function to detect face in a frame
def detect(image):
    image_size = cv.GetSize(image)

    # create grayscale version
    grayscale = cv.CreateImage(image_size, 8, 1)
    cv.CvtColor(image, grayscale, cv.CV_BGR2GRAY)

    # create storage
    storage = cv.CreateMemStorage(0)

    # equalize histogram
    cv.EqualizeHist(grayscale, grayscale)

    # show processed image
    cv.ShowImage('Processed', grayscale)

    # detect objects
    cascade = cv.Load('C:\\OpenCV\\data\\haarcascades\\haarcascade_frontalface_alt.xml')
    faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING)

    if faces:
        for i in faces:
            cv.Rectangle(image,
                         (i[0][0], i[0][1]),
                         (i[0][0] + i[0][2], i[0][1] + i[0][3]),
                         (0, 255, 0),
                         3,
                         8,
                         0)
            

if __name__ == "__main__":
    print "Press ESC to exit ..."

    # create windows
    #cv.NamedWindow('Raw', cv.CV_WINDOW_AUTOSIZE)
    #cv.NamedWindow('Processed', cv.CV_WINDOW_AUTOSIZE)

    # create capture device
    device = 0 # assume we want first device
    capture = cv.CaptureFromCAM(device)
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
        cv.ShowImage('Raw', frame)

        # handle events
        k = cv.WaitKey(10)

        if k == 0x1b: # ESC
            print 'ESC pressed. Exiting ...'
            cv.DestroyAllWindows()
            break

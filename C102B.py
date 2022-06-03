import cv2
import dropbox
import time 
import random

starttime = time.time()

def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        image1 = "img"+str(number)+".png"
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite(image1,frame)
        starttime = time.time
        result = False
    return image1
    print("snapshot taken")

    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

#def uploadfile(name):



def main():
    while(True):
        if((time.time()-starttime)>=10):
            name = take_snapshot()
  #          uploadfile(name)
         
main()
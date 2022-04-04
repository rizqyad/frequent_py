import cv2
import os

in_path = 'video_sources'
out_path = 'frames_output'
filename = 'frame'

# function for getting frame from video
def getFrame(sec, vidcap): #input time
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        print(filename + str(count))
        cv2.imwrite(out_path + '/' + filename + str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames

# read every mp4 file in the folder
count = 1 #frame counter start
for name in os.listdir(in_path):
    if name.endswith(".mp4"):
        print(in_path + '/' + name)
        vidcap = cv2.VideoCapture(in_path + '/' + name) #start video capture for name.mp4
        sec = 0 #time start
        frameRate = 1 #it will capture image in each 1 second
        success = getFrame(sec, vidcap) #calling function
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = getFrame(sec,vidcap)
        vidcap.release()
    print(count)

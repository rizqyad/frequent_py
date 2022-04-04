import cv2
import os

in_path = 'video_sources'
out_path = 'frames_output'
filename = 'uji-mtrl-R'

videoname = "video_sources/CCTV Berbasis Kewilayahan _ Pemerintah Kota Yogyakarta 2021-08-01 06_14.mp4"

print(videoname)

# open video capture
vidcap = cv2.VideoCapture(videoname)
# read frame
hasFrame, image = vidcap.read()
count = 1 #frame counter start
while hasFrame:
    if count < 10:
        numering = '000'+str(count)
    elif count < 100:
        numering = '00'+str(count)
    elif count < 1000:
        numering = '0'+str(count)
    else:
        numering = str(count)
    print(filename + numering)
    cv2.imwrite(out_path + '/' + filename + numering+".jpg", image)
    hasFrame, image = vidcap.read()
    count += 1 #frame counter increament
vidcap.release()

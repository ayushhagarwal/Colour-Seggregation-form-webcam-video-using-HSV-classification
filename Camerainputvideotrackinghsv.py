import cv2
import numpy as np

def nothing(x):
    pass
cap=cv2.VideoCapture(0)     ####capturing video from the webcam

cv2.namedWindow('tracking window')
fourcc=cv2.VideoWriter_fourcc(* 'XVID')
out1=cv2.VideoWriter('original video input.mp4',fourcc,20.0,(640,480)) ##fourcc is codec
out2=cv2.VideoWriter('mask.mp4',fourcc,20.0,(640,480))
out3=cv2.VideoWriter('object sperated result.mp4',fourcc,20.0,(640,480))
###new window in which we can adjust lower and upper bound values of HSV
cv2.createTrackbar('LH','tracking window',0,255,nothing)
cv2.createTrackbar('LS','tracking window',0,255,nothing)
cv2.createTrackbar('LV','tracking window',0,255,nothing)
cv2.createTrackbar('UH','tracking window',255,255,nothing)
cv2.createTrackbar('US','tracking window',255,255,nothing)
cv2.createTrackbar('UV','tracking window',255,255,nothing)

while True:
    #frame=cv2.imread('smarties.png')
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


###get the lower and upper values of HSV from the trackbar position
    l_h=cv2.getTrackbarPos('LH','tracking window')
    l_s=cv2.getTrackbarPos('LS','tracking window')
    l_v=cv2.getTrackbarPos('LV','tracking window')
    u_h=cv2.getTrackbarPos('UH','tracking window')
    u_s=cv2.getTrackbarPos('US','tracking window')
    u_v=cv2.getTrackbarPos('UV','tracking window')
    

    l_b=np.array([l_h,l_s,l_v])   ##lower bound value for hsv space
    u_b=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    ####saving the video simultaneously as they are running
    out1.write(frame)
    out2.write(mask)
    out3.write(res)


####showing all the windows of videos simultaneously
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)


    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
out1.release()
out2.release()
out3.release()

cv2.destroyAllWindows()
         

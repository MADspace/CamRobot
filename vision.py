import cv2, cv, numpy as np

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    
    rval, frame = vc.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.medianBlur(frame, 3)
    circles = cv2.HoughCircles(frame, cv2.cv.CV_HOUGH_GRADIENT, 1, 1000, param1=100, param2=30)
    if circles != None:
        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle

    
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
quit(0)
img = cv2.imread("ball.jpg", 0)

img = cv2.medianBlur(img, 5)
#img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 100, param1=100, param2=30)
circles = np.uint16(np.around(circles))
print circles
for i in circles[0,:]:
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
    cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle


cv2.imshow('detected circles',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
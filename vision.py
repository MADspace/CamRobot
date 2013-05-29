import cv2, cv, numpy as np, urllib2

cv2.namedWindow("preview")

rval = True
while rval:
    
    plaatje = urllib2.urlopen('http://192.168.168.161:8123/snapshot.cgi?user=admin&pwd=31084_robot').read()

    img_array = np.asarray(bytearray(plaatje), dtype=np.uint8)
    print img_array
    frame = cv2.imdecode(img_array, 0)

    frame = cv2.medianBlur(frame, 9)
    circles = cv2.HoughCircles(frame, cv2.cv.CV_HOUGH_GRADIENT, 1, 1000, param1=100, param2=30, minRadius=30, maxRadius=300)
    if circles != None:
        for i in circles[0,:]:
            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle

    
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
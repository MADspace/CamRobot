import cv2, cv, numpy as np, urllib2

cv2.namedWindow("preview")

rval = True
while rval:
    
    plaatje = urllib2.urlopen('http://192.168.168.161:8123/snapshot.cgi?user=admin&pwd=31084_robot').read()
    urllib2.urlopen('http://192.168.168.161:8123/decoder_control.cgi?command=1&user=admin&pwd=31084_robot').read()
    img_array = np.asarray(bytearray(plaatje), dtype=np.uint8)
    frame = cv2.imdecode(img_array, 0)
    
    frame = frame[240:480,0:640]

    frame = cv2.medianBlur(frame, 9)
    circles = cv2.HoughCircles(frame, cv2.cv.CV_HOUGH_GRADIENT, 1, 1000, param1=100, param2=30, minRadius=30, maxRadius=300)
    if circles != None:
        for i in circles[0,:]:
            x_coordinate = i[0]
            if x_coordinate < 320:
                print 'left!'
                urllib2.urlopen('http://192.168.168.161:8123/decoder_control.cgi?command=6&user=admin&pwd=31084_robot').read()
            else:
                print 'right!'
                urllib2.urlopen('http://192.168.168.161:8123/decoder_control.cgi?command=4&user=admin&pwd=31084_robot').read()

            cv2.circle(frame,(i[0],i[1]),i[2],(0,255,0),1)  # draw the outer circle
            cv2.circle(frame,(i[0],i[1]),2,(0,0,255),3)     # draw the center of the circle

    
    
    cv2.imshow("preview", frame)
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
    
import cv2
import numpy as np
frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0) #default 0 for computer webcam, otherwise change id in case multiple cams
cap.set(3,frameWidth) # Set width
cap.set(4,frameHeight) #Set Height
cap.set(10,100) #Set Brightness

myColors =[[51,168,30,121,255,168]]
myColorValue = [[0,255,0]]

def findColor(img, myColors, myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        #cv2.imshow(str(color[0]),mask)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValue[count],cv2.FILLED)
        count +=1



def getContours(img):
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        #cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            print("peri : {0}".format(peri))
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            x,y, w, h = cv2.boundingRect(approx)
    return x+w//2,y


while True:
    result, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors, myColorValue)
    cv2.imshow("Video",imgResult)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
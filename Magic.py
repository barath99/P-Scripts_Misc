########################### INVISIBILITY CLOAK ########################

import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
time.sleep(3)
 
for i in range(30):
  ret,background = cap.read()
  cv2.imshow('BG',background)


cv2.imshow('Final_Bg',background)

while True:
    # Capturing the live frame
    ret, img = cap.read()
     
    # converting from BGR to HSV color space
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 
    # Range for lower red
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
 
    # Range for upper range
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask2 = cv2.inRange(hsv,lower_red,upper_red)
 
    # Generating the final mask to detect red color
    mask = mask1+mask2


    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
    cv2.imshow('check',mask)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3),np.uint8))
    cv2.imshow('check1',mask)
 
    #creating an inverted mask to segment out the cloth from the frame
    mask2 = cv2.bitwise_not(mask)
     
 
    #Segmenting the cloth out of the frame using bitwise and with the inverted mask
    res1 = cv2.bitwise_and(img,img,mask=mask2)

    # creating image showing static background frame pixels only for the masked region
    res2 = cv2.bitwise_and(background, background, mask = mask)
 
 
    #Generating the final output
    final_output = cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow("magic",final_output)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()


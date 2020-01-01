import cv2
import numpy as np
import matplotlib.pyplot as plt

#Classifying a picture as a day light/night light picture

#img = cv2.imread('img.png')
cap= cv2.VideoCapture(0)
while True:
    _,img = cap.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# In HSV the V channel will have most distinguishable differences between
# a day light picture and a night light picture

    sum_brightness = np.sum(img[:,:,2])
    avg_brightness = sum_brightness/(img.shape[0]*img.shape[1])

    print (sum_brightness)
    print (avg_brightness)

    day =1
    def classifier(avg_brightness1):
        day = 1
        if avg_brightness1 <50:
            day = 0
        return day

    day= classifier(avg_brightness)

    if day==1:
        print("Its Day")
    else:
        print("Its Night")

    if cv2.waitKey(1000) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()

    

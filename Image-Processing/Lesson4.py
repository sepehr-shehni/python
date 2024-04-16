import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    #cv2.line(frame,(100,200),(200,400),(10,30,130),20)
    #cv2.rectangle(frame,(100,200),(200,300),(0,0,255),5)
    #cv2.circle(frame,(400,200),70,(120,0,50),3)
    #
    # pts = np.array([[50,100],[120,200],[250,100],[400,20]])
    # cv2.polylines(frame,[pts],True,(60,40,20),5)

    #font = cv2.FONT_HERSHEY_COMPLEX
    #cv2.putText(frame,'Fariborz Fallahzadeh',(50,50),font,1,(100,20,255),2)
    cv2.imshow('webcam',frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
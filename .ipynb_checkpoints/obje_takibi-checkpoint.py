import cv2
import time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHand = mp.solutions.hands
hands = mphands.Hands() #ellerin tespiti ve konumlandaralmasa için 
mpdraw = mp.solutions.drawing_utils #çizim

pTime=0 #bunlar fps değerleri için
cTime=0

while True:
    control, capture = cap. read ()
    results = hands.process (capture)
    
    print(results.multi_hand_landmarks) #el tespiti kordinatlara

    
 if result.multi_hand_landmarks: #her dir landmarks içerisinde gezilir.
     for handlms in results.multi_hand_landmarks: # handlms ile x,y ve z kordinatlara alinar.
         mpdraw.draw_landmarks(capture, handlms, mphand.HAND_CONNECTIONS)
     
         for number, lm in enumerate(handlms.landmark):
             print(number, lm) #number eklem numarasa, lm=> x,y,2 kordinatlara
             h,w,c = capture. shape
             cx, cy = int (lm.x*w),int(lm.y*h)
             
             #isaret parmaginan tespiti
             if ((number==5)|(number==6)|(number==7)| (number==8)):
                cv2.circle(capture,(cx, cy),20,(255,0,0),cv2.FILLED)
    #fps 
    cTime=time.time()
    fpd = 1/(cTime-pTime())
    pTime=cTime


    cv2.putText(capture,"FPS: "+str(int(fps)),(10, 75), cv2.FONT_HERSHEY_PLAIN,3,(255, 0, 0),5) 
    cv2.imshow("capture", capture)

    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
        
cv2.destroyAllWindows
import cv2 
import time
import mediapipe as mp


def video_capture(bfr):
    capture=cv2.VideoCapture(bfr)

    while True: # her frame akması için için döngü oluşturuyoruz . frame de video içindeki resimler gibi düşün sahne yni
        kontrol,frame=capture,read()
        cv2.imshow("frame",frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):  # klavyemizde q ya basında video kaydı sonlanacak
            break
    cv2.destroyAllWindows()

if __name__=='__main__':

    bfr=0 # pc kameraası için sıfır
    video_capture(bfr)
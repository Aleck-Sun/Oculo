import cv2
import requests
import time

vid = cv2.VideoCapture(0)

def APIinterfacer(url, blob : bytes) -> str:
    r = requests.post(url, data=blob)
    return "5 Dollars" 
    

def main():
    while(True):
        
        ret, frame = vid.read()
        
        cv2.imshow('frame', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    vid.release()
    
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
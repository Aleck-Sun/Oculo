import cv2
import requests
import time
import base64

vid = cv2.VideoCapture(0)

def APIinterfacer(url, blob : bytes) -> str:
    files = {
        'file': ("moneyBill.jpg", blob),
        'Content-Type': 'image/jpeg',
        'Content-Length': 1
    }
    
    r = requests.post(url, files=files)
    print(r.status_code, r.content)
    return r.content.decode('utf-8')
    

def main():
    while(True):
        
        _, frame = vid.read()
        
        cv2.imshow('frame', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            _, buffer = cv2.imencode('.jpg', frame)
            
            print(APIinterfacer("http://localhost:5000/api/v0/classifyImage", buffer))
            break
        
        
    vid.release()
    
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
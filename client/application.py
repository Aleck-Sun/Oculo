import cv2
import requests
import time
import base64

vid = cv2.VideoCapture(0)

def APIinterfacer(url, blob : bytes) -> str:
    r = requests.post(url, data=blob)
    print(r.status_code, r.content)
    return r.content.decode('utf-8')
    

def main():
    while(True):
        
        ret, frame = vid.read()
        
        cv2.imshow('frame', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            ret, buffer = cv2.imencode('.jpg', frame)
            tojpeg = base64.b64encode(buffer)
            
            print(APIinterfacer("http://localhost:5000/api/v0/classifyImage", tojpeg))
            break
        
        
    vid.release()
    
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    main()
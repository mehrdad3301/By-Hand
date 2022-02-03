import cv2 
import time 

class Controller : 
    wCam , hCam = 640 , 480
    def __init__(self) : 
        self.cap = cv2.VideoCapture(0) 
        self.cap.set(3 , self.wCam)
        self.cap.set(4 , self.hCam)
        self.fps = Fps() 

    def get_image(self) : 
        sec , self.img = self.cap.read() 
        self.img = cv2.flip(self.img , 1)
        return self.img if sec else None 

    def show_image(self , militime = 1 , name = 'cam') : 
        cv2.imshow(name , self.img) 
        cv2.waitKey(militime)

    def put_fps(self) :
        cv2.putText(self.img , "FPS : " + str(int(self.fps.get_fps())) , (50, 50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0 , 0 , 255) , 2)		

class Fps : 

    def __init__(self) : 
        self.prev_time = 0
        self.curr_time = 0
        self.fps = 0

    def get_fps(self) : 
        self.curr_time = time.time()
        self.fps = 1 / (self.curr_time - self.prev_time) 
        self.prev_time = self.curr_time 	
        return self.fps


 
import cv2 
import autopy 
import numpy as np 
import HandTrackingModule as htm 

class MouseController : 
    
    def __init__(self , detector = htm.handDetector() , wCam = 640 , hCam = 480)  : 
        self.detector = detector 
        self.wCam = wCam
        self.hCam = hCam 
        self.frameR = 100
        self.pre_x = 0 
        self.pre_y = 0 
        self.cur_x  = 0 
        self.cur_y = 0 
        self.smooth = 5 

    def check_mouse_move(self , img) : 
        
        img = self.detector.findHands(img , True) 
        lm = self.detector.findPosition(img) 
        
        # check if hand was detected 
        if len(lm) != 0 : 
            fingers = self.detector.fingersUp()

            #see if index finger is up
            # if true enter moving mode 
            if fingers[1] != 0 : 
            
                x1 , y1 = lm[8][1:] 
                cv2.circle(img , (x1 , y1) , 15 , (0 , 0 , 255) , cv2.FILLED)
                
                cv2.rectangle(img , (self.frameR , self.frameR) , (self.wCam - self.frameR , self.hCam - self.frameR) , (0 , 0 , 255) , 3)

                wScr , hScr = autopy.screen.size()
                x1 = np.interp(x1 , [self.frameR , self.wCam - self.frameR] , [0 , wScr])
                y1 = np.interp(y1 , [self.frameR , self.hCam - self.frameR] , [0 , hScr])

                #see if middle finger is also up 
                #if true enter click mode 
                if fingers[2] == 0 :

                    try :

                        self.cur_x = self.pre_x + (x1 - self.pre_x) / self.smooth
                        self.cur_y = self.pre_y + (y1 - self.pre_y) / self.smooth
                        self.pre_x = self.cur_x 
                        self.pre_y = self.cur_y

                        autopy.mouse.move(self.cur_x , self.cur_y)

                    except ValueError : 
                        pass 
                else : 
                    x2 , y2 = lm[12][1:]
                    cv2.circle(img , (x2 , y2) , 15 , (0 , 0 , 255) , cv2.FILLED)

                    length , img , points = self.detector.findDistance(12 , 8 , img , True)

                    if length < 40 : 
                        autopy.mouse.click()
                        cv2.circle(img , points[4:], 15 , (0 , 0 , 255) , cv2.FILLED)
                    
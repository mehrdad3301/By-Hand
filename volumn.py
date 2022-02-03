import cv2 
import HandTrackingModule as htm
from subprocess import call 

class VolumnControl : 
	def __init__(self , detector = htm.handDetector()) : 
		self.detector = detector  

	# this method changes system volumn accordingly - only works on linux ! 
	def set_volumn(self ,percentage) : 
		call(["amixer", "-D", "pulse", "sset", "Master", str(percentage)+"%"])


	def check_for_volumn(self, img) : 

		img = self.detector.findHands(img)
		lm = self.detector.findPosition(img) 
		
		# check if hand was detected 
		if len(lm) != 0 :  
			length = self.detector.findDistance(4 , 8 , img , True)[0] 
			vol_per = length / 350 * 100 
			self.set_volumn(vol_per)
			cv2.rectangle(img , (50 , 100) , (85 , 400) , (0 , 255 , 0) , 3)
			cv2.rectangle(img , (50 , 400 - int(vol_per / 100 * (400 - 100) )) , (85 , 400) , (0 , 255 , 0) , cv2.FILLED)
			cv2.putText(img , "Vol : " + str(int(vol_per)) + "%" , (50, 450) , cv2.FONT_HERSHEY_COMPLEX , 0.5 , (0 , 0 , 255) , 1)		



## By Hand  

This is a little project to make your laptop more intractive . It uses mediapipe hand solutions to detect hand landmarks and uses  that data to change volumn or move the mouse. 

## Getting Started 
 
# Volumn 
VolumnController uses HandTrackingModule to find the distance between index and thumb. It then uses set_volumn method to change the volumn. However This method only works on Linux. Refer to Acknowledgments for help.
<img align='center' src='img/volumn.gif' width='450'/> 

# Mouse 
There are two modes. moving and clicking. When There's only index up MouseController enters moving mode. It creates a Rectangle for us to move our finger in and calculates relative coordinates to move the mouse. If both middle and index are up, We are in clicking mode. It waits until index and middle tips touch then clicks. 
<img align='center' src='img/mouse.gif' width='600'/> 
### Prerequisites 

* [mediapipe](https://github.com/google/mediapipe)
* [opencv](https://github.com/opencv/opencv)
* [autopy](https://github.com/autopilot-rs/autopy)

## Acknowledgments

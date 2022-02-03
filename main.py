from mouse import MouseController
from utils import Controller
from volumn import VolumnControl

def main() : 

    controller = Controller() 
    vc = VolumnControl()
    #mv = MouseController(wCam = controller.wCam , hCam = controller.hCam)
    
    while True : 
        
        img = controller.get_image()
        controller.put_fps()       
        vc.check_for_volumn(img) 
        #mv.check_mouse_move(img)
        controller.show_image()
        
if __name__ == "__main__" : 
    main()
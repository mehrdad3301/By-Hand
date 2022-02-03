from mouse import MouseController
from utils import Controller
from volumn import VolumnControl

def main() : 

    controller = Controller() 
    vc = VolumnControl()
    mv = MouseController()
    while True : 
        
        img = controller.get_image()
        controller.put_fps()       
        
        mv.check_mouse_move(img) 
        controller.show_image()
        
if __name__ == "__main__" : 
    main()
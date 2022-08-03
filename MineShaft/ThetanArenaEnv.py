from .BaseEnv import BaseEnv
import os

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=BaseEnv.IO_MODE.FULL_CONTROL,
                 explore_space=BaseEnv.EXPLORE_MODE.FULL):
        """This is the code of start game
        
        Use try and catch statement to catch exception when the game is not installed in the provided path,
        then raise the exception for the upper level to handle.

        The hardcode path to open the game:
        "C:\Program Files (x86)\Thetan Arena\Thetan Arena.exe"
        """
        super(ThetanArenaEnv, self).__init__()
        
        """
        use try and catch statement to catch exception 
        when the game is not installed in the provided path, 
        then raise the exception for the upper level to handle
        """
        try:
            self._start_game()
        except:
            raise Exception("the game is not installed")

    def step(self, action):
        pass
    
    def reset(self):
        pass
    
    def close(self):
        pass
    
    def _take_action(self, action):
        pass
    
    def _screen_cap(self):
        pass
    
    def _keyboard_input(self, action):
        # scan and find keyboard action
        # key press # self._keyboard_press(ascii_list)
        # key release # self._keyboard_release(ascii_list)
        pass
    
    def _keyboard_press(self, ascii_list):
        pass

    def _keyboard_release(self, ascii_list):
        pass
    
    def _mouse_move(self, action):
        pass
    
    def _mouse_click(self, left, right):
        # scan and find mouse action
        # mouse press #self._mouse_press(left, right)
        # mouse release #self._mouse_release(left, right)
        pass
    
    def _mouse_press(self, left, right):
        pass
    
    def _mouse_release(self, left, right):
        pass
    
   def _start_game(self):
        """
        This is the code for start game
        
        The file path "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe" 
        and programme name "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe" 
        is hardcode.
    """
        
        progname = "C:\\Users\\Public\\Desktop\\Thetan Arena"
        filepath = "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe"
       
        self.p = subprocess.Popen([filepath,progname])

    def _enter_match(self):  
        '''
        the method requires an image parameter which is in numpy.ndarray format
        then it compares the image with screen capture
        '''
        def matching_with_screencap(tofind):
		    '''
            screen capture using pyautogui 
            '''
            screen = pyautogui.screenshot()

            '''
            change the capture to numpy array
            '''
            img = np.array(screen)

            '''
            since the matchtemplate() function requires 2 images with same format
            so the below code is to convert the images to RBG format
            '''
            
            tofind = cv.cvtColor(tofind, cv.COLOR_BGR2RGB)



            background = cv.cvtColor(img, cv.COLOR_BGR2RGB)
              

            '''
            the below opencv function matchTemplate() receive 3 parameters, first 2 are images in 
            numpy array, the third one is the opencv comparison algorithm. The function returns
            a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel 
            match with template.
            '''
            result = cv.matchTemplate(background,tofind,cv.TM_CCOEFF_NORMED)
            '''
            the below minMaxLoc() function receives a parameter which is a grayscale image
            then return 4 parameters:
            1. the  thershold value of minimum match objects
            2. the  thershold value of maximum match objects
            3. the  coordinates of minimu match objects
            4. the  coordinates of maximum match objects
            '''
            min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
            '''
            the methond only returns the thershold value and location of the most suitable matching object
            '''
            return max_loc,max_val	

        '''
        change the current directory to the script folder so that relative path can be used
        '''
        folder_path = os.path.dirname(os.path.abspath(__file__))      
        os.chdir(folder_path)
         
        import time 
        '''
        opencv read the find match image by file path
        '''
        tofind = cv.imread('../SourcePictures/findmatch2.png',cv.IMREAD_UNCHANGED) 
        '''
        using the above method
        '''
        loc,thershold = matching_with_screencap(tofind)

        '''
        using pyautogui to click the obtained coordinates
        '''
        pyautogui.moveTo(loc[0]-100,loc[1],duration =0.2)
        pyautogui.click(button='left',duration=0.2)
        
        '''
        similarly, using pyautogui to click the obtained coordinates
        '''

        tofind = cv.imread('../SourcePictures/deathmatch2.png',cv.IMREAD_UNCHANGED)  
        loc2,thershold = matching_with_screencap(tofind)
        if thershold>0.7:
            pyautogui.moveTo(loc2[0]+250,loc2[1],duration =0.2)
            pyautogui.click(button='left',duration=0.2)

        else:
            pyautogui.dragTo(loc[0]-400,loc[1],duration =0.2,button='left')
            tofind = cv.imread('../SourcePictures/deathmatch2.png',cv.IMREAD_UNCHANGED)  
            time.sleep(2)
            loc2,thershold = matching_with_screencap(tofind)
            if thershold<0.6:
                print('no deathmatch game mode')
                exit()
            pyautogui.moveTo(loc2[0]+250,loc2[1],duration =0.2)
            pyautogui.click(button='left',duration=0.2)

        '''
        again, using the above method to find and click the tutorial image
        '''

        tofind = cv.imread('../SourcePictures/tutor.png',cv.IMREAD_UNCHANGED)  
        loc,thershold = matching_with_screencap(tofind)
        pyautogui.moveTo(loc[0] ,loc[1],duration =0.2)
        pyautogui.click(button='left',duration=0.2)
         
        
    def _end_game(self):
        pass
    
    def _reset_game(self):
        pass

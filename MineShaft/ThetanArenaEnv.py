from .BaseEnv import BaseEnv
import subprocess
import os
import cv2
import mss
import numpy
import pyautogui
import pygetwindow as gw

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
            os.startfile("C:\Program Files (x86)\Thetan Arena\Thetan Arena.exe")
            # can this line be directly replaced by the following?
            # self._start_game()
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
        """
        This is the function to capture screen from the game - Thetan Arena.
        pygetwindow is used to get the coordinates and resolution of game by matching with WindowsWithTitle('Thetan Arena').

        Returns
        -------
        captured image in format of numpy.array in CHW
        
        """
		
        with mss.mss() as sct:
            gameWindow = gw.getWindowsWithTitle('Thetan Arena')[0]
            monitor = {"top": gameWindow.top, "left": gameWindow.left, "width": gameWindow.width, "height": gameWindow.height}

            img = numpy.array(sct.grab(monitor))

            rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB) 
            rgb2 = numpy.transpose(rgb, (2,0,1))

            return rgb2
    
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
        """
        This is the code of open Enter Tutorial of Deathmatch by hardcode the mouse location
        This code only work on pc with the screen resolution is 1980 x 1080
        The code need to run after enter the game of TheTan Arena
        """
        pyautogui.moveTo(1347,989,1)  
        pyautogui.leftClick()
        time.sleep(2)
        
        pyautogui.dragTo(300, 400, 2, button='left')
        time.sleep(2)
        
        pyautogui.moveTo(1451,317,2)
        pyautogui.leftClick()
        time.sleep(2)
        
        pyautogui.moveTo(948,754,2)
        pyautogui.leftClick()
    
    def _end_game(self):
        """
        This is the code for end game
    """
        self.p.terminate()
    
    def _reset_game(self):
        pass

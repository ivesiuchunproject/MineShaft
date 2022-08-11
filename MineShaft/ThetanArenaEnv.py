import os
import time
import subprocess

import mss
import numpy as np
import pyautogui
import cv2
import pygetwindow as gw

from .BaseEnv import BaseEnv
from cv_matching import cv_matching

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=BaseEnv.IO_MODE.FULL_CONTROL,
                 explore_space=BaseEnv.EXPLORE_MODE.FULL):
        """This is the code of start game

        Use try and catch statement to catch exception
        when the game is not installed in the provided path,
        then raise the exception for the upper level to handle.

        The hardcode path to open the game:
        "C:\Program Files (x86)\Thetan Arena\Thetan Arena.exe"
        """
        super(ThetanArenaEnv, self).__init__()

        try:
            self._start_game()
        except:
            raise Exception("the game is not installed")
        
        if io_mode == IO_MODE.FULL_CONTROL:
            # obs_shape in (HEIGHT, WIDTH, N_CHANNELS)
            obs_shape = (512, 512, 4)
            self.observation_space = spaces.Box(low=0, high=255,
                                                shape=obs_shape,
                                                dtype=np.uint8)

            gameWindow = gw.getWindowsWithTitle('Thetan Arena')[0]
            monitor = {"top": gameWindow.top,
                       "left": gameWindow.left,
                       "width": gameWindow.width,
                       "height": gameWindow.height}

            self.sct = mss.mss()
            img = np.array(self.sct.grab(self.monitor))
            ratio = max(img.shape) // 512
            self.dsize = (img.shape[1] // ratio,
                          img.shape[0] // ratio)
            self.left_right_pad = (obs_shape[1] - self.dsize[1]) // 2
            self.top_bottom_pad = (obs_shape[0] - self.dsize[0]) // 2

        return self.action_space, self.observation_space

    def step(self, action):
        pass

    def reset(self):
        pass

    def close(self):
        pass

    def _take_action(self, action):
        pass

    def _screen_cap(self):
        """This is the function to capture screen from the game Thetan Arena.

        `pygetwindow` is used to get the coordinates and resolution of game
        by matching with WindowsWithTitle('Thetan Arena').
        
        The image will then be resized to the specified size defined in 
        `observation_space` with the same ratio as original image by padding
        with black pixels.

        Returns
        -------
        numpy.array
            Captured RGBA image with format of numpy.array in HWC
        
        """
        img = np.array(self.sct.grab(self.monitor))
        img = cv2.resize(img, self.dsize)
        return cv2.copyMakeBorder(img,
                                  self.top_bottom_pad,
                                  self.top_bottom_pad,
                                  self.left_right_pad,
                                  self.left_right_pad,
                                  cv2.BORDER_CONSTANT,
                                  value=[0, 0, 0])

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
        """This is the code for starting game

        The file path "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe"
        and
        program name "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe"
        is hardcode.
        """

        progname = "C:\\Users\\Public\\Desktop\\Thetan Arena"
        filepath = "C:\\Program Files (x86)\\Thetan Arena\\Thetan Arena.exe"

        self.p = subprocess.Popen([filepath, progname])

    def _enter_match(self):
        """
        change the current directory to the script folder so that relative
        path can be used
        """
        folder_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(folder_path)

        """
        opencv read the find match image by file path
        """

        tofind = cv2.imread(
            "../SourcePictures/findmatch2.png", cv2.IMREAD_UNCHANGED)

        """
        using the above method
        """
        loc, thershold = cv_matching.matching_with_screencap(tofind)

        """
        using pyautogui to click the obtained coordinates
        """
        pyautogui.moveTo(loc[0] - 100, loc[1], duration=0.2)
        pyautogui.click(button="left", duration=0.2)

        """
        similarly, using pyautogui to click the obtained coordinates
        """

        tofind = cv2.imread(
            "../SourcePictures/deathmatch2.png", cv2.IMREAD_UNCHANGED)
        loc2, thershold = cv_matching.matching_with_screencap(tofind)
        if thershold > 0.7:
            pyautogui.moveTo(loc2[0] + 250, loc2[1], duration=0.2)
            pyautogui.click(button="left", duration=0.2)

        else:
            pyautogui.dragTo(loc[0] - 400, loc[1], duration=0.2, button="left")
            tofind = cv2.imread(
                "../SourcePictures/deathmatch2.png",
                cv2.IMREAD_UNCHANGED)
            time.sleep(2)
            loc2, thershold = cv_matching.matching_with_screencap(tofind)
        if thershold < 0.6:
            print("no deathmatch game mode")
            exit()
        pyautogui.moveTo(loc2[0] + 250, loc2[1], duration=0.2)
        pyautogui.click(button="left", duration=0.2)

        """
        again, using the above method to find and click the tutorial image
        """

        tofind = cv2.imread("../SourcePictures/tutor.png", cv2.IMREAD_UNCHANGED)
        loc, thershold = matching_with_screencap(tofind)
        pyautogui.moveTo(loc[0], loc[1], duration=0.2)
        pyautogui.click(button="left", duration=0.2)

        """
        Determine if the Tutorial has started
        """

        """
        opencv read the image by file path for matching
        """
        tofind = cv2.imread(
            "../SourcePictures/entertutor2.png", cv2.IMREAD_UNCHANGED)
        """
        wait for 5 seconds as the game maybe loading
        """
        time.sleep(5)
        """
        time.time() return the current time
        start_time store the current time
        """
        start_time = time.time()
        """
        set a boolean to determind if the tutorial game is started
        """
        tutor_started = False
        """
        use a while loop to keep matching the screen capture and the required image
        the loop will go on at most 20 seconds
        if there is no match with thershold larger than 0.7 after 20seconds,
        it is determinded that the tutorial is not started
        """
        while time.time() - start_time < 20 and not tutor_started:
            loc, thershold = cv_matching.matching_with_screencap(tofind)
            if thershold > 0.7:
                tutor_started = True

        """
        Determine if the Tutorial has finished

        only run if the tutorial is started
        """
        if tutor_started:
            """
            since the game last for 3 minites, the matching will start after that
            """
            time.sleep(180)
            """
            opencv read the image by file path for matching
            """

            tofind = cv2.imread(
                "../SourcePictures/finishtutor.png",
                cv2.IMREAD_UNCHANGED)

            """
            similarly, set a boolean to determind if the game is finished and
            record the time
            """

            start_time = time.time()
            tutor_ended = False

        """

        use a while loop to keep matching the screen capture and the required image
        the loop will go on at most 60 seconds
        if there is no match with thershold larger than 0.7 after 60seconds,
        it is determinded that the tutorial is not finished

        """

        while time.time() - start_time < 60 and not tutor_ended:
            loc, thershold = matching_with_screencap(tofind)
            if thershold > 0.7:
                tutor_ended = True

    def _end_game(self):
        """
        This is the code for end game
        """
        self.p.terminate()

    def _reset_game(self):
        pass

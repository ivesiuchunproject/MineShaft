from .BaseEnv import BaseEnv
import subprocess
import os
import time
import os
import numpy as np
import pyautogui
import cv2 as cv
from cv_matching import cv_matching


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

        tofind = cv.imread(
            "../SourcePictures/findmatch2.png", cv.IMREAD_UNCHANGED)

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

        tofind = cv.imread(
            "../SourcePictures/deathmatch2.png", cv.IMREAD_UNCHANGED)
        loc2, thershold = cv_matching.matching_with_screencap(tofind)
        if thershold > 0.7:
            pyautogui.moveTo(loc2[0] + 250, loc2[1], duration=0.2)
            pyautogui.click(button="left", duration=0.2)

        else:
            pyautogui.dragTo(loc[0] - 400, loc[1], duration=0.2, button="left")
            tofind = cv.imread(
                "../SourcePictures/deathmatch2.png",
                cv.IMREAD_UNCHANGED)
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

        tofind = cv.imread("../SourcePictures/tutor.png", cv.IMREAD_UNCHANGED)
        loc, thershold = matching_with_screencap(tofind)
        pyautogui.moveTo(loc[0], loc[1], duration=0.2)
        pyautogui.click(button="left", duration=0.2)

        """
        Determine if the Tutorial has started
        """

        """
        opencv read the image by file path for matching
        """
        tofind = cv.imread(
            "../SourcePictures/entertutor2.png", cv.IMREAD_UNCHANGED)
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

            tofind = cv.imread(
                "../SourcePictures/finishtutor.png",
                cv.IMREAD_UNCHANGED)

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

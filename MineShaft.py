import cv2
import pyautogui
import numpy as np
from mss.windows import MSS as mss


class MineShaft:
    def __init__(self):
        self.sct=mss()
		width, height= pyautogui.size()
		monitor = {
			"top": (height-360)//2,
			"left": (width-640)//2,
			"width": 640,
			"height": 360
		}
        # start the game

    def step(self, action):
        self._take_action(action)
        reward = self._get_reward()
        ob = np.array(sct.grab(monitor))
        episode_over = False
        return ob, reward, episode_over, {}

    def _reset(self):
        pass

    def _take_action(self, action):
    	# [W, S, A, D, E, R, F, left_click, screen_X, screen_Y]
        pass

    def _get_reward(self):
        """ Reward is given for XY. """
        if self.status == FOOBAR:
            return 1
        elif self.status == ABC:
            return self.somestate ** 2
        else:
            return 0

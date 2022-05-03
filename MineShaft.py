"""This is the base class of the MineShaft environment. It inherited OpenAI Gym Environment.

For any game supported by MineShaft, the environment inherited this class as an interface.
"""
from enum import Enum

import gym
from gym import spaces

class BaseEnv(gym.Env):
    """Custom Environment that follows gym interface
    
    Attributes
    ----------
    IO_MODE : Enum
        IO_MODE.API = direct access to game API
	IO_MODE.SIMPLIFIED = simpilified observation_space and action_space
	IO_MODE.FULL_CONTROL = screen and full keyboard and mouse control
    """
    metadata = {'render.modes': ['human']}
    IO_MODE = Enum('IO_MODE', ('API', 'SIMPLIFIED', 'FULL_CONTROL'))

    def __init__(self, io_mode=IO_MODE.FULL_CONTROL):
        super(CustomEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input:
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(HEIGHT, WIDTH, N_CHANNELS), dtype=np.uint8)

    def step(self, action):
        self._take_action(action)
        reward = self._get_reward()
        ob = np.array(sct.grab(monitor))
        episode_over = False
	info = {}
        return observation, reward, done, info

    def reset(self):
        ...
        return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        pass

    def close (self):
        ...

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

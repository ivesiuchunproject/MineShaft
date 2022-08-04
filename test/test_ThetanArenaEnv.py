import time
import unittest

import numpy as np
import pyautogui
import keyboard

from MineShaft.ThetanArenaEnv import ThetanArenaEnv

class ThetanArenaEnvTestCase(unittest.TestCase):
	def setUp(self):
		self.mouse_x_y = (0.3, 0.6)
		self.env = ThetanArenaEnv()

	def tearDown(self):
		self.mouse_x_y = None

	def test__mouse_move(self):
		"""Test case for mouse move method
		
		The function will call mouse move method of `ThetanArenaEnv` with
		parameters `x=0.3, y=0.6` of the screen. Then check if the mouse
		coordinate now moved to the expected `(x, y)` location.
		
		(Cannot test correctly if `(x, y)` definition changed to reletive
		coordinate of game window)
		"""
		expected = np.asarray(pyautogui.size()) * np.asarray(self.mouse_x_y);
		self.env._mouse_move(self.mouse_x_y);
		result = np.asarray(pyautogui.position());
		self.assertTrue(np.abs(expected - result) < 2);

	def test__mouse_click(self):
		"""Test case for mouse clikc method

		There is no way to determine if the click, press, release works well.
		Assume if no error occur is good then pass the test.
		"""
		self.env._mouse_click(False, True);
		self.env._mouse_click(True, False);
		self.env._mouse_click(True, True);
		self.env._mouse_click(False, False);
		self.env._mouse_press(True, False);
		self.env._mouse_release(True, False);
		self.env._mouse_press(False, True);
		self.env._mouse_release(False, True);

	def test__mouse_drag(self):
		"""Test case for mouse drag (combination of mouse action)

		There is no way to determine if the combination works well.
		Assume if no error occur is good then pass the test.
		"""
		self.env._mouse_press(True, False);
		expected = np.asarray(pyautogui.size()) * np.asarray(self.mouse_x_y);
		self.env._mouse_move(self.mouse_x_y);
		self.env._mouse_release(True, False);
		self.env._mouse_press(False, True);
		expected = np.asarray(pyautogui.size()) * np.asarray(self.mouse_x_y);
		self.env._mouse_move(self.mouse_x_y);
		self.env._mouse_release(False, True);
		
	def test__keyboard_input(self):
		"""Test case for keyboard input

		The test case will try to press "a" and "ctrl + a".
		And use `keyboard` to detect if the key is pressed as the function
		of `_keyboard_press` is designed to be.

		Notes
		-------
			The keyboard input action is a 1D matrix of float value with
			length `133`. Each value in the matrix represent the force
			pressed on the following keys on the keyboard (in the same
			sequence).
			```
			[
				'!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+',
				',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6',
				'7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[',
				'\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e','f',
				'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
				'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|',
				'}', '~', 'altleft', 'altright', 'backspace', 'capslock',
				'ctrlleft', 'ctrlright', 'delete', 'divide', 'down', 'end',
				'enter', 'esc', 'escape', 'f1', 'f10', 'f11', 'f12', 'f13',
				'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21',
				'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
				'insert', 'left', 'multiply', 'num0', 'num1', 'num2', 'num3',
				'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock',
				'pagedown', 'pageup', 'pause', 'right', 'shiftleft',
				'shiftright', 'space', 'stop', 'subtract', 'tab',
				'up', 'command', 'optionleft', 'optionright'
			]
			```
			The value of force will be in range `0` to `1` and it is considered
			to be pressed down only if the value is larger than `0.5`.
		"""
		action_a = np.zeros((133));
		action_a[38] = 1;
		# press "a"
		self.env._keyboard_press(action_a);
		assert keyboard.is_pressed("a");
		self.env._keyboard_release( 1 - action_a);
		assert not keyboard.is_pressed("a");
		action_ctrl_a = np.zeros((133));
		action_ctrl_a[38] = 1;
		action_ctrl_a[72] = 1;
		# press Ctrl+a
		self.env._keyboard_press(action_ctrl_a);
		assert keyboard.is_pressed('ctrl+a');
		self.env._keyboard_release( 1 - action_ctrl_a);
		assert not keyboard.is_pressed('ctrl+a');

from .BaseEnv import BaseEnv

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=IO_MODE.FULL_CONTROL,
                 explore_space=EXPLORE_MODE.FULL):
        super(ThetanArenaEnv, self).__init__()
        
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
    
    def _mouse_move(self, x, y):
        pass
    
    def _mouse_click(self, left, right):
        pass
    
    def _start_game(self):
        pass
    
    def _end_game(self):
        pass
    
    def _reset_game(self):
        pass

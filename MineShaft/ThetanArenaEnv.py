from .BaseEnv import BaseEnv

class ThetanArenaEnv(BaseEnv):
    def __init__(self, io_mode=IO_MODE.FULL_CONTROL,
                 explore_space=EXPLORE_MODE.FULL):
        super(ThetanArenaEnv, self).__init__()

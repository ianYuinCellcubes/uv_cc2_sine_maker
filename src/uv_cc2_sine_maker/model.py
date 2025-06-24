import numpy as np
'''
Must be add spec file.
    hiddenimports=['numpy', 'numpy._core._exceptions'],
'''

class monitor_info:
    mIndex: int = 0     #  monitor select
    mCount: int = 1     #  How many moniter detect
    mlist: list = []    #  monitor list(data)

class sine_info:
    sCount: int = 0
    sList: list = [255, 0]
    sPeriod: int = 1

    def reset(self):
        self.sCount = 0
        self.sList = [255, 0]
        self.sPeriod = 1

    def print_sine(self):
        _size = self.sPeriod
        _list = []
        for i in range(0, 2*_size):
            _sin_squared = np.sin((i*np.pi)/(2*_size))**2
            _x = 255 * _sin_squared
            _rslt = np.round(_x, 0).astype(int)
            _list.append(_rslt)
        self.sList = _list
        self.sCount = 0
    
    def set_period(self, period):
        self.sPeriod = period
        self.print_sine(self)

    def set_gray_lv(self, index, value):
        self.sList[index] = value

    def get_period(self):
        return self.sPeriod
    
    def shift_right(self):
        self.sCount += 1
        if self.sCount > (2 * self.sPeriod):
            self.sCount = 0
    def shift_left(self):
        self.sCount -= 1
        if self.sCount < 0:
            self.sCount = (2 * self.sPeriod)

    def print_frame_pattern(self):
        _pattern = []
        for i in range(0, len(self.sList)):
            _x = self.sCount + i
            if _x > ((2 * self.sPeriod)-1):
                _x = _x - (2 * self.sPeriod)
            _pattern.append(self.sList[_x])
        return _pattern

class DataModel:
    def __init__(self):
        self.data = None
        self.monitor = monitor_info
        self.resolution_x = 1920
        self.resolution_y = 1080
        self.mode = 1
        self.scrolling = False
        self.sine = sine_info

    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    
    def set_monitor_list(self, monitor_list):
        self.monitor.mlist = monitor_list
    def get_monitor_list(self):
        return self.monitor.mlist
    
    def set_monitor_count(self, monitor_count):
        self.monitor.mCount = monitor_count
    def get_monitor_count(self):
        return self.monitor.mCount
    
    def set_monitor_index(self, monitor_index):
        self.monitor.mIndex = monitor_index
    def get_monitor_index(self):
        return self.monitor.mIndex
    
    def set_resolution_x(self, resolution_x):
        self.resolution_x = resolution_x
    def get_resolution_x(self):
        return self.resolution_x
    
    def set_resolution_y(self, resolution_y):
        self.resolution_y = resolution_y
    def get_resolution_y(self):
        return self.resolution_y
    
    def set_mode_x(self):
        self.mode = 1
    def set_mode_y(self):
        self.mode = 0
    def get_mode(self):
        return self.mode
    
    def set_scrolling(self, scrolling):
        self.scrolling = scrolling

    def get_scrolling(self):
        return self.scrolling
    
    def set_sine_reset(self):
        self.sine.reset(self.sine)
    
    def set_sine_period(self, period):
        self.sine.set_period(self.sine, period)
    def get_sine_period(self):
        return self.sine.get_period(self.sine)
    
    def set_sine_shift_right(self):
        self.sine.shift_right(self.sine)
    def set_sine_shift_left(self):
        self.sine.shift_left(self.sine)
    
    def get_sine_list(self):
        return self.sine.sList
    
    def get_frame_pattern(self):
        return self.sine.print_frame_pattern(self.sine)

    def set_gray_lv(self, index, value):
        self.sine.set_gray_lv(self.sine, index, value)
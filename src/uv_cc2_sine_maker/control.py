from src.uv_cc2_sine_maker.model import DataModel
from src.uv_cc2_sine_maker.main_view import MainView
from src.uv_cc2_sine_maker.sub_view import SubView
from src.uv_cc2_sine_maker.screen_reader import Monitor
from PySide6.QtGui import QPixmap, QColor, QPainter, QPen
from PySide6.QtCore import QRect, QTimer

class MainController():
    def __init__(self):
        self.model = DataModel()
        self.view = MainView(self)
        self.sub_view = SubView()
        self.init()

    def init(self):
        self.search_monitor()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_pattern)
        self.timer.start(10)
        # self.make_frame()
        
    def show_main_view(self):
        self.view.show()

    def show_sub_view(self):
        self.sub_view.show()
        
    def ClosedWindow(self):
        self.sub_view.close()

    def on_btn_monitor_detect_clicked(self):
        self.search_monitor()

    def on_cmb_monitor_detect_activated(self, index):
        self.model.set_monitor_index(index)
        self.sub_view.update_monitor(self.model.get_monitor_list()[index])
        
    def on_resolution_x_valueChanged(self, value):
        self.model.set_resolution_x(int(value))
        self.make_frame()

    def on_resolution_y_valueChanged(self, value):
        self.model.set_resolution_y(int(value))
        self.make_frame()

    def on_rbtn_mode_x_toggled(self, checked):
        self.model.set_mode_x()
        self.make_frame()
    
    def on_rbtn_mode_y_toggled(self, checked):
        self.model.set_mode_y()
        self.make_frame()
    
    def on_scrolling_valueChanged(self, value):
        self.model.set_scrolling(value)
    
    def update_pattern(self):
        _flag_scrolling = self.model.get_scrolling()
        if _flag_scrolling:
            self.update_frame()
        else:
            self.make_frame()

    def on_btn_control_add_clicked(self):
        _tmp = self.model.get_sine_period() + 1
        self.model.set_sine_period(_tmp)
        self.view.update_gray_stack(self.model.get_sine_list())
        self.make_frame()
    
    def on_btn_control_sub_clicked(self):
        _tmp = self.model.get_sine_period() - 1
        if _tmp < 1:
            _tmp = 1
        self.model.set_sine_period(_tmp)
        self.view.update_gray_stack(self.model.get_sine_list())
        self.make_frame()

    def on_sb_gl_valueChanged(self, index, value):
        self.model.set_gray_lv(index, value)

    def update_resolution(self):
        _rsl_x = self.model.get_resolution_x()
        _rsl_y =self.model.get_resolution_y()
        _info = self.model.get_monitor_list()[self.model.get_monitor_index()][3]
        self.sub_view.setGeometry(_info[0], _info[1], _rsl_x, _rsl_y)

    def search_monitor(self):
        screen_reader = Monitor
        self.model.set_monitor_list(screen_reader.scanning(screen_reader))
        self.model.set_monitor_count(screen_reader.countMonitor())
        self.view.update_monitor_detect_view(self.model.get_monitor_list())

    def make_frame(self):
        _pattern = self.model.get_frame_pattern()
        _resolution_x = self.model.get_resolution_x()
        _resolution_y = self.model.get_resolution_y()
        _mode = self.model.get_mode()
        _canvas = QPixmap(_resolution_x, _resolution_y)
        _canvas.fill(QColor(0, 0, 0))
        _painter = QPainter(_canvas)
        if _mode == 1: # X
            _i = 0
            while _i < _resolution_y:
                for _j in range(0, len(_pattern)):
                    _gray_box = QRect(0, _i + _j, _resolution_x, 1)
                    _painter.fillRect(_gray_box, QColor(_pattern[_j], _pattern[_j], _pattern[_j]))
                _i = _i + len(_pattern)
        elif _mode == 0: # Y
            _i = 0
            while _i < _resolution_x:
                for _j in range(0, len(_pattern)):
                    _gray_box = QRect(_i + _j, 0, 1, _resolution_y)
                    _painter.fillRect(_gray_box, QColor(_pattern[_j], _pattern[_j], _pattern[_j]))
                _i = _i + len(_pattern)
        _painter.end()
        self.sub_view.update_pixmap(_canvas)
        self.update_resolution()

    def update_frame(self):
        self.model.set_sine_shift_right()
        self.make_frame()
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap, QIcon
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QMainWindow,
    QComboBox,
    QPushButton,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QSpinBox,
    QFrame,
    QCheckBox,
    QGroupBox,
    QRadioButton,
    QScrollArea,
    QSizePolicy
)
'''
rcc -g python .\resource\rcc.qrc -o rcc.py
'''
# from . import rcc
from src.uv_cc2_sine_maker import rcc

class MainView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sine Maker')
        self.setWindowIcon(QIcon(':/logo.ico'))

        # self.setWindowIcon(QIcon('../../resource/logo.ico'))

        _lbl_logo = QLabel()
        _pixmap_logo = QPixmap(':/cellcubes_001.png').scaledToHeight(600)
        _lbl_logo.setPixmap(_pixmap_logo)

        vbox = QVBoxLayout()
        self.mdV = monitor_detect_view(self.controller)
        self.mdV.setMaximumHeight(150)
        self.mV = monitor_view(self.controller)
        self.mV.setMaximumHeight(250)
        self.pV = pattern_view(self.controller)
        self.pV.setMaximumHeight(300)
        self.sV = SineInfo_view(self.controller)

        vbox.addWidget(self.mdV)
        vbox.addWidget(QHLine())
        vbox.addWidget(self.mV)
        vbox.addWidget(QHLine())
        vbox.addWidget(self.pV)
        vbox.addWidget(QHLine())
        vbox.addWidget(self.sV)
        vbox.setContentsMargins(0,0,0,0)

        wgt_vbox = QWidget()
        wgt_vbox.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(_lbl_logo)
        hbox.addWidget(wgt_vbox)

        widget = QWidget()
        widget.setLayout(hbox)

        self.setCentralWidget(widget)
        self.setGeometry(200, 200, 400, 300)

    def closeEvent(self, e):
        self.controller.ClosedWindow()

    def update_monitor_detect_view(self, monitor_list):
        self.mdV.update_monitor_detect_view(monitor_list)
    
    def update_gray_stack(self, slist):
        self.sV.update_gray_stack(slist)

class monitor_detect_view(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()
    
    def initUI(self):
        _vbox = QVBoxLayout()
        _vbox.addWidget(self.monitor_detect_bar())

        self.setLayout(_vbox)

    def monitor_detect_bar(self):
        _lbl_monitor_detect = QLabel("Monitor Select")
        self.cmb_monitor_detect = QComboBox(self)
        self.cmb_monitor_detect.activated[int].connect(self.on_cmb_monitor_detect_activated)
        self.cmb_monitor_detect.setMaximumHeight(40)

        _btn_monitor_detect = QPushButton("Search")
        _btn_monitor_detect.clicked.connect(self.on_btn_monitor_detect_clicked)
        _btn_monitor_detect.setMaximumHeight(40)
        _btn_monitor_detect.setMaximumWidth(100)

        _MD_h_layout = QHBoxLayout()
        _MD_h_layout.addWidget(self.cmb_monitor_detect)
        _MD_h_layout.addWidget(_btn_monitor_detect)
        
        _wgt_MD_h_layout = QWidget()
        _wgt_MD_h_layout.setLayout(_MD_h_layout)
        
        _MD_layout = QVBoxLayout()
        _MD_layout.addWidget(_lbl_monitor_detect)
        _MD_layout.addWidget(_wgt_MD_h_layout)
        _MD_layout.setContentsMargins(0, 0, 0, 0)
        _MD_layout.setSpacing(0)

        _wgt_MD_layout = QWidget()
        _wgt_MD_layout.setLayout(_MD_layout)

        return _wgt_MD_layout

    def on_cmb_monitor_detect_activated(self, index):
        self.controller.on_cmb_monitor_detect_activated(index)
    
    def on_btn_monitor_detect_clicked(self):
        self.controller.on_btn_monitor_detect_clicked()

    def update_monitor_detect_view(self, monitor_list):
        self.cmb_monitor_detect.clear()
        print(monitor_list)
        for i in range(len(monitor_list)):
            self.cmb_monitor_detect.addItem(monitor_list[i][1].lstrip("\\\\.\\"), userData=i)


class monitor_view(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        _vbox = QVBoxLayout()
        _vbox.addWidget(self.monitor_bar())

        self.setLayout(_vbox)

    def monitor_bar(self):
        _lbl_monitor = QLabel("Monitor")

        _lbl_resolution = QLabel("Resolution \t X:")
        self.resolution_x = QSpinBox()
        self.resolution_x.setAlignment(Qt.AlignCenter)
        self.resolution_x.setRange(1, 10000)
        self.resolution_x.setValue(1920)
        self.resolution_x.setSingleStep(1)
        self.resolution_x.setSuffix("px")
        self.resolution_x.valueChanged.connect(self.on_resolution_x_valueChanged)
        
        _lbl_resolution_y = QLabel("\t Y:")
        self.resolution_y = QSpinBox()
        self.resolution_y.setAlignment(Qt.AlignCenter)
        self.resolution_y.setRange(1, 10000)
        self.resolution_y.setValue(1080)
        self.resolution_y.setSingleStep(1)
        self.resolution_y.setSuffix("px")
        self.resolution_y.valueChanged.connect(self.on_resolution_y_valueChanged)

        _h_layout = QHBoxLayout()
        _h_layout.addWidget(_lbl_resolution)
        _h_layout.addWidget(self.resolution_x)
        _h_layout.addWidget(_lbl_resolution_y)
        _h_layout.addWidget(self.resolution_y)

        _wgt_h_layout = QWidget()
        _wgt_h_layout.setLayout(_h_layout)

        _v_layout = QVBoxLayout()
        _v_layout.addWidget(_lbl_monitor)
        _v_layout.addWidget(_wgt_h_layout)

        _wgt_v_layout = QWidget()
        _wgt_v_layout.setLayout(_v_layout)

        return _wgt_v_layout
    
    def on_resolution_x_valueChanged(self, value):
        self.controller.on_resolution_x_valueChanged(value)
    
    def on_resolution_y_valueChanged(self, value):
        self.controller.on_resolution_y_valueChanged(value)

class pattern_view(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        _vbox = QVBoxLayout()
        _vbox.addWidget(self.option_bar())
        _vbox.setContentsMargins(0,0,0,0)
        _vbox.setSpacing(0)

        self.setLayout(_vbox)

    def option_bar(self):
        _lbl_option = QLabel("Option")

        _group_box = QGroupBox()
        _lbl_mode = QLabel("Mode")
        self.rbtn_mode_x = QRadioButton("X", _group_box)
        self.rbtn_mode_y = QRadioButton("Y", _group_box)

        _h_layout_1 = QHBoxLayout()
        _h_layout_1.addWidget(_lbl_mode)
        _h_layout_1.addWidget(self.rbtn_mode_x)
        _h_layout_1.addWidget(self.rbtn_mode_y)
        _group_box.setLayout(_h_layout_1)

        self.rbtn_mode_x.toggled.connect(self.on_rbtn_mode_x_toggled)
        self.rbtn_mode_y.toggled.connect(self.on_rbtn_mode_y_toggled)
        self.rbtn_mode_x.setChecked(True)

        _lbl_scrolling = QLabel("Scroll")
        self.scrolling = QCheckBox()
        self.scrolling.setChecked(False)
        self.scrolling.checkStateChanged.connect(self.on_scrolling_valueChanged)

        _h_layout_2 = QHBoxLayout()
        _h_layout_2.addWidget(_lbl_scrolling)
        _h_layout_2.addWidget(self.scrolling)

        _wgt_h_layout_1 = QWidget()
        _wgt_h_layout_1.setLayout(_h_layout_1)
        _wgt_h_layout_2 = QWidget()
        _wgt_h_layout_2.setLayout(_h_layout_2)

        _v_layout = QVBoxLayout()
        _v_layout.addWidget(_lbl_option)
        # _v_layout.addWidget(_group_box)
        _v_layout.addWidget(_wgt_h_layout_1)
        _v_layout.addWidget(_wgt_h_layout_2)

        _wgt_v_layout = QWidget()
        _wgt_v_layout.setLayout(_v_layout)

        return _wgt_v_layout
    
    def on_rbtn_mode_x_toggled(self, checked):
        self.controller.on_rbtn_mode_x_toggled(checked)
    
    def on_rbtn_mode_y_toggled(self, checked):
        self.controller.on_rbtn_mode_y_toggled(checked)
    
    def on_scrolling_valueChanged(self, value):
        if value == Qt.CheckState.Checked:
            self.controller.on_scrolling_valueChanged(True)
        elif value == Qt.CheckState.Unchecked:
            self.controller.on_scrolling_valueChanged(False)

class SineInfo_view(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        _vbox = QVBoxLayout()
        _vbox.addWidget(self.sine_info_bar())

        self.setLayout(_vbox)

    def sine_info_bar(self):
        _lbl_sine_info = QLabel("Sine Info")

        _lbl_control = QLabel("Control")
        _btn_control_add = QPushButton("+")
        _btn_control_sub = QPushButton("-")

        _btn_control_add.clicked.connect(self.on_btn_control_add_clicked)
        _btn_control_sub.clicked.connect(self.on_btn_control_sub_clicked)

        _h_layout_1 = QHBoxLayout()
        _h_layout_1.addWidget(_lbl_control)
        _h_layout_1.addWidget(_btn_control_add)
        _h_layout_1.addWidget(_btn_control_sub)

        _wgt_h_layout_1 = QWidget()
        _wgt_h_layout_1.setLayout(_h_layout_1)

        wgt_gray_stack = QWidget()
        self.sb_grayLv:list = []
        for i in range(0,2):
            sb_gl_tmp = QSpinBox()
            color = 0
            t_color = 255
            if i < 1:
                color = 255
                t_color = 0
            sb_gl_tmp.setStyleSheet(f"QSpinBox {{background-color : rgb({color},{color},{color}); font:bold; color : rgb({t_color},{t_color},{t_color});}}")
            sb_gl_tmp.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
            sb_gl_tmp.setRange(0, 255)
            sb_gl_tmp.setValue(color)
            sb_gl_tmp.setObjectName(f"gl{i}")
            sb_gl_tmp.valueChanged.connect(self.on_sb_gl_valueChanged)
            self.sb_grayLv.append(sb_gl_tmp)

        self.lyt_gray_stack = QVBoxLayout(wgt_gray_stack)
        for j in range(0, 2):
            self.lyt_gray_stack.addWidget(self.sb_grayLv[j])

        _qsa_gray_stack = QScrollArea()
        _qsa_gray_stack.setWidgetResizable(True)
        _qsa_gray_stack.setWidget(wgt_gray_stack)
        _qsa_gray_stack.setMinimumHeight(200)

        _v_layout = QVBoxLayout()
        _v_layout.addWidget(_lbl_sine_info, 1)
        _v_layout.addWidget(_wgt_h_layout_1, 1)
        _v_layout.addWidget(_qsa_gray_stack, 1)
        # _v_layout.addWidget(qsa)

        _wgt_v_layout = QWidget()
        _wgt_v_layout.setLayout(_v_layout)

        return _wgt_v_layout
    
    def update_gray_stack(self, slist):
        for i in reversed(range(self.lyt_gray_stack.count())):
            self.lyt_gray_stack.itemAt(i).widget().deleteLater()
        count = 0
        self.sb_gl = []
        for i in slist:
            self.sb_gl.append(QSpinBox())
            self.sb_gl[count].setObjectName(f"gl{count}")
            self.sb_gl[count].valueChanged.connect(self.on_sb_gl_valueChanged)
            color = 0
            if i < 120:
                color = 255
            self.sb_gl[count].setStyleSheet(f"QSpinBox {{background-color : rgb({i},{i},{i}); font:bold; color : rgb({color},{color},{color});}}")
            self.sb_gl[count].setRange(0, 255)
            self.sb_gl[count].setValue(i)
            self.lyt_gray_stack.addWidget(self.sb_gl[count])
            count = count + 1
    
    def on_sb_gl_valueChanged(self, value):
        self.controller.on_sb_gl_valueChanged(int(self.sender().objectName().lstrip("gl")), value)
        color = 0
        if value < 120:
            color = 255
        self.sender().setStyleSheet(f"QSpinBox {{background-color : rgb({value},{value},{value}); font:bold; color : rgb({color},{color},{color});}}")

    def on_btn_control_add_clicked(self):
        self.controller.on_btn_control_add_clicked()
    
    def on_btn_control_sub_clicked(self):
        self.controller.on_btn_control_sub_clicked()
    
    def update_sine_info_view(self, sine_info):
        self.controller.update_sine_info_view(sine_info)

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setContentsMargins(0,0,0,0)
        self.setMaximumHeight(30)

class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
        self.setContentsMargins(0, 0, 0, 0)
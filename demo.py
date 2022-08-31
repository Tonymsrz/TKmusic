from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from pygame import mixer
import sys
from time import sleep
from eyed3 import load
from subprocess import call
from ast import literal_eval
from bs4 import BeautifulSoup
try:
    from PyQt5.QtWidgets import QLabel, QListWidgetItem, QLineEdit, QComboBox, QMenu, QAction, QMainWindow, QWidget, \
    QGridLayout, QTabWidget, QListWidget, QPushButton, QProgressBar, QMessageBox, QApplication, QFileDialog, \
    QStatusBar, QGraphicsOpacityEffect
    from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QMutex, QRect, QPoint, Qt, QSize
    from PyQt5.QtGui import QIcon, QPixmap, QCursor
except:
    call('pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com pyqt5')
    from PyQt5.QtWidgets import QLabel, QListWidgetItem, QLineEdit, QComboBox, QMenu, QAction, QMainWindow, QWidget, \
        QGridLayout, QTabWidget, QListWidget, QPushButton, QProgressBar, QMessageBox, QApplication, QFileDialog
    from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QMutex, QRect, QPoint, Qt, QSize
    from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtCore import QTimer, QThread, pyqtSignal, QMutex, QRect, QPoint, Qt, QSize
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from requests import post, get
from os import getenv, mkdir, makedirs, remove, listdir
from PIL import Image, ImageDraw, ImageFilter
from mutagen import File
from shutil import copyfile, rmtree
from threading import Thread
from decimal import Decimal
from jsonpath import jsonpath

SongPath = []  # 本地音乐的路径
num = 0
bo = ''  # boing, boed, love
apdata = getenv("APPDATA")
data = str(apdata) + '\music'
urls = []
lrcs = []
picd = []

big = False

SongName = []
typerr = ''
list_confident = 'boing'
num_m = 0
lrcd = []
path = ''
number = 1

stop = False
num = 0
voice = 0.5
pause = False
big = False
music = []
urls = []
songs = []
type = 'kugou'
name = ''
downloading = False
page = 5
id = []
proxies = {}
nowatime = 0
songed = []
urled = []
bo = ''
pic = []
picd = []
qmut = QMutex()
lrcs = []
lrct = []
paing = False
tryed = 0
apdata = getenv("APPDATA")
data = str(apdata) + '\music'
print(data)
to = ''
timenum = 0
start = False
loves = []
loveurls = []
lovepics = []
lovelrc = []
namem = ''
play = 'shun'  # 默认播放模式为顺序播放
stop = False
filew = 1
num = 0
voice = 0.5
pause = False
asas = 1
picno = False
big = False
stopdown = False


class MyQLabel(QtWidgets.QLabel):

    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()
        self.setCursor(QCursor(Qt.PointingHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        pass

    def mousePressEvent(self, event):
        self.setCursor(QCursor(Qt.ArrowCursor))

    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class WorkThread(QThread):
    # 自定义信号对象。参数str就代表这个信号可以传一个字符串
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(WorkThread, self).__init__()

    def run(self):
        global to
        global number
        global path
        global downloading
        global pic
        global lrct
        global lrcd
        global picno
        global stopdown
        if bo == 'boing':
            try:
                proxies = {
                    'http': 'http://124.72.109.183:8118',
                    ' Shttp': 'http://49.85.1.79:31666'

                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'}
                # 处理图片
                try:
                    try:
                        try:
                            aq = pic[num]
                            aqq = aq.split('/')

                        except:
                            pass

                        if type == 'kugou' and len(aqq) - 1 == 6:  # 酷狗
                            aqqe = str(aqq[0]) + str('//') + str(aqq[2]) + str('/') + str(aqq[3]) + str('/') + str(
                                '400') + str('/') + str(aqq[5]) + str('/') + str(aqq[6])
                            print(aqqe)
                        elif type == 'netease' and len(aqq) - 1 == 4:  # 网易
                            aqn = aq.split('?')
                            b = '?param=500x500'
                            aqqe = (str(aqn[0]) + str(b))
                            print(aqqe)
                        else:
                            aqqe = pic[num]
                        req = get(aqqe)

                        checkfile = open(str(data + '/ls1.png'), 'w+b')
                        for i in req.iter_content(100000):
                            checkfile.write(i)

                        checkfile.close()
                        lsfile = str(data + '/ls1.png')
                        safile = str(data + '/back.png')
                        draw(lsfile, safile)
                        picno = True
                    except:
                        print('图片下载错误')
                        picno = False
                        pass
                    url1 = urls[num]
                    print(url1)
                    number = number + 1
                    path = str(data + '\{}.临时文件'.format(number))
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.110.430.128 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                    # 下载歌曲
                    with get(url1, stream=True, headers=headers) as r, open(path, 'wb') as file:
                        total_size = int(r.headers['content-length'])
                        content_size = 0
                        for content in r.iter_content(chunk_size=1024):
                            if not stopdown:
                                file.write(content)
                                content_size += len(content)
                                plan = (content_size / total_size) * 100
                                # print(int(plan))
                                develop = str(int(plan)) + str('%')
                                self.trigger.emit(str(develop))
                            else:
                                print('stopdown')
                                break

                            stopdown = False

                    to = 'downloadmusic\{}.mp3'.format(songs[num])
                    makedirs('downloadmusic', exist_ok=True)
                except:
                    pass
                try:
                    if bo == 'boing':
                        lrct = []
                        f = lrcs[num]  # 按行读取
                        # print (f)
                        lines = f.split('\n')
                        # print (lines)
                        # 处理歌词
                        if not lines == ['']:
                            for i in lines:
                                if not i == '':
                                    line1 = i.split('[')
                                    try:
                                        line2 = line1[1].split(']')
                                        if line2 == '':
                                            pass
                                        else:
                                            linew = line2[1]
                                            # print(linew)
                                            lrct.append(linew)
                                        self.trigger.emit(str('lrcfinish'))
                                    except:
                                        print('{}的歌词错误'.format(str(line1)))
                                else:
                                    pass
                        else:
                            self.trigger.emit(str('lrcnofinish'))
                            print('没有歌词')
                except:
                    print('歌词错误')

                try:
                    copyfile(path, to)
                except:
                    pass
                downloading = False
                self.trigger.emit(str('finish'))

            except:
                self.trigger.emit(str('nofinish'))
        elif bo == 'boed':
            try:
                proxies = {
                    'http': 'http://124.72.109.183:8118',
                    'http': 'http://49.85.1.79:31666'

                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'}
                try:
                    try:
                        try:
                            aq = picd[num]
                            aqq = aq.split('/')

                        except:
                            pass
                        if type == 'kugou' and len(aqq) - 1 == 6:
                            aqqe = str(aqq[0]) + str('//') + str(aqq[2]) + str('/') + str(aqq[3]) + str('/') + str(
                                '400') + str('/') + str(aqq[5]) + str('/') + str(aqq[6])
                            print(aqqe)
                        elif type == 'netease' and len(aqq) - 1 == 4:
                            aqn = aq.split('?')
                            b = '?param=500x500'
                            aqqe = (str(aqn[0]) + str(b))
                            print(aqqe)
                        else:
                            aqqe = picd[num]
                        req = get(aqqe)

                        checkfile = open(str(data + '/ls1.png'), 'w+b')
                        for i in req.iter_content(100000):
                            checkfile.write(i)

                        checkfile.close()
                        lsfile = str(data + '/ls1.png')
                        safile = str(data + '/back.png')
                        draw(lsfile, safile)
                        picno = True
                    except:
                        print('图片下载错误')
                        picno = False
                        pass

                    url1 = urled[num]
                    print(url1)
                    # os.makedirs('music', exist_ok=True)
                    number = number + 1
                    path = str(data + '\{}.临时文件'.format(number))
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.110.430.128 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                    with get(url1, stream=True, headers=headers) as r, open(path, 'wb') as file:
                        total_size = int(r.headers['content-length'])
                        content_size = 0
                        for content in r.iter_content(chunk_size=1024):
                            if not stopdown:
                                file.write(content)
                                content_size += len(content)
                                plan = (content_size / total_size) * 100
                                # print(int(plan))
                                develop = str(int(plan)) + str('%')
                                self.trigger.emit(str(develop))
                            else:
                                print('down')
                                break
                        stopdown = False
                    to = 'downloadmusic\{}.mp3'.format(songed[num])
                    makedirs('downloadmusic', exist_ok=True)
                except:
                    self.trigger.emit(str('nofinish'))
                    pass

                try:

                    lrct = []
                    f = lrcd[num]  # 按行读取
                    # print(f)
                    lines = f.split('\n')
                    # print(lines)
                    for i in lines:
                        line1 = i.split('[')
                        try:
                            line2 = line1[1].split(']')
                            if line2 == '':
                                pass
                            else:
                                linew = line2[1]
                                # print(linew)
                                lrct.append(linew)
                            self.trigger.emit(str('lrcfinish'))
                        except:
                            print('歌词错误')

                except:
                    pass

                try:
                    copyfile(path, to)
                except:
                    pass
                downloading = False
                self.trigger.emit(str('finish'))

            except:
                self.trigger.emit(str('nofinish'))
        elif bo == 'love':
            try:
                proxies = {
                    'http': 'http://124.72.109.183:8118',
                    'http': 'http://49.85.1.79:31666'

                }
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'}
                try:
                    try:
                        try:
                            aq = lovepics[num]
                            aqq = aq.split('/')

                        except:
                            pass
                        if type == 'kugou' and len(aqq) - 1 == 6:
                            aqqe = str(aqq[0]) + str('//') + str(aqq[2]) + str('/') + str(aqq[3]) + str('/') + str(
                                '400') + str('/') + str(aqq[5]) + str('/') + str(aqq[6])
                            print(aqqe)
                        elif type == 'netease' and len(aqq) - 1 == 4:
                            aqn = aq.split('?')
                            b = '?param=500x500'
                            aqqe = (str(aqn[0]) + str(b))
                            print(aqqe)
                        else:
                            aqqe = lovepics[num]
                        req = get(aqqe)

                        checkfile = open(str(data + '/ls1.png'), 'w+b')
                        for i in req.iter_content(100000):
                            checkfile.write(i)

                        checkfile.close()
                        lsfile = str(data + '/ls1.png')
                        safile = str(data + '/back.png')
                        draw(lsfile, safile)
                        picno = True
                    except:
                        print('图片错误')
                        picno = False
                        pass

                    url1 = loveurls[num]
                    print(url1)
                    # os.makedirs('music', exist_ok=True)
                    number = number + 1
                    path = str(data + '\{}.临时文件'.format(number))
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.110.430.128 Safari/537.36',
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                    with get(url1, stream=True, headers=headers) as r, open(path, 'wb') as file:
                        total_size = int(r.headers['content-length'])
                        content_size = 0
                        for content in r.iter_content(chunk_size=1024):
                            if not stopdown:
                                file.write(content)
                                content_size += len(content)
                                plan = (content_size / total_size) * 100
                                # print(int(plan))
                                develop = str(int(plan)) + str('%')
                                self.trigger.emit(str(develop))
                            else:
                                print('down')
                                break
                        stopdown = False
                    to = 'downloadmusic\{}.mp3'.format(songed[num])
                    makedirs('downloadmusic', exist_ok=True)
                except:
                    self.trigger.emit(str('nofinish'))
                    pass

                try:

                    lrct = []
                    f = lovelrc[num]  # 按行读取
                    # print(f)
                    lines = f.split('\n')
                    # print(lines)
                    for i in lines:
                        line1 = i.split('[')
                        try:
                            line2 = line1[1].split(']')
                            if line2 == '':
                                pass
                            else:
                                linew = line2[1]
                                # print(linew)
                                lrct.append(linew)
                            self.trigger.emit(str('lrcfinish'))
                        except:
                            print('歌词错误')
                except:
                    pass

                try:
                    copyfile(path, to)
                except:
                    pass
                downloading = False
                self.trigger.emit(str('finish'))

            except:
                self.trigger.emit(str('nofinish'))


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.RowLength = 0
        # self.setupUi(MainWindow())
        t1 = Thread(target=self.action)
        t1.setDaemon(True)
        t1.start()

        self.start()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 744)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_basic = QtWidgets.QWidget(self.centralwidget)
        self.widget_basic.setGeometry(QtCore.QRect(0, 0, 961, 561))
        self.widget_basic.setObjectName("widget_basic")
        self.tabWidget = QtWidgets.QTabWidget(self.widget_basic)
        self.tabWidget.setGeometry(QtCore.QRect(200, 90, 681, 449))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")

        self.tab_search_3 = QtWidgets.QWidget()
        self.tab_search_3.setObjectName("tab_search_3")
        self.listWidget_searchresults = QtWidgets.QListWidget(self.tab_search_3)
        self.listWidget_searchresults.setGeometry(QtCore.QRect(10, 10, 651, 401))
        self.listWidget_searchresults.setObjectName("listWidget_searchresults")
        self.listWidget_searchresults.doubleClicked.connect(lambda: self.change_func(self.listWidget_searchresults))  # 应该是双击后进入下载播放的一系列流程
        self.listWidget_searchresults.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_searchresults.customContextMenuRequested[QPoint].connect(self.myListWidgetContext)  # 右键菜单，用于添加喜爱和在列表中删除
        self.tabWidget.addTab(self.tab_search_3, "")

        self.tab_history_3 = QtWidgets.QWidget()
        self.tab_history_3.setObjectName("tab_history_3")
        self.listWidget_history = QtWidgets.QListWidget(self.tab_history_3)
        self.listWidget_history.setGeometry(QtCore.QRect(10, 10, 651, 401))
        self.listWidget_history.setObjectName("listWidget_history")
        self.listWidget_history.doubleClicked.connect(lambda: self.change_funcse(self.listWidget_history))
        self.listWidget_history.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_history.customContextMenuRequested[QPoint].connect(self.myListWidgetContext2)
        self.tabWidget.addTab(self.tab_history_3, "")


        self.tab_love_3 = QtWidgets.QWidget()
        self.tab_love_3.setObjectName("tab_love_3")
        self.listWidget_love = QtWidgets.QListWidget(self.tab_love_3)
        self.listWidget_love.setGeometry(QtCore.QRect(10, 110, 651, 301))
        self.listWidget_love.setObjectName("listWidget_love")
        self.listWidget_love.doubleClicked.connect(lambda: self.change_funclove(self.listWidget_love))
        self.listWidget_love.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget_love.customContextMenuRequested[QPoint].connect(self.myListWidgetContext3)  # 这个也就是右键菜单

        self.label_ssmallpic_2 = QtWidgets.QLabel(self.tab_love_3)
        self.label_ssmallpic_2.setGeometry(QtCore.QRect(10, 0, 100, 100))
        self.label_ssmallpic_2.setObjectName("label_ssmallpic_2")
        self.pushButton_playlove = QtWidgets.QPushButton(self.tab_love_3)
        self.pushButton_playlove.setGeometry(QtCore.QRect(150, 40, 93, 28))
        self.pushButton_playlove.setObjectName("pushButton_playlove")
        self.pushButton_clearlove = QtWidgets.QPushButton(self.tab_love_3)
        self.pushButton_clearlove.setGeometry(QtCore.QRect(280, 40, 93, 28))
        self.pushButton_clearlove.setObjectName("pushButton_clearlove")
        self.tabWidget.addTab(self.tab_love_3, "")
        self.tab_local_3 = QtWidgets.QWidget()
        self.tab_local_3.setObjectName("tab_local_3")

        self.pushButton_choosefile = QtWidgets.QPushButton(self.tab_local_3)
        self.pushButton_choosefile.setGeometry(QtCore.QRect(470, 10, 93, 28))
        self.pushButton_choosefile.setObjectName("pushButton_choosefile")
        self.pushButton_choosefile.clicked.connect(self.add)

        self.pushButton_clearlocal = QtWidgets.QPushButton(self.tab_local_3)
        self.pushButton_clearlocal.setGeometry(QtCore.QRect(570, 10, 93, 28))
        self.pushButton_clearlocal.setObjectName("pushButton_clearlocal")
        self.pushButton_clearlocal.clicked.connect(self.dellocal)

        self.listWidget_local = QtWidgets.QListWidget(self.tab_local_3)
        self.listWidget_local.setGeometry(QtCore.QRect(10, 40, 651, 371))
        self.listWidget_local.setObjectName("listWidget_local")
        self.listWidget_local.doubleClicked.connect(lambda: self.change(self.listWidget_local))

        self.tabWidget.addTab(self.tab_local_3, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_basic)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 0, 521, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.comboBox_kind = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_kind.setEnabled(True)
        self.comboBox_kind.setEditable(False)
        self.comboBox_kind.setIconSize(QtCore.QSize(20, 20))
        self.comboBox_kind.setFrame(True)
        self.comboBox_kind.setObjectName("comboBox_kind")
        self.comboBox_kind.addItems(['秋秋音乐', '网抑云音乐', '裤钩音乐', '裤我音乐'])
        self.comboBox_kind.currentIndexChanged[int].connect(self.print)

        self.horizontalLayout_7.addWidget(self.comboBox_kind)
        self.lineEdit_search = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_search.setText("")
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_7.addWidget(self.lineEdit_search)
        self.pushButton_search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.pushButton_search.clicked.connect(self.correct)
        self.horizontalLayout_7.addWidget(self.pushButton_search)

        self.label_smallpic = MyQLabel(self.widget_basic)
        self.label_smallpic.setGeometry(QtCore.QRect(0, 210, 200, 200))
        self.label_smallpic.setObjectName("label_smallpic")
        self.label_smallpic.connect_customized_slot(self.show)

        self.widget_bottom = QtWidgets.QWidget(self.centralwidget)
        self.widget_bottom.setGeometry(QtCore.QRect(0, 560, 961, 141))
        self.widget_bottom.setObjectName("widget_bottom")

        self.label_name = QtWidgets.QLabel(self.widget_bottom)
        self.label_name.setGeometry(QtCore.QRect(80, 60, 170, 20))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName("label_name")
        self.label_singer = QtWidgets.QLabel(self.widget_bottom)
        self.label_singer.setGeometry(QtCore.QRect(130, 90, 70, 20))
        self.label_singer.setAlignment(QtCore.Qt.AlignCenter)
        self.label_singer.setObjectName("label_singer")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_bottom)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(260, 80, 511, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_Lefttime = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_Lefttime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Lefttime.setObjectName("label_Lefttime")
        self.horizontalLayout_10.addWidget(self.label_Lefttime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.label_Righttime = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_Righttime.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Righttime.setObjectName("label_Righttime")
        self.horizontalLayout_10.addWidget(self.label_Righttime)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_bottom)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 0, 511, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.pushButton_previous = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_previous.setObjectName("pushButton_previous")
        self.horizontalLayout_11.addWidget(self.pushButton_previous)
        self.pushButton_previous.clicked.connect(self.previous)

        self.pushButton_PlayPause = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_PlayPause.setStyleSheet("")
        self.pushButton_PlayPause.setObjectName("pushButton_PlayPause")
        self.horizontalLayout_11.addWidget(self.pushButton_PlayPause)
        self.pushButton_PlayPause.clicked.connect(self.pause)

        self.pushButton_next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout_11.addWidget(self.pushButton_next)
        self.pushButton_next.clicked.connect(self.nextion)

        self.pushButton_vol_down = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_vol_down.setObjectName("pushButton_vol_down")
        self.horizontalLayout_11.addWidget(self.pushButton_vol_down)
        self.pushButton_vol_down.clicked.connect(self.voicedown)

        self.pushButton_vol_up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_vol_up.setObjectName("pushButton_vol_up")
        self.horizontalLayout_11.addWidget(self.pushButton_vol_up)
        self.pushButton_vol_up.clicked.connect(self.voiceup)

        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalSlider = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.comboBox_playmode = QtWidgets.QComboBox(self.widget_bottom)
        self.comboBox_playmode.setGeometry(QtCore.QRect(790, 0, 87, 22))
        self.comboBox_playmode.setObjectName("comboBox_playmode")
        self.comboBox_playmode.addItem("")
        self.comboBox_playmode.addItem("")
        self.comboBox_playmode.addItem("")
        self.label_vol = QtWidgets.QLabel(self.widget_bottom)
        self.label_vol.setGeometry(QtCore.QRect(790, 50, 130, 20))
        self.label_vol.setAlignment(QtCore.Qt.AlignCenter)
        self.label_vol.setObjectName("label_vol")

        self.label_ssmallpic = MyQLabel(self.widget_bottom)
        self.label_ssmallpic.setGeometry(QtCore.QRect(10, 40, 67, 67))
        self.label_ssmallpic.setObjectName("label_ssmallpic")
        self.label_ssmallpic.connect_customized_slot(self.show)  # 左下角的小图片也可以切换播放页

        self.widget_playing = QtWidgets.QWidget(self.centralwidget)
        self.widget_playing.setGeometry(QtCore.QRect(0, 0, 961, 561))
        self.widget_playing.setObjectName("widget_playing")
        self.pushButton_playback = QtWidgets.QPushButton(self.widget_playing)
        self.pushButton_playback.setGeometry(QtCore.QRect(0, 0, 93, 28))
        self.pushButton_playback.setObjectName("pushButton_playback")
        self.pushButton_playback.clicked.connect(self.show)

        self.label_bigpic = MyQLabel(self.widget_playing)
        self.label_bigpic.setGeometry(QtCore.QRect(0, 140, 300, 300))
        self.label_bigpic.setObjectName("label_bigpic")
        self.label_bigpic.connect_customized_slot(self.show)

        pix_img = QPixmap(str(data + '/backdown.png'))
        pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
        self.label_bigpic.setPixmap(pix)

        self.layoutWidget = QtWidgets.QWidget(self.widget_playing)

        self.widget_playing.setHidden(True)  # 默认开始时播放页是隐藏的

        self.layoutWidget.setGeometry(QtCore.QRect(300, 50, 251, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_bigname = QtWidgets.QLabel(self.layoutWidget)
        self.label_bigname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_bigname.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bigname.setObjectName("label_bigname")
        self.verticalLayout_5.addWidget(self.label_bigname)
        self.label_bigsinger = QtWidgets.QLabel(self.layoutWidget)
        self.label_bigsinger.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_bigsinger.setAlignment(QtCore.Qt.AlignCenter)
        self.label_bigsinger.setObjectName("label_bigsinger")
        self.verticalLayout_5.addWidget(self.label_bigsinger)
        self.listWidget_lyrics = QtWidgets.QListWidget(self.widget_playing)
        self.listWidget_lyrics.setGeometry(QtCore.QRect(300, 140, 621, 411))
        self.listWidget_lyrics.setObjectName("listWidget_lyrics")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 961, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def action(self):
        global pause
        xun = 1
        while xun < 2:
            # print ('checking')

            try:
                sleep(1)
                if not mixer.music.get_busy() and pause == False and not downloading and start:
                    if play == 'shun':
                        print('自动下一首（循环播放）')
                        self.next()
                    elif play == 'shui':
                        print('自动下一首（随机播放）')
                        self.shui()
                    elif play == 'always':
                        print('自本一首（单曲循环）')
                        if not bo == 'local':
                            print('本一首（单曲循环）')


                            pause = False

                            mixer.music.load(data + '\{}.临时文件'.format(number))
                            mixer.music.play()
                        else:
                            print('本一首（单曲循环）')


                            pause = False

                            mixer.music.load(SongPath[num])
                            mixer.music.play()

            except:
                try:
                    pass
                except:
                    pass
                pass
        else:
            mixer.music.stop()

    def add(self):  # 添加本地音乐
        try:

            global SongPath
            global SongName
            global num
            global filew
            global asas
            fileN = QFileDialog.getExistingDirectory(None, "选取文件夹", "")
            if not fileN == '':
                self.listWidget_local.clear()
                filew = fileN + '/'
                asas = filew
                l1 = [name for name in listdir(fileN) if
                      name.endswith('.mp3') or name.endswith('.flac') or name.endswith('.wma') or name.endswith(
                          '.MP3') or name.endswith('.FLAC') or name.endswith('.WMA')]
                # l2 = [name for name in listdir(fileN) if name.endswith('.flac')]
                # l3 = [name for name in listdir(fileN) if name.endswith('wma')]
                SongNameadd = l1  # + l2 + l3
                SongPathadd = [filew + i for i in SongNameadd]
                SongName = SongName + SongNameadd
                SongPath = SongPath + SongPathadd
                print(SongPath)
                # self.Timer.timeout.connect(self.timercontorl)#时间函数，与下面的进度条和时间显示有关
                # self.label = os.path.splitext(SongName[num])#分割文件名和扩展名
                # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
                r = 0
                for i in SongName:
                    # self.listwidget.addItem(i)#将文件名添加到listWidget

                    self.listWidget_local.addItem(i)
                    # self.listWidget_local.item(r).setForeground(Qt.white)
                    r = r + 1
                # self.next(self)
        except:
            filew = asas

    def bofang(self, num, bo):
        print('尝试进行播放')
        try:
            import urllib
            global pause
            global songs
            global music
            global downloading
            downloading = True
            pause = False
            try:
                mixer.stop()
            except:
                pass
            mixer.init()
            try:
                self.Timer = QTimer()
                self.Timer.start(500)
            except:
                pass
            try:
                self.label_name.setText('正在寻找文件...')
                self.label_singer.setText('')
                self.work = WorkThread()
                self.work.start()
                self.work.trigger.connect(self.display)
            except:
                print('无法播放，歌曲下载错误')
                downloading = False
                pass

        except:
            sleep(0.1)
            print('播放系统错误')
            # self.next()
            pass

    def display(self, sd):
        global pause
        global songed
        global urled
        global lrcd
        global timenum

        if sd == 'finish':
            try:
                if bo == 'boing':
                    try:
                        e, x = str(songs[num]).split(' - ')
                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                    except:
                        self.label_name.setText(songs[num])
                        self.label_bigname.setText(songs[num])
                        self.label_singer.setText('')
                        self.label_bigsinger.setText('')

                        pass
                elif bo == 'boed':
                    try:
                        e, x = str(songed[num]).split(' - ')
                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                    except:
                        self.label_name.setText(songed[num])
                        self.label_bigname.setText(songed[num])
                        pass
                elif bo == 'love':
                    try:
                        e, x = str(loves[num]).split(' - ')
                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                    except:
                        self.label_name.setText(loves[num])
                        self.label_bigname.setText(loves[num])
                        self.label_singer.setText('')
                        self.label_bigsinger.setText('')
                        pass
                try:

                    if not picno:
                        pix_img = QPixmap(str(data + '/backdown.png'))
                        pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                        self.label_bigpic.setPixmap(pix)
                        pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                        self.label_smallpic.setPixmap(pix)
                        pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                        self.label_ssmallpic.setPixmap(pix)

                    else:
                        pix_img = QPixmap(str(data + '/back.png'))
                        pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                        self.label_bigpic.setPixmap(pix)
                        pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                        self.label_smallpic.setPixmap(pix)
                        pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                        self.label_ssmallpic.setPixmap(pix)

                except:
                    pix_img = QPixmap(str(data + '/backdown.png'))
                    pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                    self.label_bigpic.setPixmap(pix)
                    pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                    self.label_smallpic.setPixmap(pix)
                    pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                    self.label_ssmallpic.setPixmap(pix)

                print(str(data + '\{}.临时文件'.format(number)))
                mixer.music.load(str(data + '\{}.临时文件'.format(number)))  # 载入音乐
                mixer.music.play()
                pause = False
                try:
                    mp3 = str(data + '\{}.临时文件'.format(number))
                    xx = load(mp3)
                    try:
                        timenum = xx.info.time_secs
                        # print(str(timenum))

                        seconds = timenum
                        m, s = divmod(seconds, 60)
                        h, m = divmod(m, 60)
                        time = "%d:%02d:%02d" % (h, m, s)
                        self.label_Righttime.setText(time)
                    except:
                        print('time error')
                    global start
                    start = True

                except:
                    print('MP3错误，播放失败')

                if bo == 'boing':
                    songed.append(songs[num])
                    urled.append(urls[num])
                    picd.append(pic[num])
                    lrcd.append(lrcs[num])
                    r = 0
                    self.listWidget_history.clear()
                    for i in songed:
                        self.listWidget_history.addItem(i)
                        # self.listWidget_history.item(r).setForeground(Qt.white)
                        r = r + 1
                else:
                    pass
                # 播放音乐
            except:
                pass
        elif sd == 'nofinish':
            self.label_name.setText('下载错误')
            self.label_singer.setText('')

        elif sd == 'lrcfinish':
            r = 0
            self.listWidget_lyrics.clear()
            for i in lrct:
                if not i == '\r':
                    self.listWidget_lyrics.addItem(i)
                    # self.listWidget_lyrics.item(r).setForeground(Qt.white)
                    r = r + 1
                else:
                    pass
        elif sd == 'lrcnofinish':
            self.listWidget_lyrics.clear()
            self.listWidget_lyrics.addItem('纯音乐，请欣赏')
            # self.listWidget_lyrics.item(0).setForeground(Qt.white)
        else:
            self.label_name.setText('加速下载中,已完成{}'.format(sd))
            self.label_singer.setText('')

    def updateTime(self):
        Gettime = mixer.music.get_pos() // 1000  # 获取播放的时间
        seconds = int(Gettime)  # 对播放的时间进行转换
        currenttime = clck(seconds)

    def timercontorl(self):
        global settime

        Song_length = timenum // 1
        Get_Length = int(float(self.horizontalSlider.maximum()))

        rate = Get_Length / 100
        settime = Song_length * rate
        mixer.music.rewind()  # 恢复播放
        mixer.music.set_pos(settime)  # 设置进度条的进度

    def change(self, listwidget):
        global num
        global bo
        # print (item.flags())
        bo = 'local'
        num = int(listwidget.currentRow())
        print(num)

        # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
        f = str(SongName[num]).split('.mp3')
        f = str(f[0]).split('.flac')
        f = str(f[0]).split('.MP3')
        f = str(f[0]).split('.FLAC')
        f = str(f[0]).split('.wma')
        f = str(f[0]).split('.WMA')
        self.label_name.setText(f[0])
        self.label_bigname.setText(f[0])
        self.label_bigsinger.setText('')
        self.label_singer.setText('')
        print(listwidget.currentRow())
        self.bofanglocal()  # 播放本地音乐时没有歌手的信息显示

    def nextion(self):  # 下一首
        global pause

        try:

            if play == 'shun':
                print('下一首（循环播放）')
                self.next()
            elif play == 'shui':
                print('下一首（随机播放）')
                self.shui()
            elif play == 'always':
                if not bo == 'local':
                    print('本一首（单曲循环）')

                    pause = False

                    mixer.music.load(data + '\{}.临时文件'.format(number))
                    mixer.music.play()
                else:
                    print('本一首（单曲循环）')

                    pause = False

                    mixer.music.load(SongPath[num])
                    mixer.music.play()

        except:
            print('下一首错误')
            pass

    def next(self):  # 下一首-顺序播放状态
        print('顺序下一首')
        global num
        global songs
        print(bo)
        if bo == 'boing':
            if num == len(songs) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1
        elif bo == 'love':
            if num == len(loves) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1

        elif bo == 'boed':
            if num == len(songed) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1

        elif bo == 'local':
            if num == len(SongName) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1
        try:
            if bo == 'boing':
                self.label_name.setText(songs[num])
                e, x = str(songs[num]).split(' - ')
                try:
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songs[num])
                    self.label_bigname.setText(songs[num])
                    self.label_singer.setText('')
                    self.label_bigsinger.setText('')
                self.bofang(num, bo)
            elif bo == 'love':
                self.label_name.setText(loves[num])
                try:
                    e, x = str(loves[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(loves[num])
                    self.label_bigname.setText(loves[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')

                self.bofang(num, bo)
            elif bo == 'boed':
                try:
                    self.label_name.setText(songed[num])
                    e, x = str(songed[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songed[num])
                    self.label_bigname.setText(songed[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')
                self.bofang(num, bo)
            elif bo == 'local':
                self.label_name.setText(SongName[num])
                self.bofanglocal()
        except:

            print('下一首错误')
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search_3), _translate("MainWindow", "搜索结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history_3), _translate("MainWindow", "播放历史"))
        self.label_ssmallpic_2.setText(_translate("MainWindow", "小小图片100*100"))
        self.pushButton_playlove.setText(_translate("MainWindow", "播放全部"))
        self.pushButton_clearlove.setText(_translate("MainWindow", "清空列表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_love_3), _translate("MainWindow", "收藏喜爱"))
        self.pushButton_choosefile.setText(_translate("MainWindow", "选择文件夹"))
        self.pushButton_clearlocal.setText(_translate("MainWindow", "清除全部"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_local_3), _translate("MainWindow", "本地歌曲"))

        self.lineEdit_search.setPlaceholderText(_translate("MainWindow", "听~我想听的歌~"))
        self.pushButton_search.setText(_translate("MainWindow", "搜索"))
        self.label_smallpic.setText(_translate("MainWindow", "小图片200*200"))
        self.label_name.setText(_translate("MainWindow", "歌曲名"))
        self.label_singer.setText(_translate("MainWindow", "歌手"))
        self.label_Lefttime.setText(_translate("MainWindow", "00:00:00"))
        self.label_Righttime.setText(_translate("MainWindow", "00:00:00"))
        self.pushButton_previous.setText(_translate("MainWindow", "上一首"))
        self.pushButton_PlayPause.setText(_translate("MainWindow", "播放/暂停"))
        self.pushButton_next.setText(_translate("MainWindow", "下一首"))
        self.pushButton_vol_down.setText(_translate("MainWindow", "音量-"))
        self.pushButton_vol_up.setText(_translate("MainWindow", "音量+"))
        self.comboBox_playmode.setItemText(0, _translate("MainWindow", "单曲循环"))
        self.comboBox_playmode.setItemText(1, _translate("MainWindow", "随机播放"))
        self.comboBox_playmode.setItemText(2, _translate("MainWindow", "顺序播放"))
        self.label_vol.setText(_translate("MainWindow", "音量大小"))
        self.label_ssmallpic.setText(_translate("MainWindow", "小小图片100*100"))
        self.pushButton_playback.setText(_translate("MainWindow", "返回"))
        self.label_bigpic.setText(_translate("MainWindow", "大图片300*300"))
        self.label_bigname.setText(_translate("MainWindow", "歌名-大字号"))
        self.label_bigsinger.setText(_translate("MainWindow", "歌手-小字号"))

    def start(self):
        try:

            try:
                self.work = startThread()
                self.work.start()
                self.work.trigger.connect(self.dispng)
            except:
                print('默认图片下载错误')
                pass

            try:
                self.work22 = barThread()
                self.work22.start()
                self.work22.trigger.connect(self.disbar)
            except:
                print('12')

            try:
                pix_img = QPixmap(str(data + '/backdown.png'))
                pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                self.label_bigpic.setPixmap(pix)
                pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                self.label_smallpic.setPixmap(pix)
                pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                self.label_ssmallpic.setPixmap(pix)
            except:
                pass
        except:
            pass

    def barchange(self):  # 进度条的设置
        while True:

            try:
                sleep(0.9)  # 延迟执行给定的秒数，可是亚秒精度的浮点数。
                print('--------------------------------------')
                print(int(mixer.music.get_pos() / 1000) * 1000)
                print(self.horizontalSlider.value() * 1000)
                print(timenum)
                if int(mixer.music.get_pos() / 1000) * 1000 > 0 and int(mixer.music.get_pos() / 1000) < timenum:
                    try:
                        print(mixer.music.get_pos())
                        print(self.horizontalSlider.value() * 1000)
                        mixer.music.set_pos(int(self.horizontalSlider.value() * 1000))
                    except:
                        pass
            except:
                pass

    def disbar(self, apk):  # 展示时间条
        if apk == 'nofinish':
            print('bar获取失败')
        elif apk == 'change':
            pass
        else:
            try:
                # print(apk)
                self.horizontalSlider.setRange(0, int(timenum))
                # print(apk)
                # print (int(float(apk)))
                self.horizontalSlider.setValue(int(float(apk)))

                x = mixer.music.get_pos()
                a = int(x / 1000)
                seconds = a
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                time = "%d:%02d:%02d" % (h, m, s)
                # print(time)
                self.label_Lefttime.setText(time)
                # self.right_process_bar.setValue(int(apk))
            except Exception as e:
                print('bar设置失败', e)



    def bofanglocal(self):  # 播放本地音乐
        mixer.init()
        try:
            global pause

            try:
                self.photo('local')
            except:
                pass
            pause = False
            fill = SongPath[num]
            print(fill)
            try:
                global timenum
                mp3 = str(SongPath[num])
                xx = load(mp3)
                timenum = xx.info.time_secs
                global start
                start = True
            except:
                print('进度条错误，播放失败')
            try:
                mixer.stop()
            except:
                pass

            try:
                print(num)
                print(SongPath)
                mixer.music.load(SongPath[num])  # 载入音乐
                mixer.music.play()  # 播放音乐
            except Exception as e:
                print('MP3音频文件出现错误')
                print(e)
        except:
            sleep(0.1)
            print('system error')
            self.next()
            pass

    def pause(self):
        global pause
        if pause:
            try:
                mixer.music.unpause()
            except:
                pass
            pause = False
        else:
            try:
                mixer.music.pause()
            except:
                pass
            pause = True

    def next(self):  # 下一首-顺序播放状态
        print('顺序下一首')
        global num
        global songs
        print(bo)
        if bo == 'boing':
            if num == len(songs) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1
        elif bo == 'love':
            if num == len(loves) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1

        elif bo == 'boed':
            if num == len(songed) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1

        elif bo == 'local':
            if num == len(SongName) - 1:
                print('冇')
                num = 0
            else:
                num = num + 1
        try:
            if bo == 'boing':
                self.label_name.setText(songs[num])
                e, x = str(songs[num]).split(' - ')
                try:
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songs[num])
                    self.label_bigname.setText(songs[num])
                    self.label_singer.setText('')
                    self.label_bigsinger.setText('')
                self.bofang(num, bo)
            elif bo == 'love':
                self.label_name.setText(loves[num])
                try:
                    e, x = str(loves[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(loves[num])
                    self.label_bigname.setText(loves[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')

                self.bofang(num, bo)
            elif bo == 'boed':
                try:
                    self.label_name.setText(songed[num])
                    e, x = str(songed[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songed[num])
                    self.label_bigname.setText(songed[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')
                self.bofang(num, bo)
            elif bo == 'local':
                self.label_name.setText(SongName[num])
                self.bofanglocal()
        except:

            print('下一首错误')
            pass

    def dispng(self, a):
        if a == 'finish':
            pix_img = QPixmap(str(data + '/backdown.png'))
            pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
            self.label_bigpic.setPixmap(pix)
            pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
            self.label_smallpic.setPixmap(pix)
            try:
                pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                self.label_ssmallpic.setPixmap(pix)
            except Exception as e:
                print(e)

        elif a == 'login':
            r = 0
            self.listWidget_love.clear()
            for i in loves:
                # self.listwidget.addItem(i)#将文件名添加到listWidget

                self.listWidget_love.addItem(i)
                self.listWidget_love.item(r).setForeground(Qt.white)
                r = r + 1
            pass
        elif a == 'voicedone':
            try:
                mixer.init()
                mixer.music.set_volume(voice)
                k = Decimal(voice).quantize(Decimal('0.00'))
                self.label_vol.setText('音量：{}'.format(str(k * 100) + '%'))
            except:
                pass
        elif a == 'first':
            try:
                pix_img = QPixmap(str(data + '/first.png'))
                pix = pix_img.scaled(150, 150, Qt.KeepAspectRatio)
                self.label_ssmallpic_2.setPixmap(pix)

            except:
                pass
        elif a == 'nofirst':
            pix_img = QPixmap(str(data + '/backdown.png'))
            pix = pix_img.scaled(150, 150, Qt.KeepAspectRatio)
            self.label_ssmallpic_2.setPixmap(pix)

        else:
            print('图片下载错误2')

    def photo(self, kind):  # 展示图片？

        try:
            if kind == 'local':
                audio = File(SongPath[num])
                mArtwork = audio.tags['APIC:'].data
                with open(str(data + '/ls.png'), 'wb') as img:
                    img.write(mArtwork)
            else:
                pass
            try:
                lsfile = str(data + '/ls.png')
                safile = str(data + '/back.png')
                draw(lsfile, safile)

                pix_img = QPixmap(str(data + '/back.png'))
                pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                self.label_bigpic.setPixmap(pix)
                pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                self.label_smallpic.setPixmap(pix)
                pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                self.label_ssmallpic.setPixmap(pix)
            except:
                print('图片处理错误')
                pix_img = QPixmap(str(data + '/ls.png'))
                pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                self.label_bigpic.setPixmap(pix)
                pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                self.label_smallpic.setPixmap(pix)
                pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                self.label_ssmallpic.setPixmap(pix)
        except:
            print('没有图片')
            try:
                pix_img = QPixmap(str(data + '/backdown.png'))
                pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
                self.label_bigpic.setPixmap(pix)
                pix = pix_img.scaled(200, 200, Qt.KeepAspectRatio)
                self.label_smallpic.setPixmap(pix)
                pix = pix_img.scaled(67, 67, Qt.KeepAspectRatio)
                self.label_ssmallpic.setPixmap(pix)
            except:
                pass

    def show(self):  # 显示或关闭播放页面
        if self.widget_playing.isHidden():
            self.widget_playing.setHidden(False)
            self.widget_basic.setHidden(True)
        else:
            self.widget_playing.setHidden(True)
            self.widget_basic.setHidden(False)

    def previous(self):  # 上一首
        global num
        global songs
        if bo == 'boing':
            if num == 0:
                print('冇')
                num = len(songs) - 1
            else:
                num = num - 1
        elif bo == 'love':
            if num == 0:
                print('冇')
                num = len(loves) - 1
            else:
                num = num - 1
        elif bo == 'boed':
            if num == 0:
                print('冇')
                num = len(songed) - 1
            else:
                num = num - 1
        elif bo == 'local':
            if num == 0:
                print('冇')
                num = len(SongName) - 1
            else:
                num = num - 1
        try:
            if bo == 'boing':
                self.label_name.setText(songs[num])
                try:
                    e, x = str(songs[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songs[num])
                    self.label_bigname.setText(songs[num])
                    self.label_singer.setText('')
                    self.label_bigsinger.setText('')
                self.bofang(num, bo)
            elif bo == 'love':
                self.label_name.setText(loves[num])
                try:
                    e, x = str(loves[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(loves[num])
                    self.label_bigname.setText(loves[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')
                self.bofang(num, bo)
            elif bo == 'boed':
                self.label_name.setText(songed[num])
                try:
                    e, x = str(songed[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songed[num])
                    self.label_bigname.setText(songed[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')
                self.bofang(num, bo)
            elif bo == 'local':
                self.label_name.setText(SongName[num])
                self.bofanglocal()

        except:
            pass

    def voiceup(self):
        try:
            print('音量加大')
            global voice
            voice += 0.1
            if voice > 1:
                voice = 1
            mixer.music.set_volume(voice)
            k = Decimal(voice).quantize(Decimal('0.00'))
            self.label_vol.setText('音量：{}'.format(str(k * 100) + '%'))
        except:
            pass

    def voicedown(self):
        try:
            print('音量减少')
            global voice
            voice -= 0.1
            if voice < 0:
                voice = 0
            mixer.music.set_volume(voice)
            k = Decimal(voice).quantize(Decimal('0.00'))
            self.label_vol.setText('音量：{}'.format(str(k * 100) + '%'))
        except:
            pass

    def delall(self, typer):
        if typer == 'love':  # 喜欢收藏的页面
            global loves
            global loveurls
            global lovelrc

            global lovepics

            loveurls = []
            lovelrc = []
            lovepics = []
            loves = []
            self.listWidget_love.clear()
        elif typer == 'boing':  # 搜索页
            print(typer)
            self.listWidget_searchresults.clear()
            global songs
            global urls
            global lrcs
            global pic
            songs = []
            urls = []
            lrcs = []
            pic = []
        elif typer == 'local':
            print(typer)
            self.listWidget_local.clear()
            global SongName
            global SongPath
            SongName = []
            SongPath = []

    def dellocal(self):
        self.delall('local')

    def myListWidgetContext(self, point):  # 搜索页面
        global num_m
        try:
            # item = QListWidgetItem(self.listwidget.currentItem())
            num_m = int(self.listWidget_searchresults.currentRow())
            print(num_m)
        except:
            pass
        if not num_m == -1:
            global list_confident
            list_confident = 'boing'
            popMenu = QMenu()
            popMenu.addAction(QAction(u'添加到喜爱的歌', self, triggered=self.addItem))
            popMenu.addAction(QAction(u'从列表中删除', self, triggered=self.deItem))

            popMenu.exec_(QCursor.pos())

    def myListWidgetContext2(self, point):  # 最近播放页面
        global num_m
        try:
            # item = QListWidgetItem(self.listwidget.currentItem())
            num_m = int(self.listWidget_history.currentRow())
            print(num_m)
        except:
            pass
        if not num_m == -1:
            global list_confident
            list_confident = 'boed'
            popMenu = QMenu()
            popMenu.addAction(QAction(u'添加到喜爱的歌', self, triggered=self.addItem))
            popMenu.addAction(QAction(u'从列表中删除', self, triggered=self.deItem))

            popMenu.exec_(QCursor.pos())

    def myListWidgetContext3(self, point):  # 喜爱的歌曲的页面
        global num_m
        try:
            # item = QListWidgetItem(self.listwidget.currentItem())
            num_m = int(self.listWidget_love.currentRow())
            print(num_m)
        except:
            pass
        if not num_m == -1:
            global list_confident
            list_confident = 'love'
            popMenu = QMenu()
            popMenu.addAction(QAction(u'从列表中删除', self, triggered=self.deItem))

            popMenu.exec_(QCursor.pos())

    def myListWidgetContext5(self):  # 本地歌曲页面
        global num_m
        try:
            # item = QListWidgetItem(self.listwidget.currentItem())
            num_m = int(self.listWidget_local.currentRow())
            print(num_m)
        except:
            pass
        if not num_m == -1:
            global list_confident
            list_confident = 'local'
            popMenu = QMenu()
            popMenu.addAction(QAction(u'从列表中删除', self, triggered=self.deItem))

            popMenu.exec_(QCursor.pos())

    def addItem(self):  # 添加喜欢的曲目，包含各种信息
        try:
            global loves
            global loveurls
            global lovepics
            global lovelrc
            if list_confident == 'boing':
                loves.append(songs[num_m])
                loveurls.append(urls[num_m])
                lovepics.append(pic[num_m])
                lovelrc.append(lrcs[num_m])
            else:
                loves.append(songed[num_m])
                loveurls.append(urled[num_m])
                lovepics.append(picd[num_m])
                lovelrc.append(lrcd[num_m])
            self.work = firstThread()
            self.work.start()
            self.work.trigger.connect(self.dispng)
        except:
            pass
        r = 0
        self.listWidget_love.clear()
        for i in loves:
            # self.listwidget.addItem(i)#将文件名添加到listWidget

            self.listWidget_love.addItem(i)
            self.listWidget_love.item(r).setForeground(Qt.white)
            r = r + 1
        print('done')
        print(loves)

    def lovesong(self):
        if bo == 'boing' or bo == 'boed':
            try:
                global loves
                global loveurls
                global lovepics
                global lovelrc
                if bo == 'boing':
                    loves.append(songs[num])
                    loveurls.append(urls[num])
                    lovepics.append(pic[num])
                    lovelrc.append(lrcs[num])
                elif bo == 'boed':
                    loves.append(songed[num])
                    loveurls.append(urled[num])
                    lovepics.append(picd[num])
                    lovelrc.append(lrcd[num])
                else:
                    pass
                    '''
                    loves.append(loves[num])
                    loveurls.append(loveurls[num])
                    lovepics.append(lovepics[num])
                    lovelrc.append(lovelrc[num])

                    del loves[num]
                    del loveurls[num]
                    del lovepics[num]
                    del lovelrc[num]
                    '''

            except:
                pass
            self.work = firstThread()
            self.work.start()
            self.work.trigger.connect(self.dispng)
            r = 0
            self.listWidget_love.clear()
            for i in loves:
                # self.listwidget.addItem(i)#将文件名添加到listWidget

                self.listWidget_love.addItem(i)
                # self.listWidget_love.item(r).setForeground(Qt.white)
                r = r + 1
            print('done')
            print(loves)
        else:
            pass

    def deItem(self):
        try:
            if list_confident == 'boing':
                global songs
                global pic
                global lrcs
                global urls
                self.listWidget_searchresults.removeItemWidget(self.listWidget_searchresults.takeItem(num_m))
                del songs[num_m]
                del pic[num_m]
                del lrcs[num_m]
                del urls[num_m]
            elif list_confident == 'boed':
                global songed
                global picd
                global lrcd
                global urled
                self.listWidget_history.removeItemWidget(self.listWidget_history.takeItem(num_m))
                del songed[num_m]
                del picd[num_m]
                del lrcd[num_m]
                del urled[num_m]
            elif list_confident == 'love':
                global loves
                global lovepics
                global lovelrc
                global loveurls
                self.listWidget_love.removeItemWidget(self.listWidget_love.takeItem(num_m))
                del loves[num_m]
                del lovepics[num_m]
                del lovelrc[num_m]
                del loveurls[num_m]
                self.work = firstThread()
                self.work.start()
                self.work.trigger.connect(self.dispng)
            elif list_confident == 'local':
                global SongPath
                global SongName
                del SongPath[num_m]
                del SongName[num_m]
                self.listWidget_local.removeItemWidget(self.listWidget_local.takeItem(num_m))

        except:
            pass

    # 创建右键菜单

    def down(self):
        if bo == 'local':
            downpath = str(filew)
            downpath = downpath.replace('/', '\\')
            downpath = downpath + SongName[num]
            print(downpath)
            print('explorer /select,{}'.format(downpath))
            call('explorer /select,{}'.format(downpath))
        else:
            call('explorer /select,{}'.format(to))

    def page(self):
        global page
        page = 5

    def print(self, i):
        global type
        print(i)
        if i == 0:
            type = 'qq'
        elif i == 1:
            type = 'netease'
        elif i == 2:
            type = 'kugou'
        elif i == 3:
            type = 'kuwo'

    def big(self):
        global big
        print('最大化：{}'.format(big))
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False
        # print (windowState())

    def close(self):
        reply = QMessageBox.question(self, u'警告', u'确定退出???', QMessageBox.Yes,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            close = True
            try:
                mixer.music.stop()
            except:
                pass
            try:

                rmtree(str(data))
            except Exception as e:
                print('删除错误类型是', e.__class__.__name__)
                print('删除错误明细是', e)
            filepath = '{}/musicdata'.format(apdata)
            try:
                mkdir(filepath)
            except:
                pass
            print(filepath)
            with open(filepath + "/loves", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(loves)))
            with open(filepath + "/lovepics", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(lovepics)))
            with open(filepath + "/loveurls", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(loveurls)))
            with open(filepath + "/lovelrc", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(lovelrc)))
            with open(filepath + "/voice", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(voice)))

            try:

                rmtree(str(data))
            except Exception as e:
                print('删除错误类型是', e.__class__.__name__)
                print('删除错误明细是', e)

            exit()

        else:
            pass

    def mini(self):

        self.showMinimized()

    def change_func(self, listwidget):
        global downloading
        global bo
        global num
        global stopdown
        bo = 'boing'
        if downloading:
            try:
                try:
                    item = QListWidgetItem(self.listWidget_searchresults.currentItem())
                    print(item.text())
                    # print (item.flags())
                    num = int(listwidget.currentRow())
                    try:
                        e, x = str(songs[num]).split(' - ')
                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                    except:
                        self.label_name.setText(songs[num])
                        self.label_bigname.setText(songs[num])
                        self.label_singer.setText('')
                        self.label_bigsinger.setText('')
                        pass
                    print(listwidget.currentRow())
                    self.bofang(num, bo)
                except:
                    downloading = False
                    pass
            except:
                print('下载无法停止')
                pass
        else:
            try:

                item = QListWidgetItem(self.listWidget_searchresults.currentItem())
                print(item.text())
                # print (item.flags())
                num = int(listwidget.currentRow())
                # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
                self.label_name.setText(songs[num])
                try:
                    try:
                        e, x = str(songs[num]).split(' - ')

                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                    except:
                        self.label_name.setText(songs[num])
                        self.label_bigname.setText(songs[num])
                        self.label_singer.setText('')
                        self.label_bigsinger.setText('')
                except Exception as e:
                    print(e)
                print(listwidget.currentRow())
                self.bofang(num, bo)
            except:
                downloading = False
                pass

    def change_funcse(self, listwidget):
        global downloading
        global bo
        global stopdown
        global num
        bo = 'boed'
        if downloading:
            try:
                stopdown = True
                print('开始停止搜索')
                downloading = False
                try:
                    global num
                    self.listWidget_searchresults.clear()
                    item = QListWidgetItem(self.listWidget_searchresults.currentItem())
                    print(item.text())
                    # print (item.flags())
                    num = int(listwidget.currentRow())
                    # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
                    try:
                        e, x = str(songed[num]).split(' - ')
                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                    except:
                        self.label_name.setText(songed[num])
                        self.label_bigname.setText(songed[num])
                        pass
                    print(listwidget.currentRow())
                    self.bofang(num, bo)
                except:
                    downloading = False
                    pass
            except:
                print('stoped downloading')
                downloading = False
                print('根本停不下来')
                pass
        else:
            try:
                self.listWidget_searchresults.clear()
                item = QListWidgetItem(self.listWidget_searchresults.currentItem())
                print(item.text())
                # print (item.flags())
                num = int(listwidget.currentRow())
                # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
                try:
                    e, x = str(songed[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(songed[num])
                    self.label_bigname.setText(songed[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')
                print(listwidget.currentRow())
                self.bofang(num, bo)
            except:
                downloading = False
                pass

    def change_funclove(self, listwidget):
        global downloading
        global bo
        global stopdown
        global num
        bo = 'love'
        if downloading:
            try:
                stopdown = True
                try:
                    global num
                    item = QListWidgetItem(self.listWidget_searchresults.currentItem())
                    print(item.text())
                    # print (item.flags())
                    num = int(listwidget.currentRow())
                    # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
                    self.label_name.setText(loves[num])

                    try:
                        e, x = str(loves[num]).split(' - ')
                        self.label_name.setText(e)
                        self.label_bigsinger.setText(x)
                        self.label_bigname.setText(e)
                        self.label_singer.setText(x)
                        print(listwidget.currentRow())
                        print('to')
                    except Exception as e:
                        self.label_name.setText(loves[num])
                        self.label_bigname.setText(loves[num])
                        self.label_singer.setText('')
                        self.label_bigsinger.setText('')
                        print(e)
                    self.bofang(num, bo)
                except Exception as e:
                    print(e)
                    downloading = False
                    pass
            except:
                print('下载无法停止')
                pass
        else:
            try:

                item = QListWidgetItem(self.listWidget_searchresults.currentItem())
                print(item.text())
                # print (item.flags())
                num = int(listwidget.currentRow())
                # self.label.setText(wenjianming)#设置标签的文本为音乐的名字
                self.label_name.setText(loves[num])
                try:
                    e, x = str(loves[num]).split(' - ')
                    self.label_name.setText(e)
                    self.label_bigsinger.setText(x)
                    self.label_bigname.setText(e)
                    self.label_singer.setText(x)
                except:
                    self.label_name.setText(loves[num])
                    self.label_bigname.setText(loves[num])
                    self.label_bigsinger.setText('')
                    self.label_singer.setText('')
                print(listwidget.currentRow())
                self.bofang(num, bo)
            except:
                downloading = False
                pass

    def correct(self):
        global name

        seaname = self.lineEdit_search.text()
        name = seaname
        print(type)
        print(seaname)
        self.pa(seaname, type)

    def pa(self, name, type, ):
        global tryed
        global paing
        global stop
        self.listWidget_searchresults.clear()
        self.listWidget_searchresults.addItem('搜索中')
        # self.listWidget_searchresults.item(0).setForeground(Qt.white)
        try:
            if paing:
                stop = True

                self.listWidget_searchresults.clear()
                self.work2 = PAThread()
                self.work2.start()
                self.work2.trigger.connect(self.seafinish)
            else:
                self.work2 = PAThread()
                self.work2.start()
                self.work2.trigger.connect(self.seafinish)
        except:
            tryed = tryed + 1
            get_info('https://www.kuaidaili.com/free/inha')
            self.listWidget_searchresults.addItem('貌似没网了呀`(*>﹏<*)′,再试一遍吧~')
            # self.listWidget_searchresults.item(0).setForeground(Qt.white)

    def seafinish(self, eds):
        global tryed
        try:
            if eds == 'finish':
                self.listWidget_searchresults.clear()
                if songs == []:
                    self.listWidget_searchresults.clear()
                    self.listWidget_searchresults.addItem('歌曲搜索失败，请再试一下其他的软件选项')
                    # self.listWidget_searchresults.item(0).setForeground(Qt.white)
                else:
                    r = 0
                    for i in songs:
                        self.listWidget_searchresults.addItem(i)
                        # self.listWidget_searchresults.item(r).setForeground(Qt.white)
                        r = r + 1
            elif eds == 'clear':
                self.listWidget_searchresults.clear()
            elif eds == 'nothing':
                self.listWidget_searchresults.clear()
                self.listWidget_searchresults.addItem('你输入了个寂寞(*/ω＼*)')
                # self.listWidget_searchresults.item(0).setForeground(Qt.white)

            else:
                print('似乎没网了呀`(*>﹏<*)′')
                self.listWidget_searchresults.clear()
                self.listWidget_searchresults.addItem('似乎没网了呀`(*>﹏<*)′')
                # self.listWidget_searchresults.item(0).setForeground(Qt.white)
                print('tryed:{}'.format(tryed))
                tryed = tryed + 1
                get_info('https://www.kuaidaili.com/free/inha')
                print('tryed:{}'.format(tryed))
        except:
            print('完成了，但没有完全完成----列表错误')
            pass

def draw(lsfile, safile):  # 还没搞懂
    markImg = Image.open(lsfile)
    thumb_width = 600

    im_square = crop_max_square(markImg).resize((thumb_width, thumb_width), Image.LANCZOS)
    im_thumb = mask_circle_transparent(im_square, 0)
    im_thumb.save(safile)
    remove(lsfile)


def mask_circle_transparent(pil_img, blur_radius, offset=0):
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pil_img.copy()
    result.putalpha(mask)
    return result


def crop_max_square(pil_img): \
    return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def display_time(time):  # 展示时间
    if time < 10:
        return "0" + str(time)
    else:
        return str(time)


def clck(seconds):
    if seconds >= 60:
        minutes = seconds // 60
        seconds = seconds - minutes * 60
        return display_time(minutes) + ":" + display_time(seconds)
    else:
        return "00:" + display_time(seconds)

# 重写
class MainWindow(QtWidgets.QMainWindow):

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, '提示',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            try:

                rmtree(str(data))
            except Exception as e:
                print('删除错误类型是', e.__class__.__name__)
                print('删除错误明细是', e)
            filepath = '{}/musicdata'.format(apdata)
            try:
                mkdir(filepath)
            except:
                pass
            print(filepath)
            with open(filepath + "/loves", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(loves)))
            with open(filepath + "/lovepics", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(lovepics)))
            with open(filepath + "/loveurls", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(loveurls)))
            with open(filepath + "/lovelrc", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(lovelrc)))
            with open(filepath + "/voice", 'w', encoding='utf-8') as f:
                f.truncate(0)
                print(f.write(str(voice)))
            event.accept()

        else:
            event.ignore()

    def mousePressEvent(self, event):  # 鼠标点击事件
        global big
        big = False

        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        global big
        big = False
        if Qt.LeftButton and self.m_flag:
            self.setWindowState(Qt.WindowNoState)
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        global big
        big = False
        self.m_flag = False

    def big(self):  # 最大化
        global big
        print('最大化：{}'.format(big))
        if not big:
            self.setWindowState(Qt.WindowMaximized)
            big = True
        elif big:
            self.setWindowState(Qt.WindowNoState)
            big = False

    def mini(self):  # 最小化

        self.showMinimized()

    def crop_max_square(pil_img): \
        return crop_center(pil_img, min(pil_img.size), min(pil_img.size))


class firstThread(QThread):
    # 喜爱的第一幅图片下载并处理线程
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(firstThread, self).__init__()

    def run(self):
        try:
            # 下在第一幅喜爱的图片
            req = get(lovepics[0])
            checkfile = open(str(data + '/ls3.png'), 'w+b')
            for i in req.iter_content(100000):
                checkfile.write(i)

            checkfile.close()
            # 处理图片
            lsfile = str(data + '/ls3.png')
            safile = str(data + '/first.png')
            draw(lsfile, safile)
            self.trigger.emit(str('first'))  # 返回完成
        except:
            self.trigger.emit(str('nofirst'))  # 返回错误
            print('图片下载错误')
            pass


class startThread(QThread):
    # 开始线程，一启动程序就运行
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(startThread, self).__init__()

    def run(self):
        try:
            apdataas = getenv("APPDATA")
            filepathas = '{}/musicdata'.format(apdataas)
            global lovelrc
            global loveurls
            global loves
            global lovepics
            global voice
            # 读取历史数据开始
            try:
                with open(filepathas + "/voice", 'r', encoding='utf-8') as f:
                    a = f.read()
                    # print(a)
                    voice = float(a)
                print(voice)
                self.trigger.emit(str('voicedone'))
            except:
                self.trigger.emit(str('voicedone'))
                pass

            with open(filepathas + "/loves", 'r', encoding='utf-8') as f:
                a = f.read()
                print(a)
            strer = a
            loves = literal_eval(strer)

            with open(filepathas + "/lovepics", 'r', encoding='utf-8') as f:
                a = f.read()
                print(a)
            strer = a
            lovepics = literal_eval(strer)

            with open(filepathas + "/loveurls", 'r', encoding='utf-8') as f:
                a = f.read()
                print(a)
            strer = a
            loveurls = literal_eval(strer)

            with open(filepathas + "/lovelrc", 'r', encoding='utf-8') as f:
                a = f.read()
                print(a)
            strer = a
            lovelrc = literal_eval(strer)
            self.trigger.emit(str('login'))
            print(loves)
            print('read finish')
        except:
            print('read error')
            pass
        # 读取数据结束

        # 下载喜爱的歌列表中首项的歌曲封面
        try:
            req = get(lovepics[0])
            checkfile = open(str(data + '/ls3.png'), 'w+b')
            for i in req.iter_content(100000):
                checkfile.write(i)

            checkfile.close()
            lsfile = str(data + '/ls3.png')
            safile = str(data + '/first.png')
            draw(lsfile, safile)
            self.trigger.emit(str('first'))
        except:
            self.trigger.emit(str('nofirst'))
            pass

        # 获取免费的代理IP
        try:
            get_info('https://www.kuaidaili.com/free/inha')
            try:
                try:
                    req = get('https://api.dujin.org/bing/1920.php')
                    checkfile = open(str(data + '/ls2.png'), 'w+b')
                    for i in req.iter_content(100000):
                        checkfile.write(i)

                    checkfile.close()
                    lsfile = str(data + '/ls2.png')
                    safile = str(data + '/backdown.png')
                    draw(lsfile, safile)
                except:
                    print('图片下载错误')
                    pass


            except:
                pass
            self.trigger.emit(str('finish'))

        except:
            self.trigger.emit(str('nofinish'))


class barThread(QThread):
    # 进度条线程
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(barThread, self).__init__()

    def run(self):
        xun4 = 1
        # print ('begin')
        try:

            # print ('check')
            sleep(1)
            try:
                try:
                    # 进度条数据储存在timenum
                    global timenum

                    xun4 = 1
                    while xun4 < 2:
                        sleep(1)
                        # print ('check')
                        if not downloading or not paing:
                            try:

                                timenumm = timenum
                                # print(timenum)
                                current = mixer.music.get_pos() / 1000  # 毫秒
                                # print(current)

                                if current < 0:
                                    pass
                                else:
                                    self.trigger.emit(str(current))  # 显示进度条数据

                                self.trigger.emit(str('change'))


                            except:
                                try:
                                    if mixer.music.get_busy():
                                        print('进度条错误')
                                except:
                                    pass
                except:
                    pass


            except:
                pass
        except:
            pass


class PAThread(QThread):
    # 爬虫线程
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数
        super(PAThread, self).__init__()

    def run(self):
        qmut.lock()
        try:
            global paing
            global stop
            global lrcs
            global urls
            global songs
            global name
            global songid
            global proxies
            global pic
            global tryed
            paing = True

            print('搜索软件{}'.format(type))
            print('开始搜索')
            name = name
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.110.430.128 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'

            }
            urls = []
            songs = []
            pic = []
            lrcs = []
            pages = 5
            print(pages)

            for a in range(1, pages + 1):
                if not stop:

                    urlss = ['http://www.xmsj.org/',
                             'http://music.laomao.me/']
                    print(tryed)
                    if tryed > 3:

                        tryed = 0
                        url = urlss[tryed]
                    else:
                        url = urlss[tryed]
                    print(urlss[tryed])

                    params = {'input': name,
                              'filter': 'name',
                              'type': type,
                              'page': a
                              }
                    if not stop:
                        try:
                            res = post(url, params, headers=headers, proxies=proxies)
                            html = res.json()

                            for i in range(0, 10):

                                try:
                                    title = jsonpath(html, '$..title')[i]
                                    author = jsonpath(html, '$..author')[i]
                                    url1 = jsonpath(html, '$..url')[i]  # 取下载网址
                                    pick = jsonpath(html, '$..pic')[i]  # 取图片

                                    lrc = jsonpath(html, '$..lrc')[i]
                                    print(title, author)
                                    lrcs.append(lrc)
                                    urls.append(url1)
                                    pic.append(pick)
                                    songs.append(str(title) + ' - ' + str(author))
                                    # self.textEdit.setText(lrc)  # 打印歌词
                                    # print(lrc)
                                except:
                                    pass
                        except:
                            stop = False
                            paing = False

                        print(urls)
                        print(songs)
                        self.trigger.emit(str('finish'))
                    else:
                        print('stop')
                        self.trigger.emit(str('finish'))
                else:
                    print('stop')
                    self.trigger.emit(str('clear'))
                    pass

            stop = False
            paing = False

        except:
            print('爬取歌曲出错')
            self.trigger.emit(str('unfinish'))
            stop = False
            paing = False
        qmut.unlock()


def get_info(url):
    print('开始获取代理IP地址...')
    print('尝试次数{}'.format(tryed))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/491.10.2623.122 Safari/537.36'
    }
    web_data = get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ranks = soup.select('#list > table > tbody > tr:nth-child({}) > td:nth-child(1)'.format(str(tryed)))
    titles = soup.select('#list > table > tbody > tr:nth-child({}) > td:nth-child(2)'.format(str(tryed)))
    times = soup.select('#list > table > tbody > tr:nth-child({}) > td:nth-child(6)'.format(str(tryed)))
    for rank, title, time in zip(ranks, titles, times):
        data = {
            'IP': rank.get_text(),
            'duan': title.get_text(),
            'time': time.get_text()
        }
        q = str('http://' + str(rank.get_text()) + '/' + str(title.get_text()))
        proxies = {
            'http': q
        }
        print('代理IP地址：{}'.format(proxies))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("痛苦音乐")
    MainWindow.show()
    sys.exit(app.exec_())

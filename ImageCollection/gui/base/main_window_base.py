# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1440, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/window_icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"selection-background-color: rgb(188, 188, 188);\n"
"selection-color: rgb(0, 0, 0);\n"
"border-color: rgb(15, 15, 15);\n"
"background-color: rgb(63, 63, 63);\n"
"alternate-background-color: rgb(188, 188, 188);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalFrame_2 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame_2.setGeometry(QtCore.QRect(330, -1, 1101, 881))
        self.verticalFrame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame_2.setObjectName("verticalFrame_2")
        self.verticalFrame_3 = QtWidgets.QFrame(self.verticalFrame_2)
        self.verticalFrame_3.setGeometry(QtCore.QRect(0, 750, 1100, 120))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame_3.sizePolicy().hasHeightForWidth())
        self.verticalFrame_3.setSizePolicy(sizePolicy)
        self.verticalFrame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.verticalFrame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame_3.setObjectName("verticalFrame_3")
        self.frame = QtWidgets.QFrame(self.verticalFrame_3)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(0, 60, 1100, 60))
        self.frame.setMinimumSize(QtCore.QSize(1100, 60))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_previous_image = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_previous_image.sizePolicy().hasHeightForWidth())
        self.button_previous_image.setSizePolicy(sizePolicy)
        self.button_previous_image.setMinimumSize(QtCore.QSize(100, 50))
        self.button_previous_image.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_previous_image.setObjectName("button_previous_image")
        self.horizontalLayout.addWidget(self.button_previous_image)
        self.button_next_image = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_next_image.sizePolicy().hasHeightForWidth())
        self.button_next_image.setSizePolicy(sizePolicy)
        self.button_next_image.setMinimumSize(QtCore.QSize(100, 50))
        self.button_next_image.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_next_image.setObjectName("button_next_image")
        self.horizontalLayout.addWidget(self.button_next_image)
        self.button_to_art = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_to_art.sizePolicy().hasHeightForWidth())
        self.button_to_art.setSizePolicy(sizePolicy)
        self.button_to_art.setMinimumSize(QtCore.QSize(100, 50))
        self.button_to_art.setMaximumSize(QtCore.QSize(400, 16777215))
        self.button_to_art.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_to_art.setObjectName("button_to_art")
        self.horizontalLayout.addWidget(self.button_to_art)
        self.button_to_erotics = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_to_erotics.sizePolicy().hasHeightForWidth())
        self.button_to_erotics.setSizePolicy(sizePolicy)
        self.button_to_erotics.setMinimumSize(QtCore.QSize(100, 50))
        self.button_to_erotics.setMaximumSize(QtCore.QSize(400, 16777215))
        self.button_to_erotics.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_to_erotics.setObjectName("button_to_erotics")
        self.horizontalLayout.addWidget(self.button_to_erotics)
        self.button_to_porn = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_to_porn.sizePolicy().hasHeightForWidth())
        self.button_to_porn.setSizePolicy(sizePolicy)
        self.button_to_porn.setMinimumSize(QtCore.QSize(100, 50))
        self.button_to_porn.setMaximumSize(QtCore.QSize(400, 16777215))
        self.button_to_porn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_to_porn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_to_porn.setObjectName("button_to_porn")
        self.horizontalLayout.addWidget(self.button_to_porn)
        self.frame_2 = QtWidgets.QFrame(self.verticalFrame_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1101, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_collection_0 = QtWidgets.QLabel(self.frame_3)
        self.label_collection_0.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_collection_0.setFont(font)
        self.label_collection_0.setStyleSheet("QLabel {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-top-left-radius: 10%;\n"
"    border-bottom-left-radius: 10%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    border-right: 2px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}")
        self.label_collection_0.setFrameShape(QtWidgets.QFrame.Box)
        self.label_collection_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_collection_0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_collection_0.setIndent(5)
        self.label_collection_0.setObjectName("label_collection_0")
        self.horizontalLayout_2.addWidget(self.label_collection_0)
        self.label_collection_1 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_collection_1.setFont(font)
        self.label_collection_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_collection_1.setStyleSheet("QLabel {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-top-right-radius: 10%;\n"
"    border-bottom-right-radius: 10%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    border-left: 2px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}")
        self.label_collection_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_collection_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_collection_1.setScaledContents(False)
        self.label_collection_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_collection_1.setIndent(5)
        self.label_collection_1.setObjectName("label_collection_1")
        self.horizontalLayout_2.addWidget(self.label_collection_1)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_collection_moveto_0 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_collection_moveto_0.setFont(font)
        self.label_collection_moveto_0.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_collection_moveto_0.setStyleSheet("QLabel {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-top-left-radius: 10%;\n"
"    border-bottom-left-radius: 10%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    border-right: 2px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}")
        self.label_collection_moveto_0.setFrameShape(QtWidgets.QFrame.Box)
        self.label_collection_moveto_0.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_collection_moveto_0.setScaledContents(False)
        self.label_collection_moveto_0.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_collection_moveto_0.setIndent(5)
        self.label_collection_moveto_0.setObjectName("label_collection_moveto_0")
        self.horizontalLayout_4.addWidget(self.label_collection_moveto_0)
        self.label_collection_moveto_1 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_collection_moveto_1.setFont(font)
        self.label_collection_moveto_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_collection_moveto_1.setStyleSheet("QLabel {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-top-right-radius: 10%;\n"
"    border-bottom-right-radius: 10%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    border-left: 2px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}")
        self.label_collection_moveto_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_collection_moveto_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_collection_moveto_1.setScaledContents(False)
        self.label_collection_moveto_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_collection_moveto_1.setIndent(5)
        self.label_collection_moveto_1.setObjectName("label_collection_moveto_1")
        self.horizontalLayout_4.addWidget(self.label_collection_moveto_1)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalFrame = QtWidgets.QFrame(self.verticalFrame_2)
        self.verticalFrame.setGeometry(QtCore.QRect(0, 0, 1100, 751))
        self.verticalFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.verticalFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_current_image_image = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_current_image_image.sizePolicy().hasHeightForWidth())
        self.label_current_image_image.setSizePolicy(sizePolicy)
        self.label_current_image_image.setMinimumSize(QtCore.QSize(950, 640))
        self.label_current_image_image.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_current_image_image.setStyleSheet("")
        self.label_current_image_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_current_image_image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_current_image_image.setLineWidth(2)
        self.label_current_image_image.setScaledContents(False)
        self.label_current_image_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_image_image.setObjectName("label_current_image_image")
        self.verticalLayout.addWidget(self.label_current_image_image)
        self.label_current_image_name = QtWidgets.QLabel(self.verticalFrame)
        self.label_current_image_name.setMaximumSize(QtCore.QSize(16777215, 45))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_current_image_name.setFont(font)
        self.label_current_image_name.setStyleSheet("border: 0px;")
        self.label_current_image_name.setFrameShape(QtWidgets.QFrame.Box)
        self.label_current_image_name.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_current_image_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_image_name.setObjectName("label_current_image_name")
        self.verticalLayout.addWidget(self.label_current_image_name)
        self.verticalFrame1 = QtWidgets.QFrame(self.centralwidget)
        self.verticalFrame1.setGeometry(QtCore.QRect(0, -1, 330, 881))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame1.sizePolicy().hasHeightForWidth())
        self.verticalFrame1.setSizePolicy(sizePolicy)
        self.verticalFrame1.setSizeIncrement(QtCore.QSize(0, 0))
        self.verticalFrame1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalFrame1.setAutoFillBackground(False)
        self.verticalFrame1.setFrameShape(QtWidgets.QFrame.Box)
        self.verticalFrame1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.verticalFrame1.setObjectName("verticalFrame1")
        self.gridFrame = QtWidgets.QFrame(self.verticalFrame1)
        self.gridFrame.setGeometry(QtCore.QRect(0, 800, 320, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setObjectName("gridFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.button_rename_image = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_rename_image.sizePolicy().hasHeightForWidth())
        self.button_rename_image.setSizePolicy(sizePolicy)
        self.button_rename_image.setMinimumSize(QtCore.QSize(149, 50))
        self.button_rename_image.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_rename_image.setObjectName("button_rename_image")
        self.gridLayout.addWidget(self.button_rename_image, 1, 2, 1, 1)
        self.button_delete_image = QtWidgets.QPushButton(self.gridFrame)
        self.button_delete_image.setMinimumSize(QtCore.QSize(100, 50))
        self.button_delete_image.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border-radius: 10px;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"    font-size: 16pt;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.button_delete_image.setFlat(False)
        self.button_delete_image.setObjectName("button_delete_image")
        self.gridLayout.addWidget(self.button_delete_image, 1, 1, 1, 1)
        self.listWidget_image_list = QtWidgets.QListWidget(self.verticalFrame1)
        self.listWidget_image_list.setGeometry(QtCore.QRect(5, 5, 320, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget_image_list.sizePolicy().hasHeightForWidth())
        self.listWidget_image_list.setSizePolicy(sizePolicy)
        self.listWidget_image_list.setStyleSheet("QListWidget::item:hover{\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QListWidget::item:selected{\n"
"    background-color: rgb(210, 210, 210);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.listWidget_image_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget_image_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget_image_list.setLineWidth(1)
        self.listWidget_image_list.setMidLineWidth(0)
        self.listWidget_image_list.setObjectName("listWidget_image_list")
        self.label_items_in_list = QtWidgets.QLabel(self.verticalFrame1)
        self.label_items_in_list.setGeometry(QtCore.QRect(10, 790, 311, 21))
        self.label_items_in_list.setAlignment(QtCore.Qt.AlignCenter)
        self.label_items_in_list.setObjectName("label_items_in_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1440, 27))
        self.menuBar.setStyleSheet("QMenuBar::item:selected {\n"
"    background-color: rgb(188, 188, 188);\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setStyleSheet("")
        self.menuFile.setObjectName("menuFile")
        self.menuCollections = QtWidgets.QMenu(self.menuBar)
        self.menuCollections.setObjectName("menuCollections")
        MainWindow.setMenuBar(self.menuBar)
        self.actionOpen_Folder = QtWidgets.QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionCollections = QtWidgets.QAction(MainWindow)
        self.actionCollections.setObjectName("actionCollections")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_Collection = QtWidgets.QAction(MainWindow)
        self.actionNew_Collection.setObjectName("actionNew_Collection")
        self.actionAll_Images = QtWidgets.QAction(MainWindow)
        self.actionAll_Images.setObjectName("actionAll_Images")
        self.actionUnsorted = QtWidgets.QAction(MainWindow)
        self.actionUnsorted.setObjectName("actionUnsorted")
        self.actioncol = QtWidgets.QAction(MainWindow)
        self.actioncol.setObjectName("actioncol")
        self.actionPorn = QtWidgets.QAction(MainWindow)
        self.actionPorn.setObjectName("actionPorn")
        self.actionErotics = QtWidgets.QAction(MainWindow)
        self.actionErotics.setObjectName("actionErotics")
        self.actionArt = QtWidgets.QAction(MainWindow)
        self.actionArt.setObjectName("actionArt")
        self.actionRecycle_bin = QtWidgets.QAction(MainWindow)
        self.actionRecycle_bin.setObjectName("actionRecycle_bin")
        self.actionRefresh_List = QtWidgets.QAction(MainWindow)
        self.actionRefresh_List.setObjectName("actionRefresh_List")
        self.actionMove_Images = QtWidgets.QAction(MainWindow)
        self.actionMove_Images.setObjectName("actionMove_Images")
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addAction(self.actionRefresh_List)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuCollections.addAction(self.actionAll_Images)
        self.menuCollections.addSeparator()
        self.menuCollections.addAction(self.actionPorn)
        self.menuCollections.addAction(self.actionErotics)
        self.menuCollections.addAction(self.actionArt)
        self.menuCollections.addSeparator()
        self.menuCollections.addAction(self.actionRecycle_bin)
        self.menuCollections.addSeparator()
        self.menuCollections.addSeparator()
        self.menuCollections.addAction(self.actionMove_Images)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuCollections.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SORTAH"))
        self.button_previous_image.setText(_translate("MainWindow", "<-"))
        self.button_next_image.setText(_translate("MainWindow", "->"))
        self.button_to_art.setText(_translate("MainWindow", "To Art"))
        self.button_to_erotics.setText(_translate("MainWindow", "To Erotics"))
        self.button_to_porn.setText(_translate("MainWindow", "To Porn"))
        self.label_collection_0.setText(_translate("MainWindow", "Current collection"))
        self.label_collection_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_collection_moveto_0.setText(_translate("MainWindow", "Move to"))
        self.label_collection_moveto_1.setText(_translate("MainWindow", "TextLabel"))
        self.label_current_image_image.setText(_translate("MainWindow", "Image"))
        self.label_current_image_name.setText(_translate("MainWindow", "Image Name"))
        self.button_rename_image.setText(_translate("MainWindow", "Rename"))
        self.button_delete_image.setText(_translate("MainWindow", "Delete"))
        self.label_items_in_list.setText(_translate("MainWindow", "TextLabel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCollections.setTitle(_translate("MainWindow", "Collections"))
        self.actionOpen_Folder.setText(_translate("MainWindow", "Open"))
        self.actionCollections.setText(_translate("MainWindow", "Collections"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_Collection.setText(_translate("MainWindow", "New Collection"))
        self.actionAll_Images.setText(_translate("MainWindow", "All Images"))
        self.actionUnsorted.setText(_translate("MainWindow", "Unsorted"))
        self.actioncol.setText(_translate("MainWindow", "col"))
        self.actionPorn.setText(_translate("MainWindow", "Porn"))
        self.actionErotics.setText(_translate("MainWindow", "Erotics"))
        self.actionArt.setText(_translate("MainWindow", "Art"))
        self.actionRecycle_bin.setText(_translate("MainWindow", "Recycle bin"))
        self.actionRefresh_List.setText(_translate("MainWindow", "Refresh List"))
        self.actionMove_Images.setText(_translate("MainWindow", "Move Images"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

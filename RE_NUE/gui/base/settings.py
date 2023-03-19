# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        MainWidget.setObjectName("MainWidget")
        MainWidget.setEnabled(True)
        MainWidget.resize(851, 582)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QtCore.QSize(750, 500))
        MainWidget.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"selection-background-color: rgb(188, 188, 188);\n"
"selection-color: rgb(0, 0, 0);\n"
"border-color: rgb(15, 15, 15);\n"
"background-color: rgb(63, 63, 63);\n"
"alternate-background-color: rgb(188, 188, 188);\n"
"\n"
"QMenuBar::item:selected {\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border-radius: 5%;\n"
"border: 1px solid rgb(188, 188, 188);\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"        \n"
"            ")
        self.MainWidget_gridLayout = QtWidgets.QGridLayout(MainWidget)
        self.MainWidget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MainWidget_gridLayout.setSpacing(0)
        self.MainWidget_gridLayout.setObjectName("MainWidget_gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(MainWidget)
        self.tabWidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabBar {\n"
"font: 13pt \"Century Gothic\";\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"font: 13pt \"Century Gothic\";\n"
"background-color: rgb(63, 63, 63);\n"
"\n"
"}\n"
"QTabBar:tab:hover {\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0)\n"
"}\n"
"QTabBar:tab:selected {\n"
"background-color: rgb(160, 160, 160);\n"
"color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QTabWidget::pane {}\n"
"                        ")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_general = QtWidgets.QWidget()
        self.tab_general.setStyleSheet("")
        self.tab_general.setObjectName("tab_general")
        self.tab_general_gridLayout = QtWidgets.QGridLayout(self.tab_general)
        self.tab_general_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tab_general_gridLayout.setSpacing(0)
        self.tab_general_gridLayout.setObjectName("tab_general_gridLayout")
        self.groupBox_audio_paths = QtWidgets.QGroupBox(self.tab_general)
        self.groupBox_audio_paths.setStyleSheet("")
        self.groupBox_audio_paths.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_audio_paths.setFlat(True)
        self.groupBox_audio_paths.setCheckable(False)
        self.groupBox_audio_paths.setObjectName("groupBox_audio_paths")
        self.groupBox_music_paths_gridLayout = QtWidgets.QGridLayout(self.groupBox_audio_paths)
        self.groupBox_music_paths_gridLayout.setContentsMargins(5, 5, 5, 0)
        self.groupBox_music_paths_gridLayout.setObjectName("groupBox_music_paths_gridLayout")
        self.widget_audio_paths_buttons = QtWidgets.QWidget(self.groupBox_audio_paths)
        self.widget_audio_paths_buttons.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border-radius: 5%;\n"
"border: 1px solid rgb(188, 188, 188);\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.widget_audio_paths_buttons.setObjectName("widget_audio_paths_buttons")
        self.widget_music_paths_buttons_verticalLayout = QtWidgets.QVBoxLayout(self.widget_audio_paths_buttons)
        self.widget_music_paths_buttons_verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.widget_music_paths_buttons_verticalLayout.setSpacing(5)
        self.widget_music_paths_buttons_verticalLayout.setObjectName("widget_music_paths_buttons_verticalLayout")
        self.button_add_path = QtWidgets.QPushButton(self.widget_audio_paths_buttons)
        self.button_add_path.setMinimumSize(QtCore.QSize(80, 0))
        self.button_add_path.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_add_path.setStyleSheet("")
        self.button_add_path.setObjectName("button_add_path")
        self.widget_music_paths_buttons_verticalLayout.addWidget(self.button_add_path)
        self.button_delete_path = QtWidgets.QPushButton(self.widget_audio_paths_buttons)
        self.button_delete_path.setMinimumSize(QtCore.QSize(80, 0))
        self.button_delete_path.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_delete_path.setStyleSheet("")
        self.button_delete_path.setObjectName("button_delete_path")
        self.widget_music_paths_buttons_verticalLayout.addWidget(self.button_delete_path)
        self.button_edit_path = QtWidgets.QPushButton(self.widget_audio_paths_buttons)
        self.button_edit_path.setMinimumSize(QtCore.QSize(80, 0))
        self.button_edit_path.setMaximumSize(QtCore.QSize(80, 16777215))
        self.button_edit_path.setStyleSheet("")
        self.button_edit_path.setObjectName("button_edit_path")
        self.widget_music_paths_buttons_verticalLayout.addWidget(self.button_edit_path)
        spacerItem = QtWidgets.QSpacerItem(20, 318, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.widget_music_paths_buttons_verticalLayout.addItem(spacerItem)
        self.groupBox_music_paths_gridLayout.addWidget(self.widget_audio_paths_buttons, 0, 1, 1, 1)
        self.tableWidget_audio_paths = QtWidgets.QTableWidget(self.groupBox_audio_paths)
        self.tableWidget_audio_paths.setStyleSheet("QHeaderView {\n"
"background: transparent;\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(63, 63, 63);\n"
"color: white;\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"background-color: rgb(63,63, 63);\n"
"border: 0px solid;\n"
"}")
        self.tableWidget_audio_paths.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_audio_paths.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_audio_paths.setLineWidth(1)
        self.tableWidget_audio_paths.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_audio_paths.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_audio_paths.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_audio_paths.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_audio_paths.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget_audio_paths.setShowGrid(True)
        self.tableWidget_audio_paths.setCornerButtonEnabled(True)
        self.tableWidget_audio_paths.setObjectName("tableWidget_audio_paths")
        self.tableWidget_audio_paths.setColumnCount(2)
        self.tableWidget_audio_paths.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_audio_paths.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_audio_paths.setHorizontalHeaderItem(1, item)
        self.tableWidget_audio_paths.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_audio_paths.horizontalHeader().setStretchLastSection(True)
        self.groupBox_music_paths_gridLayout.addWidget(self.tableWidget_audio_paths, 0, 0, 1, 1)
        self.tab_general_gridLayout.addWidget(self.groupBox_audio_paths, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_general, "")
        self.MainWidget_gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.widget_footer = QtWidgets.QWidget(MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_footer.sizePolicy().hasHeightForWidth())
        self.widget_footer.setSizePolicy(sizePolicy)
        self.widget_footer.setMinimumSize(QtCore.QSize(0, 40))
        self.widget_footer.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_footer.setAutoFillBackground(False)
        self.widget_footer.setObjectName("widget_footer")
        self.widget_footer_horizontalLayout = QtWidgets.QHBoxLayout(self.widget_footer)
        self.widget_footer_horizontalLayout.setContentsMargins(0, 4, 6, 4)
        self.widget_footer_horizontalLayout.setObjectName("widget_footer_horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(498, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.widget_footer_horizontalLayout.addItem(spacerItem1)
        self.widget_footer_buttons = QtWidgets.QWidget(self.widget_footer)
        self.widget_footer_buttons.setStyleSheet("QPushButton {\n"
"background-color: rgb(60, 60, 60);\n"
"border-radius: 5%;\n"
"border: 1px solid rgb(188, 188, 188);\n"
"font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(188, 188, 188);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.widget_footer_buttons.setObjectName("widget_footer_buttons")
        self.widget_footer_buttons_gridLayout = QtWidgets.QGridLayout(self.widget_footer_buttons)
        self.widget_footer_buttons_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_footer_buttons_gridLayout.setVerticalSpacing(0)
        self.widget_footer_buttons_gridLayout.setObjectName("widget_footer_buttons_gridLayout")
        self.button_ok = QtWidgets.QPushButton(self.widget_footer_buttons)
        self.button_ok.setMinimumSize(QtCore.QSize(80, 32))
        self.button_ok.setMaximumSize(QtCore.QSize(80, 32))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.button_ok.setFont(font)
        self.button_ok.setStyleSheet("")
        self.button_ok.setObjectName("button_ok")
        self.widget_footer_buttons_gridLayout.addWidget(self.button_ok, 0, 0, 1, 1)
        self.button_cancel = QtWidgets.QPushButton(self.widget_footer_buttons)
        self.button_cancel.setMinimumSize(QtCore.QSize(80, 32))
        self.button_cancel.setMaximumSize(QtCore.QSize(80, 32))
        self.button_cancel.setSizeIncrement(QtCore.QSize(0, 0))
        self.button_cancel.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.button_cancel.setFont(font)
        self.button_cancel.setStyleSheet("")
        self.button_cancel.setObjectName("button_cancel")
        self.widget_footer_buttons_gridLayout.addWidget(self.button_cancel, 0, 1, 1, 1)
        self.button_apply = QtWidgets.QPushButton(self.widget_footer_buttons)
        self.button_apply.setMinimumSize(QtCore.QSize(80, 32))
        self.button_apply.setMaximumSize(QtCore.QSize(80, 32))
        self.button_apply.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.button_apply.setFont(font)
        self.button_apply.setStyleSheet("")
        self.button_apply.setObjectName("button_apply")
        self.widget_footer_buttons_gridLayout.addWidget(self.button_apply, 0, 2, 1, 1)
        self.widget_footer_horizontalLayout.addWidget(self.widget_footer_buttons)
        self.MainWidget_gridLayout.addWidget(self.widget_footer, 2, 0, 1, 1)

        self.retranslateUi(MainWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWidget)

    def retranslateUi(self, MainWidget):
        _translate = QtCore.QCoreApplication.translate
        MainWidget.setWindowTitle(_translate("MainWidget", "Settings"))
        self.groupBox_audio_paths.setTitle(_translate("MainWidget", "Paths"))
        self.button_add_path.setText(_translate("MainWidget", "Add"))
        self.button_delete_path.setText(_translate("MainWidget", "Delete"))
        self.button_edit_path.setText(_translate("MainWidget", "Edit"))
        self.tableWidget_audio_paths.setSortingEnabled(True)
        item = self.tableWidget_audio_paths.horizontalHeaderItem(0)
        item.setText(_translate("MainWidget", "R"))
        item = self.tableWidget_audio_paths.horizontalHeaderItem(1)
        item.setText(_translate("MainWidget", "Path"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("MainWidget", "General"))
        self.button_ok.setText(_translate("MainWidget", "OK"))
        self.button_cancel.setText(_translate("MainWidget", "Cancel"))
        self.button_apply.setText(_translate("MainWidget", "Apply"))

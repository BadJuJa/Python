# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWidget(object):
    def setupUi(self, MainWidget):
        if not MainWidget.objectName():
            MainWidget.setObjectName(u"MainWidget")
        MainWidget.setEnabled(True)
        MainWidget.resize(851, 582)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWidget.sizePolicy().hasHeightForWidth())
        MainWidget.setSizePolicy(sizePolicy)
        MainWidget.setMinimumSize(QSize(750, 500))
        MainWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"selection-background-color: rgb(188, 188, 188);\n"
"selection-color: rgb(0, 0, 0);\n"
"border-color: rgb(15, 15, 15);\n"
"background-color: rgb(63, 63, 63);\n"
"alternate-background-color: rgb(188, 188, 188);\n"
"\n"
"QMenuBar::item:selected {\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.MainWidget_gridLayout = QGridLayout(MainWidget)
        self.MainWidget_gridLayout.setSpacing(0)
        self.MainWidget_gridLayout.setObjectName(u"MainWidget_gridLayout")
        self.MainWidget_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(MainWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.tabWidget.setFont(font)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"QTabBar {\n"
"	font: 13pt \"Century Gothic\";\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QTabBar:tab {\n"
"	font: 13pt \"Century Gothic\";\n"
"	background-color: rgb(63, 63, 63);\n"
"\n"
"}\n"
"QTabBar:tab:hover {\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0)\n"
"}\n"
"QTabBar:tab:selected {\n"
"	background-color: rgb(160, 160, 160);\n"
"	color: rgb(12, 12, 12);\n"
"}\n"
"\n"
"QTabWidget::pane {}")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_general = QWidget()
        self.tab_general.setObjectName(u"tab_general")
        self.tab_general.setStyleSheet(u"")
        self.tab_general_gridLayout = QGridLayout(self.tab_general)
        self.tab_general_gridLayout.setSpacing(0)
        self.tab_general_gridLayout.setObjectName(u"tab_general_gridLayout")
        self.tab_general_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_music_paths = QGroupBox(self.tab_general)
        self.groupBox_music_paths.setObjectName(u"groupBox_music_paths")
        self.groupBox_music_paths.setStyleSheet(u"")
        self.groupBox_music_paths.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_music_paths.setFlat(True)
        self.groupBox_music_paths.setCheckable(False)
        self.groupBox_music_paths_gridLayout = QGridLayout(self.groupBox_music_paths)
        self.groupBox_music_paths_gridLayout.setObjectName(u"groupBox_music_paths_gridLayout")
        self.groupBox_music_paths_gridLayout.setContentsMargins(5, 5, 5, 0)
        self.widget_music_paths_buttons = QWidget(self.groupBox_music_paths)
        self.widget_music_paths_buttons.setObjectName(u"widget_music_paths_buttons")
        self.widget_music_paths_buttons_verticalLayout = QVBoxLayout(self.widget_music_paths_buttons)
        self.widget_music_paths_buttons_verticalLayout.setSpacing(5)
        self.widget_music_paths_buttons_verticalLayout.setObjectName(u"widget_music_paths_buttons_verticalLayout")
        self.widget_music_paths_buttons_verticalLayout.setContentsMargins(5, 0, 5, 0)
        self.button_add_path = QPushButton(self.widget_music_paths_buttons)
        self.button_add_path.setObjectName(u"button_add_path")
        self.button_add_path.setMinimumSize(QSize(80, 0))
        self.button_add_path.setMaximumSize(QSize(80, 16777215))
        self.button_add_path.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"} ")

        self.widget_music_paths_buttons_verticalLayout.addWidget(self.button_add_path)

        self.button_delete_path = QPushButton(self.widget_music_paths_buttons)
        self.button_delete_path.setObjectName(u"button_delete_path")
        self.button_delete_path.setMinimumSize(QSize(80, 0))
        self.button_delete_path.setMaximumSize(QSize(80, 16777215))
        self.button_delete_path.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"} ")

        self.widget_music_paths_buttons_verticalLayout.addWidget(self.button_delete_path)

        self.button_edit_path = QPushButton(self.widget_music_paths_buttons)
        self.button_edit_path.setObjectName(u"button_edit_path")
        self.button_edit_path.setMinimumSize(QSize(80, 0))
        self.button_edit_path.setMaximumSize(QSize(80, 16777215))
        self.button_edit_path.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"} ")

        self.widget_music_paths_buttons_verticalLayout.addWidget(self.button_edit_path)

        self.verticalSpacer = QSpacerItem(20, 318, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.widget_music_paths_buttons_verticalLayout.addItem(self.verticalSpacer)


        self.groupBox_music_paths_gridLayout.addWidget(self.widget_music_paths_buttons, 0, 1, 1, 1)

        self.tableWidget_music_paths = QTableWidget(self.groupBox_music_paths)
        if (self.tableWidget_music_paths.columnCount() < 2):
            self.tableWidget_music_paths.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_music_paths.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_music_paths.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_music_paths.setObjectName(u"tableWidget_music_paths")
        self.tableWidget_music_paths.setStyleSheet(u"QHeaderView {\n"
"	background: transparent;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	background-color: rgb(63, 63, 63);\n"
"	color: white;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"	background-color: rgb(63,63, 63);\n"
"	border: 0px solid;\n"
"}")
        self.tableWidget_music_paths.setFrameShape(QFrame.StyledPanel)
        self.tableWidget_music_paths.setFrameShadow(QFrame.Sunken)
        self.tableWidget_music_paths.setLineWidth(1)
        self.tableWidget_music_paths.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_music_paths.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_music_paths.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_music_paths.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_music_paths.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tableWidget_music_paths.setShowGrid(True)
        self.tableWidget_music_paths.setSortingEnabled(True)
        self.tableWidget_music_paths.setCornerButtonEnabled(True)
        self.tableWidget_music_paths.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget_music_paths.horizontalHeader().setStretchLastSection(True)

        self.groupBox_music_paths_gridLayout.addWidget(self.tableWidget_music_paths, 0, 0, 1, 1)


        self.tab_general_gridLayout.addWidget(self.groupBox_music_paths, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_general, "")
        self.tab_interface = QWidget()
        self.tab_interface.setObjectName(u"tab_interface")
        self.tab_interface_gridLayout = QGridLayout(self.tab_interface)
        self.tab_interface_gridLayout.setSpacing(0)
        self.tab_interface_gridLayout.setObjectName(u"tab_interface_gridLayout")
        self.tab_interface_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox_current_song_parameters = QGroupBox(self.tab_interface)
        self.groupBox_current_song_parameters.setObjectName(u"groupBox_current_song_parameters")
        self.groupBox_current_song_parameters.setStyleSheet(u"")
        self.groupBox_current_song_parameters_gridLayout = QGridLayout(self.groupBox_current_song_parameters)
        self.groupBox_current_song_parameters_gridLayout.setObjectName(u"groupBox_current_song_parameters_gridLayout")
        self.groupBox_current_song_parameters_gridLayout.setHorizontalSpacing(25)
        self.button_radio_dials = QRadioButton(self.groupBox_current_song_parameters)
        self.button_radio_dials.setObjectName(u"button_radio_dials")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        self.button_radio_dials.setFont(font1)
        self.button_radio_dials.setChecked(False)

        self.groupBox_current_song_parameters_gridLayout.addWidget(self.button_radio_dials, 0, 1, 1, 1)

        self.button_radio_sliders = QRadioButton(self.groupBox_current_song_parameters)
        self.button_radio_sliders.setObjectName(u"button_radio_sliders")
        self.button_radio_sliders.setFont(font1)
        self.button_radio_sliders.setChecked(True)

        self.groupBox_current_song_parameters_gridLayout.addWidget(self.button_radio_sliders, 1, 1, 1, 1)

        self.label_style = QLabel(self.groupBox_current_song_parameters)
        self.label_style.setObjectName(u"label_style")
        self.label_style.setFont(font1)
        self.label_style.setAlignment(Qt.AlignCenter)

        self.groupBox_current_song_parameters_gridLayout.addWidget(self.label_style, 0, 0, 1, 1)


        self.tab_interface_gridLayout.addWidget(self.groupBox_current_song_parameters, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_interface, "")

        self.MainWidget_gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.widget_footer = QWidget(MainWidget)
        self.widget_footer.setObjectName(u"widget_footer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_footer.sizePolicy().hasHeightForWidth())
        self.widget_footer.setSizePolicy(sizePolicy1)
        self.widget_footer.setMinimumSize(QSize(0, 40))
        self.widget_footer.setMaximumSize(QSize(16777215, 40))
        self.widget_footer.setAutoFillBackground(False)
        self.widget_footer_horizontalLayout = QHBoxLayout(self.widget_footer)
        self.widget_footer_horizontalLayout.setObjectName(u"widget_footer_horizontalLayout")
        self.widget_footer_horizontalLayout.setContentsMargins(0, 4, 6, 4)
        self.horizontalSpacer = QSpacerItem(498, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.widget_footer_horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_footer_buttons = QWidget(self.widget_footer)
        self.widget_footer_buttons.setObjectName(u"widget_footer_buttons")
        self.widget_footer_buttons_gridLayout = QGridLayout(self.widget_footer_buttons)
        self.widget_footer_buttons_gridLayout.setObjectName(u"widget_footer_buttons_gridLayout")
        self.widget_footer_buttons_gridLayout.setVerticalSpacing(0)
        self.widget_footer_buttons_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_ok = QPushButton(self.widget_footer_buttons)
        self.button_ok.setObjectName(u"button_ok")
        self.button_ok.setMinimumSize(QSize(80, 32))
        self.button_ok.setMaximumSize(QSize(80, 32))
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.button_ok.setFont(font2)
        self.button_ok.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"} ")

        self.widget_footer_buttons_gridLayout.addWidget(self.button_ok, 0, 0, 1, 1)

        self.button_cancel = QPushButton(self.widget_footer_buttons)
        self.button_cancel.setObjectName(u"button_cancel")
        self.button_cancel.setMinimumSize(QSize(80, 32))
        self.button_cancel.setMaximumSize(QSize(80, 32))
        self.button_cancel.setSizeIncrement(QSize(0, 0))
        self.button_cancel.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(16)
        font3.setBold(False)
        font3.setItalic(False)
        self.button_cancel.setFont(font3)
        self.button_cancel.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"} ")

        self.widget_footer_buttons_gridLayout.addWidget(self.button_cancel, 0, 1, 1, 1)

        self.button_apply = QPushButton(self.widget_footer_buttons)
        self.button_apply.setObjectName(u"button_apply")
        self.button_apply.setMinimumSize(QSize(80, 32))
        self.button_apply.setMaximumSize(QSize(80, 32))
        self.button_apply.setBaseSize(QSize(0, 0))
        self.button_apply.setFont(font3)
        self.button_apply.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(60, 60, 60);\n"
"	border-radius: 5%;\n"
"    border: 1px solid rgb(188, 188, 188);\n"
"	font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(188, 188, 188);\n"
"	color: rgb(0, 0, 0);\n"
"} ")

        self.widget_footer_buttons_gridLayout.addWidget(self.button_apply, 0, 2, 1, 1)


        self.widget_footer_horizontalLayout.addWidget(self.widget_footer_buttons)


        self.MainWidget_gridLayout.addWidget(self.widget_footer, 2, 0, 1, 1)


        self.retranslateUi(MainWidget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWidget)
    # setupUi

    def retranslateUi(self, MainWidget):
        MainWidget.setWindowTitle(QCoreApplication.translate("MainWidget", u"Settings", None))
        self.groupBox_music_paths.setTitle(QCoreApplication.translate("MainWidget", u"Music paths", None))
        self.button_add_path.setText(QCoreApplication.translate("MainWidget", u"Add", None))
        self.button_delete_path.setText(QCoreApplication.translate("MainWidget", u"Delete", None))
        self.button_edit_path.setText(QCoreApplication.translate("MainWidget", u"Edit", None))
        ___qtablewidgetitem = self.tableWidget_music_paths.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWidget", u"R", None));
        ___qtablewidgetitem1 = self.tableWidget_music_paths.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWidget", u"Path", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), QCoreApplication.translate("MainWidget", u"General", None))
        self.groupBox_current_song_parameters.setTitle(QCoreApplication.translate("MainWidget", u"Current song parameters", None))
        self.button_radio_dials.setText(QCoreApplication.translate("MainWidget", u"Dials", None))
        self.button_radio_sliders.setText(QCoreApplication.translate("MainWidget", u"Sliders", None))
        self.label_style.setText(QCoreApplication.translate("MainWidget", u"Style", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_interface), QCoreApplication.translate("MainWidget", u"Interface", None))
        self.button_ok.setText(QCoreApplication.translate("MainWidget", u"OK", None))
        self.button_cancel.setText(QCoreApplication.translate("MainWidget", u"Cancel", None))
        self.button_apply.setText(QCoreApplication.translate("MainWidget", u"Apply", None))
    # retranslateUi


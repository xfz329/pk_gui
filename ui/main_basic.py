# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_basic.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1140, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/fig/cbeis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.widget = QtWidgets.QWidget(MainWindow)
        self.widget.setMinimumSize(QtCore.QSize(1140, 0))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_table = DataTableWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_table.sizePolicy().hasHeightForWidth())
        self.widget_table.setSizePolicy(sizePolicy)
        self.widget_table.setMinimumSize(QtCore.QSize(700, 0))
        self.widget_table.setMaximumSize(QtCore.QSize(700, 16777215))
        self.widget_table.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget_table.setObjectName("widget_table")
        self.gridLayout.addWidget(self.widget_table, 0, 0, 11, 1)
        self.pushButton_open = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_open.sizePolicy().hasHeightForWidth())
        self.pushButton_open.setSizePolicy(sizePolicy)
        self.pushButton_open.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_open.setObjectName("pushButton_open")
        self.gridLayout.addWidget(self.pushButton_open, 0, 1, 1, 1)
        self.pushButton_copy = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_copy.sizePolicy().hasHeightForWidth())
        self.pushButton_copy.setSizePolicy(sizePolicy)
        self.pushButton_copy.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.gridLayout.addWidget(self.pushButton_copy, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(1, 37, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 1, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 1, 3, 3)
        self.label_pk = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pk.sizePolicy().hasHeightForWidth())
        self.label_pk.setSizePolicy(sizePolicy)
        self.label_pk.setMinimumSize(QtCore.QSize(200, 40))
        self.label_pk.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_pk.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_pk.setFont(font)
        self.label_pk.setText("")
        self.label_pk.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pk.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_pk.setObjectName("label_pk")
        self.gridLayout.addWidget(self.label_pk, 3, 2, 3, 1)
        spacerItem1 = QtWidgets.QSpacerItem(1, 43, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 3, 2, 1)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(200, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(200, 40))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 7, 1, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(207, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 8, 2, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 9, 1, 1, 3)
        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 400, 343))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_assit = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_assit.sizePolicy().hasHeightForWidth())
        self.label_assit.setSizePolicy(sizePolicy)
        self.label_assit.setMinimumSize(QtCore.QSize(300, 0))
        self.label_assit.setSizeIncrement(QtCore.QSize(0, 0))
        self.label_assit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_assit.setText("")
        self.label_assit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_assit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.label_assit.setObjectName("label_assit")
        self.gridLayout_2.addWidget(self.label_assit, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 10, 1, 1, 3)
        MainWindow.setCentralWidget(self.widget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1140, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_author = QtWidgets.QAction(MainWindow)
        self.action_author.setObjectName("action_author")
        self.action_logs = QtWidgets.QAction(MainWindow)
        self.action_logs.setObjectName("action_logs")
        self.action_calcualte_pk = QtWidgets.QAction(MainWindow)
        self.action_calcualte_pk.setObjectName("action_calcualte_pk")
        self.menu.addAction(self.action_open)
        self.menu_2.addAction(self.action_calcualte_pk)
        self.help.addAction(self.action_author)
        self.help.addAction(self.action_logs)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "麻醉深度评估PK值计算器"))
        self.pushButton_open.setText(_translate("MainWindow", "打开并计算PK"))
        self.pushButton_copy.setText(_translate("MainWindow", "复制PK值至粘贴板"))
        self.label.setText(_translate("MainWindow", "计算结果"))
        self.label_2.setText(_translate("MainWindow", "辅助变量"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "计算"))
        self.help.setTitle(_translate("MainWindow", "关于"))
        self.action_open.setText(_translate("MainWindow", "打开并计算PK"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_author.setText(_translate("MainWindow", "作者"))
        self.action_author.setShortcut(_translate("MainWindow", "F1"))
        self.action_logs.setText(_translate("MainWindow", "更新日志"))
        self.action_logs.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.action_calcualte_pk.setText(_translate("MainWindow", "计算PK"))
        self.action_calcualte_pk.setShortcut(_translate("MainWindow", "Ctrl+D"))
from qtpandas.views.DataTableView import DataTableWidget
import resource.label_rc
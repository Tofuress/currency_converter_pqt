# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 609)
        MainWindow.setStyleSheet("background: #BDB76B;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(540, 0, 541, 101))
        self.frame_2.setStyleSheet("background-color: #FAFAD2")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 311, 81))
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 861, 621))
        self.tabWidget.setStyleSheet("QTabBar::tab {\n"
"    height: 91px;\n"
"    width: 263px;\n"
"    border: 2px solid #B8860B;\n"
"    border-bottom-color: #B8860B;\n"
"    background-color: #F0E68C;\n"
"    padding: 2px;\n"
"    \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #FAFAD2;\n"
"    border-bottom-color: #f66867;\n"
"}\n"
"\n"
"QTabWidget {\n"
"    border: none;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("")
        self.tab.setObjectName("tab")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(120, 20, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.input_currency = QtWidgets.QComboBox(self.tab)
        self.input_currency.setGeometry(QtCore.QRect(10, 70, 261, 60))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(10)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;\n"
"")
        self.input_currency.setObjectName("input_currency")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.input_currency.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(140, 210, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.input_text_currency = QtWidgets.QTextEdit(self.tab)
        self.input_text_currency.setGeometry(QtCore.QRect(330, 70, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(10)
        self.input_text_currency.setFont(font)
        self.input_text_currency.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.input_text_currency.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;")
        self.input_text_currency.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.input_text_currency.setObjectName("input_text_currency")
        self.input_amount = QtWidgets.QLineEdit(self.tab)
        self.input_amount.setGeometry(QtCore.QRect(10, 150, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(12)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 56, 51))
        self.label_2.setObjectName("label_2")
        self.output_currency = QtWidgets.QComboBox(self.tab)
        self.output_currency.setGeometry(QtCore.QRect(10, 250, 261, 60))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(10)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;")
        self.output_currency.setObjectName("output_currency")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_currency.addItem("")
        self.output_text_currency = QtWidgets.QTextEdit(self.tab)
        self.output_text_currency.setGeometry(QtCore.QRect(330, 250, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(10)
        self.output_text_currency.setFont(font)
        self.output_text_currency.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.output_text_currency.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;")
        self.output_text_currency.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.output_text_currency.setObjectName("output_text_currency")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(290, 250, 56, 51))
        self.label_3.setObjectName("label_3")
        self.output_amount = QtWidgets.QLineEdit(self.tab)
        self.output_amount.setGeometry(QtCore.QRect(10, 330, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(12)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;\n"
"border-radius: 20;\n"
"")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setReadOnly(True)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(70, 420, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background: #EEE8AA;\n"
"border: 2px solid #f66867;")
        self.pushButton.setObjectName("pushButton")
        self.history_list = QtWidgets.QListWidget(self.tab)
        self.history_list.setGeometry(QtCore.QRect(540, 0, 351, 441))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(16)
        self.history_list.setFont(font)
        self.history_list.setStyleSheet("background: #EEE8AA;\n"
"    width: 263px;\n"
"    border: 2px solid #B8860B;\n"
"    padding: 2px;")
        self.history_list.setObjectName("history_list")
        self.clear_1 = QtWidgets.QPushButton(self.tab)
        self.clear_1.setGeometry(QtCore.QRect(590, 460, 221, 31))
        self.clear_1.setStyleSheet("QPushButton{\n"
"background-color: #FFE4B5;\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FAEBD7;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #BDB76B;\n"
"}")
        self.clear_1.setObjectName("clear_1")
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.input_currency.raise_()
        self.label_5.raise_()
        self.input_text_currency.raise_()
        self.input_amount.raise_()
        self.output_currency.raise_()
        self.output_text_currency.raise_()
        self.output_amount.raise_()
        self.pushButton.raise_()
        self.history_list.raise_()
        self.clear_1.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #FAEBD7;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #BDB76B;\n"
"}")
        self.tab_2.setObjectName("tab_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 150, 541, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.layout_btns = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.layout_btns.setContentsMargins(0, 0, 0, 0)
        self.layout_btns.setObjectName("layout_btns")
        self.btn_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setObjectName("btn_3")
        self.layout_btns.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setObjectName("btn_1")
        self.layout_btns.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_plus_min = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus_min.sizePolicy().hasHeightForWidth())
        self.btn_plus_min.setSizePolicy(sizePolicy)
        self.btn_plus_min.setObjectName("btn_plus_min")
        self.layout_btns.addWidget(self.btn_plus_min, 4, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setObjectName("btn_8")
        self.layout_btns.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setObjectName("btn_0")
        self.layout_btns.addWidget(self.btn_0, 4, 1, 1, 1)
        self.btn_ce = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy)
        self.btn_ce.setObjectName("btn_ce")
        self.layout_btns.addWidget(self.btn_ce, 0, 1, 1, 1)
        self.btn_baepsae = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_baepsae.sizePolicy().hasHeightForWidth())
        self.btn_baepsae.setSizePolicy(sizePolicy)
        self.btn_baepsae.setObjectName("btn_baepsae")
        self.layout_btns.addWidget(self.btn_baepsae, 0, 2, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy)
        self.btn_4.setObjectName("btn_4")
        self.layout_btns.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setObjectName("btn_5")
        self.layout_btns.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setObjectName("btn_9")
        self.layout_btns.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setObjectName("btn_6")
        self.layout_btns.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_c = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_c.sizePolicy().hasHeightForWidth())
        self.btn_c.setSizePolicy(sizePolicy)
        self.btn_c.setObjectName("btn_c")
        self.layout_btns.addWidget(self.btn_c, 0, 0, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setObjectName("btn_dot")
        self.layout_btns.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setObjectName("btn_7")
        self.layout_btns.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setObjectName("btn_2")
        self.layout_btns.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_div = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setObjectName("btn_div")
        self.layout_btns.addWidget(self.btn_div, 0, 3, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mult.sizePolicy().hasHeightForWidth())
        self.btn_mult.setSizePolicy(sizePolicy)
        self.btn_mult.setObjectName("btn_mult")
        self.layout_btns.addWidget(self.btn_mult, 1, 3, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy)
        self.btn_minus.setObjectName("btn_minus")
        self.layout_btns.addWidget(self.btn_minus, 2, 3, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy)
        self.btn_plus.setObjectName("btn_plus")
        self.layout_btns.addWidget(self.btn_plus, 3, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_eq.sizePolicy().hasHeightForWidth())
        self.btn_eq.setSizePolicy(sizePolicy)
        self.btn_eq.setObjectName("btn_eq")
        self.layout_btns.addWidget(self.btn_eq, 4, 3, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 60, 541, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("border:none;\n"
"background-color: #FFE4B5;\n"
"padding-right: 10px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.history_list_2 = QtWidgets.QListWidget(self.tab_2)
        self.history_list_2.setGeometry(QtCore.QRect(540, 0, 321, 441))
        font = QtGui.QFont()
        font.setFamily("Felix Titling")
        font.setPointSize(16)
        self.history_list_2.setFont(font)
        self.history_list_2.setStyleSheet("background: #EEE8AA;\n"
"    width: 263px;\n"
"    border: 2px solid #B8860B;\n"
"    padding: 2px;")
        self.history_list_2.setObjectName("history_list_2")
        self.label = QtWidgets.QLineEdit(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 541, 61))
        self.label.setStyleSheet("background-color: #FFFFE0;\n"
"padding: 10px;\n"
"border: none;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.clear_2 = QtWidgets.QPushButton(self.tab_2)
        self.clear_2.setGeometry(QtCore.QRect(590, 460, 221, 31))
        self.clear_2.setStyleSheet("QPushButton{\n"
"background-color: #FFE4B5;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #FAEBD7;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #BDB76B;\n"
"}")
        self.clear_2.setObjectName("clear_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Конвертер валют"))
        self.label_8.setText(_translate("MainWindow", "История операций"))
        self.label_4.setText(_translate("MainWindow", "Введите исходную сумму и её валюту "))
        self.input_currency.setItemText(0, _translate("MainWindow", "Найдите валюту в списке"))
        self.input_currency.setItemText(1, _translate("MainWindow", "RUB - Рубль"))
        self.input_currency.setItemText(2, _translate("MainWindow", "USD - Доллар США"))
        self.input_currency.setItemText(3, _translate("MainWindow", "EUR - Евро"))
        self.input_currency.setItemText(4, _translate("MainWindow", "JPY - Японская йена"))
        self.input_currency.setItemText(5, _translate("MainWindow", "GBP - Британский фунт стерлингов"))
        self.input_currency.setItemText(6, _translate("MainWindow", "CAD - Канадский доллар"))
        self.input_currency.setItemText(7, _translate("MainWindow", "AUD - Австралийский доллар"))
        self.input_currency.setItemText(8, _translate("MainWindow", "CHF - Швейцарский франк"))
        self.input_currency.setItemText(9, _translate("MainWindow", "SGD - Сингапурский доллар"))
        self.input_currency.setItemText(10, _translate("MainWindow", "HKD - Гонконгский доллар"))
        self.input_currency.setItemText(11, _translate("MainWindow", "SEK - Шведская крона"))
        self.input_currency.setItemText(12, _translate("MainWindow", "NOK - Норвежская крона"))
        self.input_currency.setItemText(13, _translate("MainWindow", "DKK - Датская крона"))
        self.input_currency.setItemText(14, _translate("MainWindow", "NZD - Новозеландский доллар"))
        self.input_currency.setItemText(15, _translate("MainWindow", "ZAR - Южноафриканский рэнд"))
        self.input_currency.setItemText(16, _translate("MainWindow", "BRL - Бразильский реал"))
        self.input_currency.setItemText(17, _translate("MainWindow", "KRW - Южнокорейская вона"))
        self.input_currency.setItemText(18, _translate("MainWindow", "CNY - Китайский юань"))
        self.input_currency.setItemText(19, _translate("MainWindow", "INR - Индийская рупия"))
        self.input_currency.setItemText(20, _translate("MainWindow", "MYR - Малайзийский ринггит"))
        self.input_currency.setItemText(21, _translate("MainWindow", "THB - Тайский бат"))
        self.input_currency.setItemText(22, _translate("MainWindow", "MXN - Мексиканское песо"))
        self.input_currency.setItemText(23, _translate("MainWindow", "PHP - Филиппинское песо"))
        self.input_currency.setItemText(24, _translate("MainWindow", "HUF - Венгерский форинт"))
        self.input_currency.setItemText(25, _translate("MainWindow", "IDR - Индонезийская рупия"))
        self.input_currency.setItemText(26, _translate("MainWindow", "CZK - Чешская крона"))
        self.input_currency.setItemText(27, _translate("MainWindow", "RON - Румынский лей"))
        self.input_currency.setItemText(28, _translate("MainWindow", "TRY - Турецкая лира"))
        self.input_currency.setItemText(29, _translate("MainWindow", "ISK - Исландская крона"))
        self.input_currency.setItemText(30, _translate("MainWindow", "HRK - Хорватская куна"))
        self.input_currency.setItemText(31, _translate("MainWindow", "BGN - Болгарский лев"))
        self.input_currency.setItemText(32, _translate("MainWindow", "NZD - Новозеландский доллар"))
        self.input_currency.setItemText(33, _translate("MainWindow", "PLN - Польский злотый"))
        self.input_currency.setItemText(34, _translate("MainWindow", "LTL - Литовский лит"))
        self.input_currency.setItemText(35, _translate("MainWindow", "SIT - Словенский толар"))
        self.input_currency.setItemText(36, _translate("MainWindow", "ROL - Румынский лей"))
        self.input_currency.setItemText(37, _translate("MainWindow", "TRL - Турецкая лира"))
        self.input_currency.setItemText(38, _translate("MainWindow", "SKK - Словацкая крона"))
        self.input_currency.setItemText(39, _translate("MainWindow", "LVL - Латвийский лат"))
        self.input_currency.setItemText(40, _translate("MainWindow", "MTL - Мальтийская лира"))
        self.input_currency.setItemText(41, _translate("MainWindow", "EEK - Эстонская крона"))
        self.input_currency.setItemText(42, _translate("MainWindow", "CYP - Кипрский фунт"))
        self.label_5.setText(_translate("MainWindow", "Введите валюту конечной суммы"))
        self.input_text_currency.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Felix Titling\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "или"))
        self.output_currency.setItemText(0, _translate("MainWindow", "Найдите валюту в списке"))
        self.output_currency.setItemText(1, _translate("MainWindow", "RUB - Рубль"))
        self.output_currency.setItemText(2, _translate("MainWindow", "USD - Доллар США"))
        self.output_currency.setItemText(3, _translate("MainWindow", "EUR - Евро"))
        self.output_currency.setItemText(4, _translate("MainWindow", "JPY - Японская йена"))
        self.output_currency.setItemText(5, _translate("MainWindow", "GBP - Британский фунт стерлингов"))
        self.output_currency.setItemText(6, _translate("MainWindow", "CAD - Канадский доллар"))
        self.output_currency.setItemText(7, _translate("MainWindow", "AUD - Австралийский доллар"))
        self.output_currency.setItemText(8, _translate("MainWindow", "CHF - Швейцарский франк"))
        self.output_currency.setItemText(9, _translate("MainWindow", "SGD - Сингапурский доллар"))
        self.output_currency.setItemText(10, _translate("MainWindow", "HKD - Гонконгский доллар"))
        self.output_currency.setItemText(11, _translate("MainWindow", "SEK - Шведская крона"))
        self.output_currency.setItemText(12, _translate("MainWindow", "NOK - Норвежская крона"))
        self.output_currency.setItemText(13, _translate("MainWindow", "DKK - Датская крона"))
        self.output_currency.setItemText(14, _translate("MainWindow", "NZD - Новозеландский доллар"))
        self.output_currency.setItemText(15, _translate("MainWindow", "ZAR - Южноафриканский рэнд"))
        self.output_currency.setItemText(16, _translate("MainWindow", "BRL - Бразильский реал"))
        self.output_currency.setItemText(17, _translate("MainWindow", "KRW - Южнокорейская вона"))
        self.output_currency.setItemText(18, _translate("MainWindow", "CNY - Китайский юань"))
        self.output_currency.setItemText(19, _translate("MainWindow", "INR - Индийская рупия"))
        self.output_currency.setItemText(20, _translate("MainWindow", "MYR - Малайзийский ринггит"))
        self.output_currency.setItemText(21, _translate("MainWindow", "THB - Тайский бат"))
        self.output_currency.setItemText(22, _translate("MainWindow", "MXN - Мексиканское песо"))
        self.output_currency.setItemText(23, _translate("MainWindow", "PHP - Филиппинское песо"))
        self.output_currency.setItemText(24, _translate("MainWindow", "HUF - Венгерский форинт"))
        self.output_currency.setItemText(25, _translate("MainWindow", "IDR - Индонезийская рупия"))
        self.output_currency.setItemText(26, _translate("MainWindow", "CZK - Чешская крона"))
        self.output_currency.setItemText(27, _translate("MainWindow", "RON - Румынский лей"))
        self.output_currency.setItemText(28, _translate("MainWindow", "TRY - Турецкая лира"))
        self.output_currency.setItemText(29, _translate("MainWindow", "ISK - Исландская крона"))
        self.output_currency.setItemText(30, _translate("MainWindow", "HRK - Хорватская куна"))
        self.output_currency.setItemText(31, _translate("MainWindow", "BGN - Болгарский лев"))
        self.output_currency.setItemText(32, _translate("MainWindow", "NZD - Новозеландский доллар"))
        self.output_currency.setItemText(33, _translate("MainWindow", "PLN - Польский злотый"))
        self.output_currency.setItemText(34, _translate("MainWindow", "LTL - Литовский лит"))
        self.output_currency.setItemText(35, _translate("MainWindow", "SIT - Словенский толар"))
        self.output_currency.setItemText(36, _translate("MainWindow", "ROL - Румынский лей"))
        self.output_currency.setItemText(37, _translate("MainWindow", "TRL - Турецкая лира"))
        self.output_currency.setItemText(38, _translate("MainWindow", "SKK - Словацкая крона"))
        self.output_currency.setItemText(39, _translate("MainWindow", "LVL - Латвийский лат"))
        self.output_currency.setItemText(40, _translate("MainWindow", "MTL - Мальтийская лира"))
        self.output_currency.setItemText(41, _translate("MainWindow", "EEK - Эстонская крона"))
        self.output_currency.setItemText(42, _translate("MainWindow", "CYP - Кипрский фунт"))
        self.output_text_currency.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Felix Titling\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "или"))
        self.pushButton.setText(_translate("MainWindow", "КОНВЕРТИРОВАТЬ"))
        self.clear_1.setText(_translate("MainWindow", "Очистить историю"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Конвертер"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.btn_plus_min.setText(_translate("MainWindow", "-"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_ce.setText(_translate("MainWindow", "CE"))
        self.btn_baepsae.setText(_translate("MainWindow", "<-"))
        self.btn_baepsae.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_dot.setShortcut(_translate("MainWindow", "."))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_mult.setShortcut(_translate("MainWindow", "*"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_minus.setShortcut(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_plus.setShortcut(_translate("MainWindow", "+"))
        self.btn_eq.setText(_translate("MainWindow", "="))
        self.btn_eq.setShortcut(_translate("MainWindow", "="))
        self.lineEdit.setText(_translate("MainWindow", "0"))
        self.clear_2.setText(_translate("MainWindow", "Очистить историю"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Калькулятор"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_order.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(54)
        sizePolicy.setVerticalStretch(115)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(540, 420))
        MainWindow.setMaximumSize(QtCore.QSize(540, 420))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 291, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.date_start = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.date_start.setObjectName("date_start")
        self.gridLayout.addWidget(self.date_start, 3, 0, 1, 1)
        self.event_id_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.event_id_combo.setObjectName("event_id_combo")
        self.gridLayout.addWidget(self.event_id_combo, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.date_end = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.date_end.setObjectName("date_end")
        self.gridLayout.addWidget(self.date_end, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.status_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.status_combo.setObjectName("status_combo")
        self.gridLayout.addWidget(self.status_combo, 5, 0, 1, 1)
        self.room_id_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.room_id_combo.setObjectName("room_id_combo")
        self.gridLayout.addWidget(self.room_id_combo, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.work_type_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.work_type_combo.setObjectName("work_type_combo")
        self.gridLayout.addWidget(self.work_type_combo, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.description_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description_text.setGeometry(QtCore.QRect(310, 110, 201, 161))
        self.description_text.setObjectName("description_text")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 149, 40))
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 290, 160, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ok_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout.addWidget(self.ok_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.cancel_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить заявку"))
        self.label_2.setText(_translate("MainWindow", "Помещение:"))
        self.label_4.setText(_translate("MainWindow", "Конец:"))
        self.label_3.setText(_translate("MainWindow", "Начало:"))
        self.label.setText(_translate("MainWindow", "id мероприятия:"))
        self.label_6.setText(_translate("MainWindow", "Статус:"))
        self.label_7.setText(_translate("MainWindow", "Вид работы:"))
        self.label_5.setText(_translate("MainWindow", "Описание:"))
        self.ok_btn.setText(_translate("MainWindow", "Ok"))
        self.cancel_btn.setText(_translate("MainWindow", "Отмена"))

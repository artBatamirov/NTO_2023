# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'club.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 352)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 731, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.teacher_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.teacher_combo.setObjectName("teacher_combo")
        self.gridLayout.addWidget(self.teacher_combo, 8, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.room_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.room_combo.setObjectName("room_combo")
        self.gridLayout.addWidget(self.room_combo, 4, 1, 1, 1)
        self.time_end_edit = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.time_end_edit.setObjectName("time_end_edit")
        self.gridLayout.addWidget(self.time_end_edit, 7, 1, 1, 1)
        self.club_type_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.club_type_combo.setObjectName("club_type_combo")
        self.gridLayout.addWidget(self.club_type_combo, 4, 0, 1, 1)
        self.date_start_edit = QtWidgets.QDateEdit(self.gridLayoutWidget)
        self.date_start_edit.setObjectName("date_start_edit")
        self.gridLayout.addWidget(self.date_start_edit, 2, 1, 1, 1)
        self.time_start_edit = QtWidgets.QTimeEdit(self.gridLayoutWidget)
        self.time_start_edit.setObjectName("time_start_edit")
        self.gridLayout.addWidget(self.time_start_edit, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.check_1 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_1.setObjectName("check_1")
        self.button_group = QtWidgets.QButtonGroup(MainWindow)
        self.button_group.setObjectName("button_group")
        self.button_group.setExclusive(False)
        self.button_group.addButton(self.check_1)
        self.horizontalLayout.addWidget(self.check_1)
        self.check_2 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_2.setObjectName("check_2")
        self.button_group.addButton(self.check_2)
        self.horizontalLayout.addWidget(self.check_2)
        self.check_3 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_3.setObjectName("check_3")
        self.button_group.addButton(self.check_3)
        self.horizontalLayout.addWidget(self.check_3)
        self.check_4 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_4.setObjectName("check_4")
        self.button_group.addButton(self.check_4)
        self.horizontalLayout.addWidget(self.check_4)
        self.check_5 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_5.setObjectName("check_5")
        self.button_group.addButton(self.check_5)
        self.horizontalLayout.addWidget(self.check_5)
        self.check_6 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_6.setObjectName("check_6")
        self.button_group.addButton(self.check_6)
        self.horizontalLayout.addWidget(self.check_6)
        self.check_7 = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.check_7.setObjectName("check_7")
        self.button_group.addButton(self.check_7)
        self.horizontalLayout.addWidget(self.check_7)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(self.centralwidget)
        self.ok_btn.setGeometry(QtCore.QRect(30, 270, 75, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(110, 270, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(200, 270, 231, 16))
        self.label_error.setText("")
        self.label_error.setObjectName("label_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавить кружок"))
        self.label_3.setText(_translate("MainWindow", "Вид кружка:"))
        self.label_5.setText(_translate("MainWindow", "Кол-во занятий в неделю( от 1 до 3):"))
        self.label_8.setText(_translate("MainWindow", "Преподаватель:"))
        self.label_2.setText(_translate("MainWindow", "Дата начала работы кружка:"))
        self.label_4.setText(_translate("MainWindow", "Помещение:"))
        self.label_7.setText(_translate("MainWindow", "Время окончания:"))
        self.label_6.setText(_translate("MainWindow", "Время начала:"))
        self.check_1.setText(_translate("MainWindow", "Пн"))
        self.check_2.setText(_translate("MainWindow", "Вт"))
        self.check_3.setText(_translate("MainWindow", "Ср"))
        self.check_4.setText(_translate("MainWindow", "Чт"))
        self.check_5.setText(_translate("MainWindow", "Пт"))
        self.check_6.setText(_translate("MainWindow", "Сб"))
        self.check_7.setText(_translate("MainWindow", "Вс"))
        self.label.setText(_translate("MainWindow", "Название:"))
        self.ok_btn.setText(_translate("MainWindow", "Ok"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))

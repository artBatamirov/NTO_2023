# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'book.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(543, 272)
        self.comment_text = QtWidgets.QPlainTextEdit(Form)
        self.comment_text.setGeometry(QtCore.QRect(350, 60, 161, 111))
        self.comment_text.setObjectName("comment_text")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(350, 30, 81, 16))
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 30, 281, 160))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(20, 30, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.event_id_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.event_id_combo.setObjectName("event_id_combo")
        self.gridLayout.addWidget(self.event_id_combo, 1, 0, 1, 1)
        self.start_edit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.start_edit.setObjectName("start_edit")
        self.gridLayout.addWidget(self.start_edit, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.room_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.room_combo.setObjectName("room_combo")
        self.gridLayout.addWidget(self.room_combo, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)
        self.end_edit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget)
        self.end_edit.setObjectName("end_edit")
        self.gridLayout.addWidget(self.end_edit, 3, 1, 1, 1)
        self.part_combo = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.part_combo.setObjectName("part_combo")
        self.part_combo.addItem("")
        self.part_combo.addItem("")
        self.gridLayout.addWidget(self.part_combo, 5, 0, 1, 1)
        self.ok_btn = QtWidgets.QPushButton(Form)
        self.ok_btn.setGeometry(QtCore.QRect(40, 230, 87, 23))
        self.ok_btn.setObjectName("ok_btn")
        self.cancel_btn = QtWidgets.QPushButton(Form)
        self.cancel_btn.setGeometry(QtCore.QRect(130, 230, 179, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(26, 10, 271, 20))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить бронирование"))
        self.label_5.setText(_translate("Form", "Комментарий:"))
        self.label_7.setText(_translate("Form", "Часть комнаты:"))
        self.label_3.setText(_translate("Form", "Конец:"))
        self.label_2.setText(_translate("Form", "id мероприятия:"))
        self.label_4.setText(_translate("Form", "Начало:"))
        self.label_6.setText(_translate("Form", "Помещение:"))
        self.part_combo.setItemText(0, _translate("Form", "часть"))
        self.part_combo.setItemText(1, _translate("Form", "полностью"))
        self.ok_btn.setText(_translate("Form", "Ok"))
        self.cancel_btn.setText(_translate("Form", "Cancel"))

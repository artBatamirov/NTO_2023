import sys
import io
import sqlite3
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QWidget, \
    QAbstractItemView, QTableWidgetItem
import datetime
from ui import Ui_MainWindow
from add_ui import Ui_MainWindow1
from add_order import Ui_MainWindow2
from book import Ui_MainWindow3
from club import Ui_MainWindow4

conn = sqlite3.connect("culture_centr.db")
cur = conn.cursor()

def check_date(date1, date2):

    date1 = datetime.datetime.strptime(date1[0], "%d.%m.%Y %H:%M:%S")
    date2 = datetime.datetime.strptime(date1[1], "%d.%m.%Y %H:%M:%S")
    date3 = datetime.datetime.strptime(date2[0], "%d.%m.%Y %H:%M:%S")
    date4 = datetime.datetime.strptime(date2[1], "%d.%m.%Y %H:%M:%S")

    if date3 >= date4:
        return False
    if date3 >= date1 and date3 <= date2 or date4 >= date1 and date4 <= date2:
        return False
    else:
        return True

def convert_to_date(date):

    date = datetime.datetime.strptime(date, "%d.%m.%Y %H:%M:%S")
    return date



# check_date('03.12.2023', '08:49:00', '04.12.2023', '15:16:00')


class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.titles = ['id', 'event_id', 'room', 'date_start', 'date_end',
                       'description', 'status', 'work_type']
        self.modified = []
        self.setupUi(self)
        # uic.loadUi('ui.ui', self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(800, 500)
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("culture_centr.db")

        self.tableView_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_4.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_4.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.tableView_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.work_type_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.work_type_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.work_type_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.work_type_3.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.room_1.setSelectionMode(QAbstractItemView.SingleSelection)
        self.room_1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.room_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.room_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.room_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.room_3.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.order_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.order_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.order_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.order_3.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.book_2_7.setSelectionMode(QAbstractItemView.SingleSelection)
        self.book_2_7.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.book_3_7.setSelectionMode(QAbstractItemView.SingleSelection)
        self.book_3_7.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.table_2.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_3.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table_3.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.teacher_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.teacher_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.club_type_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.club_type_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.club_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.club_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.load_data()
        self.add_btn_2_2.clicked.connect(self.add_type)
        self.add_btn_3_2.clicked.connect(self.add_type)
        self.reload_btn.clicked.connect(self.load_data)
        self.add_btn_2_1.clicked.connect(self.open_second_form)
        self.add_btn_3_1.clicked.connect(self.open_second_form)
        self.del_btn_2_1.clicked.connect(self.del_row)
        self.del_btn_3_1.clicked.connect(self.del_row)
        self.del_btn_2_2.clicked.connect(self.del_row)
        self.del_btn_3_2.clicked.connect(self.del_row)

        self.del_btn_2_4.clicked.connect(self.del_row_name)
        self.del_btn_2_5.clicked.connect(self.del_row_name)
        self.del_btn_3_4.clicked.connect(self.del_row_name)
        self.del_btn_3_5.clicked.connect(self.del_row_name)
        self.del_btn_1_1.clicked.connect(self.del_row_name)

        self.add_btn_2_4.clicked.connect(self.add_name)
        self.add_btn_2_5.clicked.connect(self.add_name)
        self.add_btn_3_4.clicked.connect(self.add_name)
        self.add_btn_3_5.clicked.connect(self.add_name)
        self.add_btn_1_1.clicked.connect(self.add_name)

        self.del_btn_2_3.clicked.connect(self.del_order)
        self.del_btn_3_3.clicked.connect(self.del_order)

        self.add_btn_2_3.clicked.connect(self.add_order)
        self.add_btn_3_3.clicked.connect(self.add_order)
        self.change_btn_2_3.clicked.connect(self.change_order)
        self.change_btn_3_3.clicked.connect(self.change_order)

        self.del_btn_2_7.clicked.connect(self.del_booking)
        self.del_btn_3_7.clicked.connect(self.del_booking)

        self.add_btn_2_7.clicked.connect(self.open_book_form)
        self.add_btn_3_7.clicked.connect(self.open_book_form)

        self.combo_2_6.currentTextChanged.connect(self.load_desktop)
        self.combo_3_6.currentTextChanged.connect(self.load_desktop)

        self.change_btn_2_7.clicked.connect(self.change_book_form)
        self.change_btn_3_7.clicked.connect(self.change_book_form)

        self.book_btn_2_1.clicked.connect(self.open_book_form)
        self.book_btn_3_1.clicked.connect(self.open_book_form)

        self.book_btn_2_8.clicked.connect(self.open_book_form)
        self.book_btn_3_8.clicked.connect(self.open_book_form)

        self.date_edit_2.dateTimeChanged.connect(self.load_rooms)
        self.date_edit_3.dateTimeChanged.connect(self.load_rooms)

        self.del_btn_1_2.clicked.connect(self.del_row_name)
        self.del_btn_1_3.clicked.connect(self.del_row_name)
        self.add_btn_1_2.clicked.connect(self.add_name)
        self.add_btn_1_3.clicked.connect(self.add_name)

        self.add_btn_1_5.clicked.connect(self.open_club_from)
        self.del_btn_1_5.clicked.connect(self.del_club)
        self.change_btn_1_5.clicked.connect(self.open_club_from)
    def add_type(self):
        type, ok_pressed = QInputDialog.getText(self, 'Введите тип мероприятия', '', )
        if ok_pressed:
            print(type)
            cur.execute("""INSERT INTO event_type(type) VALUES(?)""", (type,))
            conn.commit()
            self.load_data()

    def add_name(self):
        db_names = ['add_btn_2_4', 'add_btn_3_4']
        if self.sender().objectName() in db_names:
            text = 'Введите вид работы:'
        elif self.sender().objectName() == 'add_btn_1_2':
            text = 'Введите имя преподавателя:'
        elif self.sender().objectName() == 'add_btn_1_3':
            text = 'Введите вид кружка:'
        else:
            text = 'Введите название помещения:'
        name, ok_pressed = QInputDialog.getText(self, text, '', )
        if ok_pressed:
            if self.sender().objectName() in db_names:
                cur.execute("""INSERT INTO work_type(name) VALUES(?)""", (name,))
            elif self.sender().objectName() == 'add_btn_1_2':
                cur.execute("""INSERT INTO teacher(name) VALUES(?)""", (name,))
            elif self.sender().objectName() == 'add_btn_1_3':
                cur.execute("""INSERT INTO club_type(name) VALUES(?)""", (name,))
            else:
                cur.execute("""INSERT INTO room(name) VALUES(?)""", (name,))
            conn.commit()
            self.load_data()

    def load_data(self):
        try:
            self.model1 = QSqlTableModel(self)
            self.model1.setTable("event")
            self.model1.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model1.setHeaderData(0, Qt.Horizontal, "id")
            self.model1.setHeaderData(1, Qt.Horizontal, "date")
            self.model1.setHeaderData(2, Qt.Horizontal, "type")
            self.model1.setHeaderData(3, Qt.Horizontal, "description")
            self.model1.select()

            self.model2 = QSqlTableModel(self)
            self.model2.setTable("event_type")
            self.model2.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model2.setHeaderData(0, Qt.Horizontal, "id")
            self.model2.setHeaderData(1, Qt.Horizontal, "type")
            self.model2.select()

            self.model4 = QSqlTableModel(self)
            self.model4.setTable("work_type")
            self.model4.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model4.setHeaderData(0, Qt.Horizontal, "id")
            self.model4.setHeaderData(1, Qt.Horizontal, "name")
            self.model4.select()

            self.model5 = QSqlTableModel(self)
            self.model5.setTable("room")
            self.model5.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model5.setHeaderData(0, Qt.Horizontal, "id")
            self.model5.setHeaderData(1, Qt.Horizontal, "name")
            self.model5.select()

            self.tableView_3.setModel(self.model1)
            self.tableView_3.resizeColumnsToContents()
            self.tableView_4.setModel(self.model1)
            self.tableView_4.resizeColumnsToContents()

            self.tableView_2.setModel(self.model2)
            self.tableView_2.resizeColumnsToContents()
            self.tableView.setModel(self.model2)
            self.tableView.resizeColumnsToContents()

            self.work_type_2.setModel(self.model4)
            self.work_type_2.resizeColumnsToContents()
            self.work_type_3.setModel(self.model4)
            self.work_type_3.resizeColumnsToContents()

            self.room_1.setModel(self.model5)
            self.room_1.resizeColumnsToContents()
            self.room_2.setModel(self.model5)
            self.room_2.resizeColumnsToContents()
            self.room_3.setModel(self.model5)
            self.room_3.resizeColumnsToContents()

            self.model6 = QSqlTableModel(self)
            self.model6.setTable("teacher")
            self.model6.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model6.setHeaderData(0, Qt.Horizontal, "id")
            self.model6.setHeaderData(1, Qt.Horizontal, "name")
            self.model6.select()
            self.teacher_table.setModel(self.model6)
            self.teacher_table.resizeColumnsToContents()

            self.model7 = QSqlTableModel(self)
            self.model7.setTable("club_type")
            self.model7.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model7.setHeaderData(0, Qt.Horizontal, "id")
            self.model7.setHeaderData(1, Qt.Horizontal, "name")
            self.model7.select()
            self.club_type_table.setModel(self.model7)
            self.club_type_table.resizeColumnsToContents()

            self.model8 = QSqlTableModel(self)
            self.model8.setTable("weekday")
            self.model8.setEditStrategy(QSqlTableModel.OnFieldChange)
            self.model8.select()
            self.weekday_table.setModel(self.model8)
            self.weekday_table.setEnabled(False)
            self.weekday_table.resizeColumnsToContents()


            # заявки
            result = cur.execute("""SELECT wo.id, event_id, r.name, date_start, date_end, description, s.name , w.name 
                                    FROM work_order as wo INNER JOIN room as r ON r.id = wo.room_id INNER JOIN 
                                    status as s ON s.id = wo.status_id INNER JOIN work_type as w 
                                    ON w.id = wo.work_type_id""").fetchall()
            if len(result) != 0:
                self.order_2.setColumnCount(len(result[0]))
                self.order_2.setHorizontalHeaderLabels(self.titles)
                self.order_3.setColumnCount(len(result[0]))
                self.order_3.setHorizontalHeaderLabels(self.titles)
                self.order_2.setRowCount(0)
                self.order_3.setRowCount(0)
                for i, row in enumerate(result):
                    self.order_2.setRowCount(self.order_2.rowCount() + 1)
                    self.order_3.setRowCount(self.order_3.rowCount() + 1)
                    colors = {'Выполнена': (255, 255, 255), 'К выполнению': (255, 192, 203), 'Создана': (128, 128, 128)}
                    color = colors[row[6]]
                    for j, elem in enumerate(row):
                        self.order_2.setItem(i, j, QTableWidgetItem(str(elem)))
                        self.order_2.item(i, j).setBackground(QColor(color[0], color[1], color[2]))
                        self.order_3.setItem(i, j, QTableWidgetItem(str(elem)))
                        self.order_3.item(i, j).setBackground(QColor(color[0], color[1], color[2]))

                self.order_2.resizeColumnsToContents()
                self.order_3.resizeColumnsToContents()

            combo_list = cur.execute("SELECT name FROM work_type").fetchall()
            self.combo_2_6.clear()
            self.combo_3_6.clear()
            for i in combo_list:
                self.combo_2_6.addItem(i[0])
                self.combo_3_6.addItem(i[0])

            self.desktop_2.setColumnCount(6)
            self.desktop_2.setHorizontalHeaderLabels(['id', 'event_id', 'room_id', 'date_start', 'date_end',
                                                      'description'])
            self.desktop_3.setColumnCount(6)
            self.desktop_3.setHorizontalHeaderLabels(['id', 'event_id', 'room_id', 'date_start', 'date_end',
                                                      'description'])

            self.load_desktop()
            self.load_book()
            self.load_club()


        except Exception as e:
            print(e)

    def load_desktop(self):
        try:
            # рабочий стол
            result = cur.execute("""SELECT id, event_id, room_id, date_start, date_end, description, work_type_id
                                    FROM work_order WHERE status_id = 2""").fetchall()
            self.desktop_2.setRowCount(0)
            self.desktop_3.setRowCount(0)
            if len(result) != 0:
                id2 = cur.execute("""SELECT id FROM work_type WHERE name = ?""",
                                  (self.combo_2_6.currentText(),)).fetchone()[0]
                id3 = cur.execute("""SELECT id FROM work_type WHERE name = ?""",
                                  (self.combo_3_6.currentText(),)).fetchone()[0]

                for i, row in enumerate([elem[:-1] for elem in result if elem[6] == id2]):

                    self.desktop_2.setRowCount(self.desktop_2.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.desktop_2.setItem(i, j, QTableWidgetItem(str(elem)))

                for i, row in enumerate([elem[:-1] for elem in result if elem[6] == id3]):
                    self.desktop_3.setRowCount(self.desktop_3.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.desktop_3.setItem(i, j, QTableWidgetItem(str(elem)))

                self.desktop_2.resizeColumnsToContents()
                self.desktop_3.resizeColumnsToContents()
        except Exception as e:
            print(e)

    def load_club(self):
        try:
            # кружки
            self.club_table.setColumnCount(11)
            self.club_table.setHorizontalHeaderLabels(['id', 'name', 'date_start', 'club_type', 'room',
                                                'class_1', 'class_2', 'class_3', 'time_start', 'time_end', 'teacher'])

            result = cur.execute("""SELECT c.id, c.name, date_start, ct.name as club_type, r.name as room, class_1,
             class_2, class_3, time_start, time_end, t.name as teacher FROM club as c INNER JOIN club_type as ct
              ON c.club_type_id = ct.id INNER JOIN room as r ON r.id = c.room_id INNER JOIN teacher as t
               ON t.id = c.teacher_id""").fetchall()
            print(result)
            self.club_table.setRowCount(0)
            for i, row in enumerate(result):
                self.club_table.setRowCount(self.club_table.rowCount() + 1)
                for j, elem in enumerate(row):
                    if elem is None:
                        elem = ''
                    self.club_table.setItem(i, j, QTableWidgetItem(str(elem)))
            self.club_table.resizeColumnsToContents()
        except Exception as e:
            print(e)

    def open_club_from(self):
        data = []
        if self.sender().objectName() == 'change_btn_1_5':
            row = -1
            for index in sorted(self.club_table.selectionModel().selectedRows()):
                row = index.row()
            if row == -1:
                return None
            for col in range(self.club_table.model().columnCount()):
                data.append(self.club_table.model().data(self.club_table.model().index(row, col)))
        self.club_form = ClubForm(self, data)
        self.club_form.show()

    def del_club(self):
        table = self.club_table
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
        data = []

        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(100, 100)
        msg.setText(
            f'''Вы дейсвительно хотите удалить данные?\nid: {data[0]}
name: {data[1]}\ndate_start: {data[2]}\nclub_type: {data[3]}\nroom: {data[4]}
classes: {data[5]}, {data[6]}, {data[7]}\ntime_start: {data[8]}\ntime_end: {data[9]}\nteacher: {data[10]}''')
        msg.setWindowTitle("Удалить данные")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if msg.clickedButton().text() == 'OK':
            cur.execute("""DELETE FROM club WHERE id = ?""", (data[0],))
            conn.commit()
            self.load_data()

    def load_book(self):
        result = cur.execute("""SELECT b.id, event_id, date, date_start, time_start, date_end, time_end, r.name, 
comment, part_of_room 
FROM 
booking b
INNER JOIN 
room r
ON b.room_id = r.id""").fetchall()
        print(result)
        if len(result) != 0:
            self.book_2_7.setColumnCount(len(result[0]))
            self.book_2_7.setHorizontalHeaderLabels(
                ['id', 'event_id', 'date', 'date_start', 'time_start', 'date_end', 'time_end', 'room', 'comment',
                 'part_of_room'])
            self.book_3_7.setColumnCount(len(result[0]))
            self.book_3_7.setHorizontalHeaderLabels(
                ['id', 'event_id', 'date', 'date_start', 'time_start', 'date_end', 'time_end', 'room', 'comment',
                 'part_of_room'])
            self.book_2_7.setRowCount(0)
            self.book_3_7.setRowCount(0)
            for i, row in enumerate(result):
                self.book_2_7.setRowCount(self.book_2_7.rowCount() + 1)
                self.book_3_7.setRowCount(self.book_3_7.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.book_2_7.setItem(i, j, QTableWidgetItem(str(elem)))
                    self.book_3_7.setItem(i, j, QTableWidgetItem(str(elem)))

            self.book_2_7.resizeColumnsToContents()
            self.book_3_7.resizeColumnsToContents()

    def del_booking(self):

        btn = {'del_btn_2_7': self.book_2_7, 'del_btn_3_7': self.book_3_7}
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
        data = []

        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(100, 100)
        msg.setText(
            f'''Вы дейсвительно хотите удалить данные?\nid: {data[0]}
date: {data[1]}\nevent: {data[2]}\ndata_start: {data[3]}\ntime_start: {data[4]}
data_end: {data[5]}\ntime_end: {data[6]}\nroom: {data[7]}\ncomment: {data[8]}\npart_of_room: {data[9]}''')
        msg.setWindowTitle("Удалить данные")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        if msg.clickedButton().text() == 'OK':
            cur.execute("""DELETE FROM booking WHERE id = ?""", (data[0],))
            conn.commit()
            self.load_data()

    def del_row(self):

        f = True
        btn = {'del_btn_2_1': self.tableView_3, 'del_btn_3_1': self.tableView_4,
               'del_btn_2_2': self.tableView, 'del_btn_3_2': self.tableView_2}
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
            # print('row', row)
        # print(row, table.objectName())
        data = []
        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        # print(data, self.sender().objectName())

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(100, 100)

        if len(data) == 4:

            type = 'Null'
            try:
                type = cur.execute("""SELECT type FROM event_type WHERE id = ?""", (data[2],)).fetchone()[0]
                type = f'{type}({data[2]})'
            except Exception as e:
                print(e)

            msg.setText(
                f'''Вы дейсвительно хотите удалить данные?\ndate: {data[1]}\ntype: {type}\ndescription: {data[3]}''')

        else:

            not_del = conn.execute("""SELECT id FROM event WHERE type = ?""", (data[0],)).fetchall()
            # print(not_del)
            if len(not_del) == 0:
                f = True

                msg.setText(f'''Вы дейсвительно хотите удалить данные?\ntype: {data[1]}''')
            else:
                f = False

                msg.setText(f'''Нельзя удалить данные\ntype: {data[1]}''')
                msg.setStandardButtons(QMessageBox.Cancel)

        msg.setWindowTitle("Удалить данные")
        if f:
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        if msg.clickedButton().text() == 'OK':

            if len(data) == 4:
                cur.execute("""DELETE FROM event WHERE id = ?""", (data[0],))
            elif f:
                cur.execute("""DELETE FROM event_type WHERE id = ?""", (data[0],))
            conn.commit()
            self.load_data()

    def del_row_name(self):
        f = True
        btn = {'del_btn_2_4': self.work_type_2, 'del_btn_2_5': self.room_2,
               'del_btn_3_4': self.work_type_3, 'del_btn_3_5': self.room_3,
               'del_btn_1_1': self.room_1,
               'del_btn_1_2': self.teacher_table, 'del_btn_1_3': self.club_type_table}
        db_names = ['del_btn_2_4', 'del_btn_3_4']
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
        data = []
        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(100, 100)

        if self.sender().objectName() in db_names[0]:
            not_del = conn.execute("""SELECT id FROM work_order WHERE work_type_id = ?""", (data[0],)).fetchall()
        elif self.sender().objectName() == 'del_btn_1_2':
            not_del = conn.execute("""SELECT id FROM club WHERE teacher_id = ?""", (data[0],)).fetchall()
        elif self.sender().objectName() == 'del_btn_1_3':
            not_del = conn.execute("""SELECT id FROM club WHERE club_type_id = ?""", (data[0],)).fetchall()
        else:
            not_del = conn.execute("""SELECT id FROM work_order WHERE room_id = ?""", (data[0],)).fetchall()
        # print(not_del)
        if len(not_del) == 0:
            f = True

            msg.setText(f'''Вы дейсвительно хотите удалить данные?\nid: {data[0]}\nname: {data[1]}''')
        else:
            f = False

            msg.setText(f'''Нельзя удалить данные\nid: {data[0]}\nname: {data[1]}''')
            msg.setStandardButtons(QMessageBox.Cancel)

        msg.setWindowTitle("Удалить данные")
        if f:
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        if msg.clickedButton().text() == 'OK':
            if self.sender().objectName() in db_names[0]:
                cur.execute("""DELETE FROM work_type WHERE id = ?""", (data[0],))
            elif self.sender().objectName() == 'del_btn_1_2':
                cur.execute("""DELETE FROM teacher WHERE id = ?""", (data[0],))
            elif self.sender().objectName() == 'del_btn_1_3':
                cur.execute("""DELETE FROM club_type WHERE id = ?""", (data[0],))
            else:
                cur.execute("""DELETE FROM room WHERE id = ?""", (data[0],))
            conn.commit()
            self.load_data()

    def del_order(self):
        btn = {'del_btn_2_3': self.order_2, 'del_btn_3_3': self.order_3}
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
            # print('row', row)
        # print(row, table.objectName())
        data = []
        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        # print(data, self.sender().objectName())

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(150, 100)

        type = 'Null'
        try:
            room = cur.execute("""SELECT name FROM room WHERE id = ?""", (data[2],)).fetchone()[0]
            room = f'{room}({data[2]})'
            work_type = cur.execute("""SELECT name FROM work_type WHERE id = ?""", (data[7],)).fetchone()[0]
            work_type = f'{work_type}({data[7]})'
            status = cur.execute("""SELECT name FROM status WHERE id = ?""", (data[6],)).fetchone()[0]
            status = f'{status}({data[6]})'
        except Exception as e:
            print(e)

        msg.setText(
            f'''Вы дейсвительно хотите удалить данные?
id мероприятия: {data[1]}
комната: {room}
начало: {data[3]}
конец: {data[4]}
описание: {data[5]}
статус: {status}
вид работы: {work_type}''')

        msg.setWindowTitle("Удалить данные")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        if msg.clickedButton().text() == 'OK':
            try:
                cur.execute("""DELETE FROM work_order WHERE id = ?""", (data[0],))
                conn.commit()
                self.load_data()
            except Exception as e:
                print(e)

    def change_order(self):
        btn = {'change_btn_2_3': self.order_2, 'change_btn_3_3': self.order_3}
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()

        data = []
        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        self.order_form = OrderForm(self, data)
        self.order_form.show()

    def add_order(self):
        self.order_form = OrderForm(self, [])
        self.order_form.show()

    def open_second_form(self):
        self.second_form = SecondForm(self)
        self.second_form.show()

    def open_book_form(self):
        data = []
        if self.sender().objectName() in ['book_btn_2_1', 'book_btn_3_1']:
            btn = {'book_btn_2_1': self.tableView_3, 'book_btn_3_1': self.tableView_4}
            table = btn[self.sender().objectName()]
            row = -1
            for index in sorted(table.selectionModel().selectedRows()):
                row = index.row()

            data = []
            if row == -1:
                return None
            data.append(table.model().data(table.model().index(row, 0)))
        if self.sender().objectName() in ['book_btn_2_8', 'book_btn_3_8']:
            btn = {'book_btn_2_8': self.table_2, 'book_btn_3_8': self.table_3}
            table = btn[self.sender().objectName()]
            row = -1
            for index in sorted(table.selectionModel().selectedRows()):
                row = index.row()
            data = []
            if row == -1:
                return None
            data.append(table.model().data(table.model().index(row, 0)))
            data.append(table.model().data(table.model().index(row, 1)))
        if self.sender().objectName() in ['book_btn_2_8', 'book_btn_3_8']:
            self.book_form = BookForm(self, data, True)
            self.book_form.show()
        else:
            self.book_form = BookForm(self, data, False)
            self.book_form.show()
        print(data, 'data: open_book_form')

    def change_book_form(self):
        btn = {'change_btn_2_7': self.book_2_7, 'change_btn_3_7': self.book_3_7}
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()

        data = []
        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        self.book_form = BookForm(self, data, False)
        self.book_form.show()

    def load_rooms(self):
        try:

            btn = {'date_edit_2': self.table_2, 'date_edit_3': self.table_3}
            table = btn[self.sender().objectName()]
            table.clear()
            if self.sender().objectName() == 'load_btn_2_8':
                date = self.date_edit_2.date().toString('dd.MM.yyyy')
            else:
                date = self.date_edit_3.date().toString('dd.MM.yyyy')
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
            room_list = cur.execute("""SELECT r.id, name, b.date_start, b.time_start, b.date_end, b.time_end  
                                            FROM room as r INNER JOIN booking as b ON r.id = b.room_id""").fetchall()
            r_list = cur.execute("""SELECT id, name FROM room""").fetchall()
            table.setColumnCount(2)
            table.setHorizontalHeaderLabels(['id', 'name'])
            table.setRowCount(0)
            not_lst = []
            show_list = []
            for i, row in enumerate(room_list + r_list):
                if len(row) > 2:
                    date1 = datetime.datetime.strptime(row[2], "%d.%m.%Y")
                    date2 = datetime.datetime.strptime(row[4], "%d.%m.%Y")
                    if not (date >= date1 and date <= date2):
                        if row[:2] not in show_list:
                            show_list.append(row[:2])
                    else:
                        not_lst.append(row[1])
                if len(row) == 2:
                    if row not in show_list:
                        show_list.append(row)
            for i in show_list:
                if i[1] in not_lst:
                    show_list.remove(i)
            for i, elem in enumerate(show_list):
                table.setRowCount(table.rowCount() + 1)
                table.setItem(i, 0, QTableWidgetItem(str(elem[0])))
                table.setItem(i, 1, QTableWidgetItem(str(elem[1])))
            table.resizeColumnsToContents()
        except Exception as e:
            print(e)


class SecondForm(QMainWindow, Ui_MainWindow1):
    def __init__(self, main):
        self.main = main
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('add_ui.ui', self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(500, 200)
        types = cur.execute("""SELECT type FROM event_type""").fetchall()
        self.comboBox.clear()
        for i in types:
            self.comboBox.addItem(i[0])
        self.add_btn.clicked.connect(self.add)
        self.cancel_btn.clicked.connect(self.cancel)

    def add(self):
        date = self.dateEdit.date().toString('dd.MM.yyyy')
        type = cur.execute("SELECT id FROM event_type WHERE type = ?", (self.comboBox.currentText(),)).fetchone()[0]
        description = self.plainTextEdit.toPlainText()
        print(description)
        cur.execute("""INSERT INTO event(date, type, description) VALUES(?, ?, ?)""", (date, type, description))
        conn.commit()
        self.main.load_data()
        self.close()

    def cancel(self):
        self.close()

class ClubForm(QMainWindow, Ui_MainWindow4):
    def __init__(self, main, data):
        self.main = main
        self.data = data
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('club.ui', self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(800, 350)
        club_types = cur.execute("""SELECT name FROM club_type""").fetchall()
        rooms = cur.execute("""SELECT name FROM room""").fetchall()
        teachers = cur.execute("""SELECT name FROM teacher""").fetchall()
        self.club_type_combo.clear()
        for i in club_types:
             self.club_type_combo.addItem(i[0])
        self.room_combo.clear()
        for i in rooms:
            self.room_combo.addItem(i[0])
        self.teacher_combo.clear()
        for i in teachers:
            self.teacher_combo.addItem(i[0])
        if self.data:
            self.name_edit.setText(self.data[1])
            date_start = QtCore.QDate.fromString(self.data[2], 'dd.MM.yyyy')
            self.date_start_edit.setDate(date_start)
            self.club_type_combo.setCurrentText(self.data[3])
            self.room_combo.setCurrentText(self.data[4])
            self.teacher_combo.setCurrentText(self.data[10])
            time_start = QtCore.QTime.fromString(self.data[8])
            time_end = QtCore.QTime.fromString(self.data[9])
            self.time_start_edit.setTime(time_start)
            self.time_end_edit.setTime(time_end)
            weekdays = [self.data[5], self.data[6], self.data[7]]
            for btn in self.button_group.buttons():
                if btn.text() in weekdays:
                    btn.setChecked(True)
        for btn in self.button_group.buttons():
            btn.clicked.connect(self.ckeck_quantity)
        self.ok_btn.clicked.connect(self.add)
        self.cancel_btn.clicked.connect(self.cancel)

    def add(self):
        name = self.name_edit.text()
        date_start = self.date_start_edit.date().toString('dd.MM.yyyy')
        club_type_id = cur.execute("SELECT id FROM club_type WHERE name = ?",
                                   (self.club_type_combo.currentText(),)).fetchone()[0]
        room_id = cur.execute("SELECT id FROM room WHERE name = ?",
                                   (self.room_combo.currentText(),)).fetchone()[0]
        quantity = []
        print(1)
        for btn in self.button_group.buttons():
            if btn.isChecked():
                quantity.append(btn.text())
        quantity += [''] * (3 - len(quantity))
        time_start = self.time_start_edit.time().toString()
        time_end = self.time_end_edit.time().toString()
        teacher_id = cur.execute("SELECT id FROM teacher WHERE name = ?",
                                   (self.teacher_combo.currentText(),)).fetchone()[0]
        print(name, date_start, club_type_id, room_id, quantity, time_start, time_end, teacher_id)
        if quantity[0] != '':
            self.label_error.setText('')
            if self.data:
                cur.execute("""UPDATE club SET name = ?, date_start = ?, club_type_id = ?, room_id = ?, class_1 = ?, 
                                class_2 = ?, class_3 = ?, time_start = ?, time_end = ?, teacher_id = ? WHERE id = ?""",
                            (name, date_start, club_type_id, room_id, quantity[0], quantity[1], quantity[2],
                             time_start, time_end, teacher_id, self.data[0]))
            else:
                cur.execute("""INSERT INTO club(name, date_start, club_type_id, room_id, class_1, class_2, class_3, 
                                time_start, time_end, teacher_id) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (name, date_start, club_type_id, room_id, quantity[0], quantity[1], quantity[2],
                             time_start, time_end, teacher_id))
            conn.commit()
            self.main.load_data()
            self.close()
        else:
            self.label_error.setText('Не указаны дни занятий!!!')

    def ckeck_quantity(self):
        s = 0
        for btn in self.button_group.buttons():
            if btn.isChecked():
                s += 1
            if s > 3:
                self.sender().setChecked(False)
    def cancel(self):
        self.close()


class OrderForm(QMainWindow, Ui_MainWindow2):
    def __init__(self, main, data):
        self.main = main
        self.data = data
        print(self.data)
        super().__init__()
        self.setupUi(self)
        # uic.loadUi('add_order.ui', self)
        self.initUi()

    def initUi(self):
        try:
            self.setFixedSize(540, 420)
            event_id_list = cur.execute("""SELECT id FROM event""").fetchall()
            room_list = cur.execute("""SELECT id, name FROM room""").fetchall()
            status_list = cur.execute("""SELECT id, name FROM status""").fetchall()
            work_type_list = cur.execute("""SELECT id, name FROM work_type""").fetchall()

            self.event_id_combo.clear()
            for i in event_id_list:
                self.event_id_combo.addItem(str(i[0]))
            self.room_id_combo.clear()
            for i in room_list:
                self.room_id_combo.addItem(f'{i[1]}({i[0]})')
            self.status_combo.clear()
            for i in status_list:
                self.status_combo.addItem(f'{i[1]}({i[0]})')
            self.work_type_combo.clear()
            for i in work_type_list:
                self.work_type_combo.addItem(f'{i[1]}({i[0]})')
            if self.data:
                self.event_id_combo.setCurrentText(str(self.data[1]))
                r_id = cur.execute("SELECT id FROM room WHERE name = ?", (self.data[2], )).fetchone()[0]
                self.room_id_combo.setCurrentText(f'{self.data[2]}({r_id})')
                s_id = cur.execute("SELECT id FROM status WHERE name = ?", (self.data[6], )).fetchone()[0]
                self.status_combo.setCurrentText(f'{self.data[6]}({s_id})')
                w_id = cur.execute("SELECT id FROM work_type WHERE name = ?", (self.data[7], )).fetchone()[0]
                self.work_type_combo.setCurrentText(f'{self.data[7]}({w_id})')
                date_start = QtCore.QDate.fromString(self.data[3], 'dd.MM.yyyy')
                date_end = QtCore.QDate.fromString(self.data[4], 'dd.MM.yyyy')
                self.date_start.setDate(date_start)
                self.date_end.setDate(date_end)
                self.description_text.appendPlainText(self.data[5])
                print('hello')
            self.ok_btn.clicked.connect(self.add)
            self.cancel_btn.clicked.connect(self.cancel)
        except Exception as e:
            print(e)

    def add(self):
        try:
            start = self.date_start.date().toString('dd.MM.yyyy')
            end = self.date_end.date().toString('dd.MM.yyyy')
            event_id = int(self.event_id_combo.currentText())
            room_id = self.room_id_combo.currentText()
            room_id = int(room_id[room_id.find('(') + 1:-1])
            work_type_id = self.work_type_combo.currentText()
            work_type_id = int(work_type_id[work_type_id.find('(') + 1:-1])
            status_id = self.status_combo.currentText()
            status_id = int(status_id[status_id.find('(') + 1:-1])
            description = self.description_text.toPlainText()
            if self.data:

                cur.execute("""UPDATE work_order SET event_id = ?, room_id = ?, date_start = ?, date_end = ?, 
                description = ?, status_id = ?, work_type_id = ? WHERE id = ?""",
                            (event_id, room_id, start, end, description, status_id, work_type_id, self.data[0]))
            else:
                cur.execute("""INSERT INTO work_order(event_id, room_id, date_start, date_end, description, 
                            status_id, work_type_id) VALUES(?, ?, ?, ?, ?, ?, ?)""",
                        (event_id, room_id, start, end, description, status_id, work_type_id))
            conn.commit()
            self.main.load_data()
            self.close()
        except Exception as e:
            print(e)

    def cancel(self):
        self.close()


class BookForm(QMainWindow, Ui_MainWindow3):
    def __init__(self, main, data, is_room):
        try:
            self.main = main
            self.data = data
            self.is_room = is_room
            super().__init__()
            self.setupUi(self)
            # uic.loadUi('book.ui', self)
            self.initUi()
        except Exception as e:
            print(e)

    def initUi(self):
        try:
            self.label.setText('')
            self.setFixedSize(540, 420)
            self.start_edit.dateTimeChanged.connect(self.load)
            self.end_edit.dateTimeChanged.connect(self.load)
            event_id_list = cur.execute("""SELECT id FROM event""").fetchall()
            room_list = cur.execute("""SELECT id, name FROM room""").fetchall()

            print(room_list, self.data)

            self.event_id_combo.clear()
            if len(self.data) == 1:
                    self.event_id_combo.addItem(str(self.data[0]))
            elif len(self.data) == 2:
                self.room_combo.addItem(f'{self.data[1]}({self.data[0]})')
                for i in event_id_list:
                    self.event_id_combo.addItem(str(i[0]))
            else:
                for i in event_id_list:
                    self.event_id_combo.addItem(str(i[0]))
                # self.event_id_combo.setCurrentIndex(2) //////////////////////////////////////////////////\\\\\\\\
            if not self.is_room:
                self.room_combo.clear()
                self.room_combo.addItem('не указана дата')
            # for i in room_list:
            #     self.room_combo.addItem(f'{i[1]}({i[0]})')

            if len(self.data) == 9:

                self.event_id_combo.setCurrentText(self.data[1])
                print(self.data)
                room_id = cur.execute("SELECT id FROM room WHERE name = ?", (self.data[7],)).fetchone()[0]
                room = f'{self.data[7]}({room_id})'
                self.room_combo.addItem(room)
                self.room_combo.setCurrentText(room)
                self.comment_text.appendPlainText(self.data[8])
                date_start = QtCore.QDate.fromString(self.data[3], 'dd.MM.yyyy')
                time_start = QtCore.QTime.fromString(self.data[4])
                date_end = QtCore.QDate.fromString(self.data[5], 'dd.MM.yyyy')
                time_end = QtCore.QTime.fromString(self.data[6])
                self.start_edit.setDate(date_start)
                self.start_edit.setTime(time_start)
                self.end_edit.setDate(date_end)
                self.end_edit.setTime(time_end)
                self.ok_btn.clicked.connect(self.update)
            else:
                self.ok_btn.clicked.connect(self.add)
            self.cancel_btn.clicked.connect(self.cancel)
        except Exception as e:
            print(e)

    def load(self):
        try:
            if not self.is_room:
                date_start = self.start_edit.date().toString('dd.MM.yyyy')
                time_start = self.start_edit.time().toString()
                date_end = self.end_edit.date().toString('dd.MM.yyyy')
                time_end = self.end_edit.time().toString()
                ds1 = convert_to_date(date_start + ' ' + time_start)
                de1 = convert_to_date(date_end + ' ' + time_end)
                room_list = cur.execute("""SELECT r.id, name, b.date_start, b.time_start, b.date_end, 
                                            b.time_end, b.id, b.part_of_room, division
                                            FROM room as r INNER JOIN booking as b ON r.id = b.room_id""").fetchall()
                r_list = cur.execute("""SELECT id, name, division FROM room """).fetchall()
                self.room_combo.clear()

                if len(room_list + r_list) == 0:
                    self.room_combo.addItem('забронировано')
                if ds1 > de1:
                    self.room_combo.addItem('неправильная дата')
                else:
                    not_corr = []
                    lst = []
                    for i in room_list:
                        ds2 = convert_to_date(i[2] + ' ' + i[3])
                        de2 = convert_to_date(i[4] + ' ' + i[5])
                        if ((ds2 >= ds1 and ds2 <= de1) or (de2 >= ds1 and de2 <= de1) or
                            (ds1 >= ds2 and ds1 <= de2) or (de1 >= ds2 and de1 <= de2)):
                            if len(self.data) == 9 and int(self.data[0]) == i[6]:
                                print(self.data[0], i[6])
                            else:
                                not_corr.append(i[1])
                                print(ds1, de1, ds2, de2, i, False)
                    print(not_corr)
                    print()
                    for i in room_list + r_list:
                        if i[1] not in not_corr and i[1] not in lst:
                            self.room_combo.addItem(f'{i[1]}({i[0]})')
                            lst.append(i[1])
                if len(self.data) == 9:
                    r  =cur.execute("""SELECT id FROM room WHERE name = ?""", (self.data[7], )).fetchone()[0]
                    self.room_combo.setCurrentText(f'{self.data[7]}({r})')
        except Exception as e:
            print(e)
    def add(self):
        try:

            date = datetime.date.today().strftime('%d.%m.%Y')
            date_start = self.start_edit.date().toString('dd.MM.yyyy')
            time_start = self.start_edit.time().toString()
            date_end = self.end_edit.date().toString('dd.MM.yyyy')
            time_end = self.end_edit.time().toString()
            part = self.part_combo.currentText()
            ds1 = convert_to_date(date_start + ' ' + time_start)
            de1 = convert_to_date(date_end + ' ' + time_end)
            if de1 <= ds1:
                self.label.setText('Неправильная дата')
                return None
            event_id = int(self.event_id_combo.currentText())
            room_id = self.room_combo.currentText()
            room_id = int(room_id[room_id.find('(') + 1:-1])
            comment = self.comment_text.toPlainText()

            not_corr = []
            lst = []
            room_list = cur.execute("""SELECT r.id, name, b.date_start, b.time_start, b.date_end, b.time_end  
                                        FROM room as r INNER JOIN booking as b ON r.id = b.room_id""").fetchall()
            f = False
            for i in room_list:
                if i[0] == room_id:
                    ds2 = convert_to_date(i[2] + ' ' + i[3])
                    de2 = convert_to_date(i[4] + ' ' + i[5])
                    if not ((ds2 >= ds1 and ds2 <= de1) or (de2 >= ds1 and de2 <= de1) or
                            (ds1 >= ds2 and ds1 <= de2) or (de1 >= ds2 and de1 <= de2)):
                        f = True

                    else:
                        self.label.setText('Помещение занято')
                        f = False
            if f:
                cur.execute("""INSERT INTO booking(date, event_id, date_start, time_start, 
                                        date_end, time_end, room_id, comment, part_of_room) 
                                        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (date, event_id, date_start, time_start, date_end, time_end, room_id, comment, part))
                conn.commit()
                self.main.load_data()
                self.close()
        except Exception as e:
            print(e)

    def update(self):
        try:
            date = datetime.date.today().strftime('%d.%m.%Y')
            date_start = self.start_edit.date().toString('dd.MM.yyyy')
            time_start = self.start_edit.time().toString()
            date_end = self.end_edit.date().toString('dd.MM.yyyy')
            time_end = self.end_edit.time().toString()
            event_id = int(self.event_id_combo.currentText())
            room_id = self.room_combo.currentText()
            room_id = int(room_id[room_id.find('(') + 1:-1])
            comment = self.comment_text.toPlainText()

            ds1 = convert_to_date(date_start + ' ' + time_start)
            de1 = convert_to_date(date_end + ' ' + time_end)
            room_list = cur.execute("""SELECT r.id, name, b.date_start, b.time_start, b.date_end, b.time_end  
                                        FROM room as r INNER JOIN booking as b ON r.id = b.room_id""").fetchall()
            for i in room_list:
                if i[0] != room_id:
                    ds2 = convert_to_date(i[2] + ' ' + i[3])
                    de2 = convert_to_date(i[4] + ' ' + i[5])
                    if not ((ds2 >= ds1 and ds2 <= de1) or (de2 >= ds1 and de2 <= de1) or
                            (ds1 >= ds2 and ds1 <= de2) or (de1 >= ds2 and de1 <= de2)):
                        cur.execute("""UPDATE booking SET
                                     date = ?, event_id= ?, date_start= ?, time_start= ?, date_end= ?, time_end= ?, 
                                     room_id= ?, comment= ? WHERE id = ?""",
                                    (date, event_id, date_start, time_start, date_end, time_end, room_id, comment,
                                     self.data[0]))
                    else:
                        self.label.setText('Помещение занято')


            conn.commit()
            self.main.load_data()
            self.close()
        except Exception as e:
            print(e)

    def cancel(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

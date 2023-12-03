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



check_date('03.12.2023', '08:49:00', '04.12.2023', '15:16:00')


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.titles = ['id', 'event_id', 'room_id', 'date_start', 'date_end',
                       'description', 'status_id', 'work_type_id']
        self.modified = []
        uic.loadUi('ui.ui', self)
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
        self.order_2.itemChanged.connect(self.item_changed)
        self.order_3.itemChanged.connect(self.item_changed)
        self.change_btn_2_3.clicked.connect(self.save_results)
        self.change_btn_3_3.clicked.connect(self.save_results)

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
        else:
            text = 'Введите название помещения:'
        name, ok_pressed = QInputDialog.getText(self, text, '', )
        if ok_pressed:
            print(name, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            if self.sender().objectName() in db_names:
                cur.execute("""INSERT INTO work_type(name) VALUES(?)""", (name,))
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

            # заявки
            result = cur.execute("""SELECT id, event_id, room_id, date_start, date_end, description, status_id, 
                                                        work_type_id FROM work_order""").fetchall()
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
                    colors = {1: (255, 255, 255), 2: (255, 192, 203), 3: (128, 128, 128)}
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


        except Exception as e:
            print(e)

    def load_desktop(self):
        try:
            # рабочий стол
            result = cur.execute("""SELECT id, event_id, room_id, date_start, date_end, description, work_type_id
                                    FROM work_order WHERE status_id = 2""").fetchall()
            print(result, 'desktop')
            self.desktop_2.setRowCount(0)
            self.desktop_3.setRowCount(0)
            if len(result) != 0:
                id2 = cur.execute("""SELECT id FROM work_type WHERE name = ?""",
                                  (self.combo_2_6.currentText(),)).fetchone()[0]
                id3 = cur.execute("""SELECT id FROM work_type WHERE name = ?""",
                                  (self.combo_3_6.currentText(),)).fetchone()[0]

                for i, row in enumerate([elem[:-1] for elem in result if elem[6] == id2]):

                    print(row)
                    self.desktop_2.setRowCount(self.desktop_2.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.desktop_2.setItem(i, j, QTableWidgetItem(str(elem)))
                        print(i, j, elem, 'yes')

                for i, row in enumerate([elem[:-1] for elem in result if elem[6] == id3]):
                    self.desktop_3.setRowCount(self.desktop_3.rowCount() + 1)
                    for j, elem in enumerate(row):
                        self.desktop_3.setItem(i, j, QTableWidgetItem(str(elem)))

                self.desktop_2.resizeColumnsToContents()
                self.desktop_3.resizeColumnsToContents()
        except Exception as e:
            print(e)

    def load_book(self):
        result = cur.execute("""SELECT b.id, event_id, date, date_start, time_start, date_end, time_end, r.name, comment 
FROM 
booking b
INNER JOIN 
room r
ON b.room_id = r.id""").fetchall()
        print(result)
        if len(result) != 0:
            self.book_2_7.setColumnCount(len(result[0]))
            self.book_2_7.setHorizontalHeaderLabels(
                ['id', 'event', 'date', 'date_start', 'time_start', 'date_end', 'time_end', 'room', 'comment'])
            self.book_3_7.setColumnCount(len(result[0]))
            self.book_3_7.setHorizontalHeaderLabels(
                ['id', 'event', 'date', 'date_start', 'time_start', 'date_end', 'time_end', 'room', 'comment'])
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
data_end: {data[5]}\ntime_end: {data[6]}\nroom: {data[7]}\ncomment: {data[8]}''')
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
               'del_btn_1_1': self.room_1}
        db_names = ['del_btn_2_4', 'del_btn_3_4']
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
        #     print('row', row)
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

        if self.sender().objectName() in db_names[0]:
            not_del = conn.execute("""SELECT id FROM work_order WHERE work_type_id = ?""", (data[0],)).fetchall()
        else:
            not_del = conn.execute("""SELECT id FROM work_order WHERE room_id = ?""", (data[0],)).fetchall()
        # print(not_del)
        if len(not_del) == 0:
            f = True

            msg.setText(f'''Вы дейсвительно хотите удалить данные?\nname: {data[1]}''')
        else:
            f = False

            msg.setText(f'''Нельзя удалить данные\nname: {data[1]}''')
            msg.setStandardButtons(QMessageBox.Cancel)

        msg.setWindowTitle("Удалить данные")
        if f:
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        if msg.clickedButton().text() == 'OK':
            if self.sender().objectName() in db_names[0]:
                cur.execute("""DELETE FROM work_type WHERE id = ?""", (data[0],))
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
            print(data[7])
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

    def item_changed(self, item):

        self.modified.append((self.titles[item.column()], item.text(), int(self.order_2.item(item.row(), 0).text())))
        print(self.modified)

    def save_results(self):
        try:
            for i in self.modified:
                que = "UPDATE work_order SET\n"
                print(i)
                if i[0] not in ['description', 'date_start', 'date_end']:
                    que += f"{i[0]} = {int(i[1])}"
                else:
                    que += f"{i[0]} = '{i[1]}'"
                que += f" WHERE id = {i[2]}"
                print(que)
                cur.execute(que)
            conn.commit()
            self.modified.clear()
            self.load_data()
        except Exception as e:
            print(e)

    def add_order(self):
        self.order_form = OrderForm(self)
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
        self.book_form = BookForm(self, data)
        self.book_form.show()

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
        self.book_form = BookForm(self, data)
        self.book_form.show()


class SecondForm(QMainWindow):
    def __init__(self, main):
        self.main = main
        super().__init__()
        uic.loadUi('add_ui.ui', self)
        self.initUi()

    def initUi(self):
        self.setFixedSize(500, 200)
        types = cur.execute("""SELECT type FROM event_type""").fetchall()
        print(types)
        self.comboBox.clear()
        for i in types:
            self.comboBox.addItem(i[0])
        self.add_btn.clicked.connect(self.add)
        self.cancel_btn.clicked.connect(self.cancel)

    def add(self):
        date = self.dateEdit.date().toString('dd.MM.yyyy')
        print(date)
        type = cur.execute("SELECT id FROM event_type WHERE type = ?", (self.comboBox.currentText(),)).fetchone()[0]
        print(type)
        description = self.plainTextEdit.toPlainText()
        print(description)
        cur.execute("""INSERT INTO event(date, type, description) VALUES(?, ?, ?)""", (date, type, description))
        print(1)
        conn.commit()
        self.main.load_data()
        self.close()

    def cancel(self):
        self.close()


class OrderForm(QMainWindow):
    def __init__(self, main):
        self.main = main
        super().__init__()
        # f1 = io.StringIO(add_ui_templ)
        uic.loadUi('add_order.ui', self)
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


class BookForm(QMainWindow):
    def __init__(self, main, data=[]):
        try:
            self.main = main
            self.data = data
            super().__init__()
            uic.loadUi('book.ui', self)
            self.initUi()
        except Exception as e:
            print(e)

    def initUi(self):
        try:
            self.setFixedSize(540, 420)
            event_id_list = cur.execute("""SELECT id FROM event""").fetchall()
            room_list = cur.execute("""SELECT id, name FROM room""").fetchall()
            print(room_list, self.data)

            self.event_id_combo.clear()
            if len(self.data) == 1:
                self.event_id_combo.addItem(str(self.data[0]))
            else:

                for i in event_id_list:
                    self.event_id_combo.addItem(str(i[0]))
                self.event_id_combo.setCurrentIndex(2)
            self.room_combo.clear()
            for i in room_list:
                self.room_combo.addItem(f'{i[1]}({i[0]})')

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

    def add(self):
        try:
            date = datetime.date.today().strftime('%d.%m.%Y')
            date_start = self.start_edit.date().toString('dd.MM.yyyy')
            time_start = self.start_edit.time().toString()
            date_end = self.end_edit.date().toString('dd.MM.yyyy')
            time_end = self.end_edit.time().toString()
            check_date(date_start, time_start, date_end, time_end)
            event_id = int(self.event_id_combo.currentText())
            room_id = self.room_combo.currentText()
            room_id = int(room_id[room_id.find('(') + 1:-1])
            comment = self.comment_text.toPlainText()
            print(date, event_id, date_start, time_start, date_end, time_end, room_id, comment)
            cur.execute("""INSERT INTO booking(date, event_id, date_start, time_start, date_end, time_end, room_id,
                        comment) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""",
                        (date, event_id, date_start, time_start, date_end, time_end, room_id, comment))

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
            print(date, event_id, date_start, time_start, date_end, time_end, room_id, comment)
            cur.execute("""UPDATE booking SET
             date = ?, event_id= ?, date_start= ?, time_start= ?, date_end= ?, time_end= ?, room_id= ?,
                                comment= ? WHERE id = ?""",
                        (date, event_id, date_start, time_start, date_end, time_end, room_id, comment, self.data[0]))

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

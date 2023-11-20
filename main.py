import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QWidget, QAbstractItemView

conn = sqlite3.connect("culture_centr.db")
cur = conn.cursor()
class App(QMainWindow):
    def __init__(self):
        super().__init__()
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



    def add_type(self):
        type, ok_pressed = QInputDialog.getText(self, 'Введите тип мероприятия', '',)
        if ok_pressed:
            print(type)
            cur.execute("""INSERT INTO event_type(type) VALUES(?)""", (type,))
            conn.commit()
            self.load_data()

    def load_data(self):
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

        self.tableView_3.setModel(self.model1)
        self.tableView_3.resizeColumnsToContents()

        self.tableView_4.setModel(self.model1)
        self.tableView_4.resizeColumnsToContents()

        self.tableView_2.setModel(self.model2)
        self.tableView_2.resizeColumnsToContents()

        self.tableView.setModel(self.model2)
        self.tableView.resizeColumnsToContents()

    def del_row(self):
        f = True
        btn = {'del_btn_2_1': self.tableView_3, 'del_btn_3_1': self.tableView_4,
               'del_btn_2_2': self.tableView, 'del_btn_3_2': self.tableView_2}
        table = btn[self.sender().objectName()]
        row = -1
        for index in sorted(table.selectionModel().selectedRows()):
            row = index.row()
            print('row', row)
        print(row, table.objectName())
        data = []
        if row == -1:
            return None
        for col in range(table.model().columnCount()):
            data.append(table.model().data(table.model().index(row, col)))
        print(data, self.sender().objectName())

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.resize(100, 100)



        if len(data) == 4:

            type = 'Null'
            try:
                type = cur.execute("""SELECT type FROM event_type WHERE id = ?""", (data[2], )).fetchone()[0]
                type = f'{type}({data[2]})'
            except Exception as e:
                print(e)

            msg.setText(f'''Вы дейсвительно хотите удалить данные?\ndate: {data[1]}\ntype: {type}\ndescription: {data[3]}''')

        else:

            not_del = conn.execute("""SELECT id FROM event WHERE type = ?""", (data[0],)).fetchall()
            print(not_del)
            if len(not_del) == 0:
                f = True

                msg.setText(f'''Вы дейсвительно хотите удалить данные?\ntype: {data[1]}''')
            else:
                f = False

                msg.setText(f'''Нельзя удалить данные\ntype: {data[1]}''')


        msg.setWindowTitle("Удалить данные")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

        if msg.clickedButton().text() == 'OK':

            if len(data) == 4:
                cur.execute("""DELETE FROM event WHERE id = ?""", (data[0], ))
            elif f:

                cur.execute("""DELETE FROM event_type WHERE id = ?""", (data[0], ))
            conn.commit()
            self.load_data()

    def open_second_form(self):
            self.second_form = SecondForm(self)
            self.second_form.show()

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
        type = cur.execute("SELECT id FROM event_type WHERE type = ?", (self.comboBox.currentText(), )).fetchone()[0]
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









if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QWidget

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

        self.load_data()
        self.add_btn_2_2.clicked.connect(self.add_type)
        self.add_btn_3_2.clicked.connect(self.add_type)
        self.reload_btn.clicked.connect(self.load_data)
        self.add_btn_2_1.clicked.connect(self.open_second_form)
        self.add_btn_3_1.clicked.connect(self.open_second_form)



    def add_type(self):
        type, ok_pressed = QInputDialog.getText(self, 'Введите тип мероприятия', '',)
        if ok_pressed:
            print(type)
            cur.execute("""INSERT INTO event_type(type) VALUES(?)""", (type,))
            conn.commit()

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
        # Set up the view
        self.tableView_3.setModel(self.model1)
        self.tableView_3.resizeColumnsToContents()

        self.tableView_4.setModel(self.model1)
        self.tableView_4.resizeColumnsToContents()

        self.tableView_2.setModel(self.model2)
        self.tableView_2.resizeColumnsToContents()

        self.tableView.setModel(self.model2)
        self.tableView.resizeColumnsToContents()

    def open_second_form(self):
        self.second_form = SecondForm()
        self.second_form.show()

class SecondForm(QMainWindow):
    def __init__(self):
        super().__init__()
        print(1)
        uic.loadUi('add_ui.ui', self)
        print(2)
        self.initUi()

    def initUi(self):
        # self.setFixedSize(400, 400)
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
        type = self.comboBox.currentText()
        print(type)
        description = self.plainTextEdit.toPlainText()
        print(description)
        cur.execute("""INSERT INTO event(date, type, description) VALUES(?, ?, ?)""", (date, type, description))
        print(1)
        conn.commit()
        self.close()

    def cancel(self):
        self.hide()









if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())
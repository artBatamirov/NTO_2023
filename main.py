import sys
import io
import sqlite3
from PyQt5 import uic
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog, QWidget, \
    QAbstractItemView, QTableWidgetItem

conn = sqlite3.connect("culture_centr.db")
cur = conn.cursor()
ui_templ = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>30</y>
      <width>701</width>
      <height>481</height>
     </rect>
    </property>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <widget class="QTabWidget" name="tabWidget">
       <property name="currentIndex">
        <number>1</number>
       </property>
       <widget class="QWidget" name="tab1">
        <attribute name="title">
         <string>Образование</string>
        </attribute>
        <widget class="QLabel" name="label">
         <property name="geometry">
          <rect>
           <x>30</x>
           <y>20</y>
           <width>81</width>
           <height>31</height>
          </rect>
         </property>
         <property name="text">
          <string>Образование</string>
         </property>
        </widget>
       </widget>
       <widget class="QWidget" name="tab2">
        <attribute name="title">
         <string>Развлечения</string>
        </attribute>
        <widget class="QTabWidget" name="tabWidget_2">
         <property name="geometry">
          <rect>
           <x>0</x>
           <y>0</y>
           <width>691</width>
           <height>451</height>
          </rect>
         </property>
         <property name="currentIndex">
          <number>1</number>
         </property>
         <widget class="QWidget" name="tab2_1">
          <attribute name="title">
           <string>Мероприятия</string>
          </attribute>
          <widget class="QTableView" name="tableView_3">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>681</width>
             <height>251</height>
            </rect>
           </property>
          </widget>
          <widget class="QWidget" name="horizontalLayoutWidget">
           <property name="geometry">
            <rect>
             <x>20</x>
             <y>300</y>
             <width>295</width>
             <height>80</height>
            </rect>
           </property>
           <layout class="QHBoxLayout" name="horizontalLayout">
            <item>
             <widget class="QPushButton" name="add_btn_2_1">
              <property name="text">
               <string>Добавить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup2_1</string>
              </attribute>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="del_btn_2_1">
              <property name="text">
               <string>Удалить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup2_1</string>
              </attribute>
             </widget>
            </item>
           </layout>
          </widget>
         </widget>
         <widget class="QWidget" name="tab2_2">
          <attribute name="title">
           <string>Виды мероприятий</string>
          </attribute>
          <widget class="QTableView" name="tableView">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>681</width>
             <height>251</height>
            </rect>
           </property>
          </widget>
          <widget class="QWidget" name="horizontalLayoutWidget_2">
           <property name="geometry">
            <rect>
             <x>30</x>
             <y>300</y>
             <width>295</width>
             <height>80</height>
            </rect>
           </property>
           <layout class="QHBoxLayout" name="horizontalLayout_2">
            <item>
             <widget class="QPushButton" name="add_btn_2_2">
              <property name="text">
               <string>Добавить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup2_2</string>
              </attribute>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="del_btn_2_2">
              <property name="text">
               <string>Удалить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup2_2</string>
              </attribute>
             </widget>
            </item>
           </layout>
          </widget>
         </widget>
        </widget>
       </widget>
       <widget class="QWidget" name="tab3">
        <attribute name="title">
         <string>Просвещение</string>
        </attribute>
        <widget class="QTabWidget" name="tabWidget_3">
         <property name="geometry">
          <rect>
           <x>0</x>
           <y>0</y>
           <width>691</width>
           <height>451</height>
          </rect>
         </property>
         <property name="currentIndex">
          <number>0</number>
         </property>
         <widget class="QWidget" name="tab3_1">
          <attribute name="title">
           <string>Мероприятия</string>
          </attribute>
          <widget class="QTableView" name="tableView_4">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>681</width>
             <height>251</height>
            </rect>
           </property>
          </widget>
          <widget class="QWidget" name="horizontalLayoutWidget_3">
           <property name="geometry">
            <rect>
             <x>20</x>
             <y>290</y>
             <width>302</width>
             <height>80</height>
            </rect>
           </property>
           <layout class="QHBoxLayout" name="horizontalLayout_4">
            <item>
             <widget class="QPushButton" name="add_btn_3_1">
              <property name="text">
               <string>Добавить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup3_1</string>
              </attribute>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="del_btn_3_1">
              <property name="text">
               <string>Удалить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup3_1</string>
              </attribute>
             </widget>
            </item>
           </layout>
          </widget>
         </widget>
         <widget class="QWidget" name="tab3_2">
          <attribute name="title">
           <string>Виды мероприятий</string>
          </attribute>
          <widget class="QTableView" name="tableView_2">
           <property name="geometry">
            <rect>
             <x>0</x>
             <y>0</y>
             <width>681</width>
             <height>251</height>
            </rect>
           </property>
          </widget>
          <widget class="QWidget" name="horizontalLayoutWidget_4">
           <property name="geometry">
            <rect>
             <x>20</x>
             <y>290</y>
             <width>295</width>
             <height>80</height>
            </rect>
           </property>
           <layout class="QHBoxLayout" name="horizontalLayout_5">
            <item>
             <widget class="QPushButton" name="add_btn_3_2">
              <property name="text">
               <string>Добавить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup3_2</string>
              </attribute>
             </widget>
            </item>
            <item>
             <widget class="QPushButton" name="del_btn_3_2">
              <property name="text">
               <string>Удалить</string>
              </property>
              <attribute name="buttonGroup">
               <string notr="true">buttonGroup3_2</string>
              </attribute>
             </widget>
            </item>
           </layout>
          </widget>
         </widget>
        </widget>
       </widget>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QPushButton" name="reload_btn">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>0</y>
      <width>151</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>Перезагрузить данные</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
 <buttongroups>
  <buttongroup name="buttonGroup2_1"/>
  <buttongroup name="buttonGroup2_2"/>
  <buttongroup name="buttonGroup3_1"/>
  <buttongroup name="buttonGroup3_2"/>
 </buttongroups>
</ui>
"""
add_ui_templ = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>501</width>
    <height>249</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Добавить мероприятие</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QDateEdit" name="dateEdit">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>90</y>
      <width>110</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>190</x>
      <y>90</y>
      <width>91</width>
      <height>22</height>
     </rect>
    </property>
   </widget>
   <widget class="QPlainTextEdit" name="plainTextEdit">
    <property name="geometry">
     <rect>
      <x>323</x>
      <y>80</y>
      <width>131</width>
      <height>87</height>
     </rect>
    </property>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>30</y>
      <width>431</width>
      <height>41</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Время:</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Вид мероприятия:</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="text">
        <string>Описание мероприятия:</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>60</x>
      <y>150</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <item>
      <widget class="QPushButton" name="add_btn">
       <property name="text">
        <string>Добавить</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="cancel_btn">
       <property name="text">
        <string>Отмена</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>501</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ui_templ)
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

        self.combo_2_6.currentTextChanged.connect(self.load_desktop)
        self.combo_3_6.currentTextChanged.connect(self.load_desktop)

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
                self.order_2.setHorizontalHeaderLabels(['id', 'event_id', 'room_id', 'date_start', 'date_end',
                                                        'description', 'status_id', 'work_type_id'])
                self.order_3.setColumnCount(len(result[0]))
                self.order_3.setHorizontalHeaderLabels(['id', 'event_id', 'room_id', 'date_start', 'date_end',
                                                        'description', 'status_id', 'work_type_id'])
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
                                  (self.combo_2_6.currentText(), )).fetchone()[0]
                id3 = cur.execute("""SELECT id FROM work_type WHERE name = ?""",
                                  (self.combo_3_6.currentText(), )).fetchone()[0]

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
            not_del = conn.execute("""SELECT id FROM work_order WHERE work_type_id = ?""", (data[0], )).fetchall()
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
                cur.execute("""DELETE FROM work_type WHERE id = ?""", (data[0], ))
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

    def open_second_form(self):
        self.second_form = SecondForm(self)
        self.second_form.show()


class SecondForm(QMainWindow):
    def __init__(self, main):
        self.main = main
        super().__init__()
        f1 = io.StringIO(add_ui_templ)
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

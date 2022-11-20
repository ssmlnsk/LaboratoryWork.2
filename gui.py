import mysql

from facade import Facade
import random

from PyQt5.QtGui import QFont
from PyQt5 import QtWidgets
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene, QListWidgetItem
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QDialog

import sys

import logging

from PyQt5.QtWidgets import QMessageBox

logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self):
        """
        Отвечает за подключением к кнопкам, объявление переменных, заполнение таблиц,
        получение списка страниц StackedWidget
        """
        super().__init__()
        self.facade = Facade()
        self.ui = uic.loadUi("main.ui", self)

        self.page = self.ui.stackedWidget_main
        self.page_id = [0]  # индексы доступных страничек после авторизации для сотрудника
        self.now_page = 0

        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.ui.btn_next.clicked.connect(self.next_page)
        self.ui.btn_back.clicked.connect(self.back_page)
        self.ui.btn_exit.clicked.connect(self.exit)

        self.ui.btn_add_employee.clicked.connect(self.new_employee)
        self.ui.btn_delete_employee.clicked.connect(self.delete_employee)
        self.ui.btn_save_employees.clicked.connect(self.save_employee)

        self.ui.btn_new_workwear.clicked.connect(self.new_workwear)
        self.ui.btn_delete_workwear.clicked.connect(self.delete_workwear)
        self.ui.btn_save_workwear.clicked.connect(self.save_workwear)

        self.ui.btn_new_type.clicked.connect(self.new_type)
        self.ui.btn_delete_type.clicked.connect(self.delete_type)
        self.ui.btn_save_type.clicked.connect(self.save_types_workwear)

        self.ui.btn_new_supplier.clicked.connect(self.new_supplier)
        self.ui.btn_delete_supplier.clicked.connect(self.delete_supplier)
        self.ui.btn_save_supplier.clicked.connect(self.save_supplier)

        self.ui.btn_new_entrance.clicked.connect(self.new_entrance)
        self.ui.btn_delete_entrance.clicked.connect(self.delete_entrance)
        self.ui.btn_save_entrance.clicked.connect(self.save_entrance)

        self.build_combobox_employee()
        self.build_combobox_workwear()
        self.build_combobox_supplier()

        self.ui.btn_new_issuance.clicked.connect(self.create_new_issuance)
        self.ui.btn_save_list_issuance.clicked.connect(self.save_issuance)
        self.ui.btn_save_issuance.clicked.connect(self.save_issuance_2)
        self.ui.btn_delete_issuance.clicked.connect(self.delete_issuance)

        self.ui.btn_plus.clicked.connect(self.add_workwear_to_issuance)

        self.ui.btn_all_employees.clicked.connect(self.oped_all_employees)

        self.updateTableEmployees()
        self.updateTableWorkwear()
        self.updateTableTypes()
        self.updateTableEntrance()
        self.updateTableIssuance()
        self.updateTableSuppliers()

    def exit(self):
        """
        Отвечает за выход из программы
        :param block: блокировка
        :return:
        """
        self.now_page = 0
        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.hide()
        self.open_auth()

    def next_page(self):
        """
        Отвечает за переход к следующей странице
        :return:
        """
        if self.now_page != len(self.page_id)-1:
            self.now_page += 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def back_page(self):
        """
        Отвечает за переход к предыдущей странице
        :return:
        """
        if self.now_page != 0:
            self.now_page -= 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def oped_all_employees(self):
        self.updateTableEmployees()
        self.page.setCurrentIndex(1)

    def updateTableEmployees(self):
        """
        Отвечает за обновление таблицы посетителей.
        :return:
        """
        self.table_employees.clear()
        rec = self.facade.read_employees()
        self.ui.table_employees.setColumnCount(6)
        self.ui.table_employees.setRowCount(len(rec))
        self.ui.table_employees.setHorizontalHeaderLabels(['Код сотрудника', 'Фамилия', 'Имя', 'Отчество', 'Профессия', 'Должность'])

        for i, employee in enumerate(rec):
            for x, field in enumerate(employee):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_employees.setItem(i, x, item)

    def updateTableEntrance(self):
        """
        Отвечает за обновление таблицы картин.
        :return:
        """
        self.table_entrance.clear()
        rec = self.facade.read_entrance()
        self.ui.table_entrance.setColumnCount(4)
        self.ui.table_entrance.setRowCount(len(rec))
        self.ui.table_entrance.setHorizontalHeaderLabels(['Номер документа', 'Дата поставки', 'Поставщик', 'Количество'])

        for i, entranse in enumerate(rec):
            for x, field in enumerate(entranse):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_entrance.setItem(i, x, item)

    def updateTableIssuance(self):
        """
        Отвечает за обновление таблицы художников.
        :return:
        """
        self.table_issuance.clear()
        rec = self.facade.read_issuance()
        self.ui.table_issuance.setColumnCount(5)
        self.ui.table_issuance.setRowCount(len(rec))
        self.ui.table_issuance.setHorizontalHeaderLabels(['ID', 'Дата выдачи', 'Сотрудник', 'Срок использования', 'Спецодежда'])

        for i, issuance in enumerate(rec):
            for x, field in enumerate(issuance):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_issuance.setItem(i, x, item)

    def updateTableTypes(self):
        """
        Отвечает за обновление таблицы выставок.
        :return:
        """
        self.table_types_workwear.clear()
        rec = self.facade.read_types_of_workwear()
        self.ui.table_types_workwear.setColumnCount(2)
        self.ui.table_types_workwear.setRowCount(len(rec))
        self.ui.table_types_workwear.setHorizontalHeaderLabels(['Код типа', 'Название'])

        for i, type in enumerate(rec):
            for x, field in enumerate(type):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_types_workwear.setItem(i, x, item)

    def updateTableWorkwear(self):
        """
        Отвечает за обновление таблицы выставленных картин.
        :return:
        """
        self.table_workwear.clear()
        rec = self.facade.read_workwear()
        self.ui.table_workwear.setColumnCount(5)
        self.ui.table_workwear.setRowCount(len(rec))
        self.ui.table_workwear.setHorizontalHeaderLabels(['Код спецодежды', 'Наименование', 'Тип', 'Стоимость', 'Данные о поставке'])

        for i, workwear in enumerate(rec):
            for x, field in enumerate(workwear):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_workwear.setItem(i, x, item)

    def updateTableSuppliers(self):
        """
        Отвечает за обновление таблицы выставленных картин.
        :return:
        """
        self.table_suppliers.clear()
        rec = self.facade.read_supplier()
        self.ui.table_suppliers.setColumnCount(2)
        self.ui.table_suppliers.setRowCount(len(rec))
        self.ui.table_suppliers.setHorizontalHeaderLabels(['Код поставщика', 'Наименование'])

        for i, supplier in enumerate(rec):
            for x, field in enumerate(supplier):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_suppliers.setItem(i, x, item)

    def new_workwear(self):
        """
        Создает и показывает диалоговое окно добавления нового художника.
        :return:
        """
        dialog_client = DialogNewWorkwear(self)
        dialog_client.setWindowTitle("Добавление нового художника")
        dialog_client.show()
        dialog_client.exec_()

    def delete_workwear(self):
        """
        Отвечает за удаление выбранной картины, выставленной на выставке.
        :return:
        """
        SelectedRow = self.table_workwear.currentRow()
        rowcount = self.table_workwear.rowCount()
        colcount = self.table_workwear.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_workwear.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_workwear.model().index(-1, -1)
            self.table_workwear.setCurrentIndex(ix)

    def new_type(self):
        type = self.ui.edit_type.text()
        self.facade.insert_type_of_workwear(type)
        self.updateTableTypes()

    def delete_type(self):
        """
        Отвечает за удаление выбранной картины.
        :return:
        """
        SelectedRow = self.table_types_workwear.currentRow()
        rowcount = self.table_types_workwear.rowCount()
        colcount = self.table_types_workwear.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_types_workwear.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_types_workwear.model().index(-1, -1)
            self.table_types_workwear.setCurrentIndex(ix)

    def new_entrance(self):
        date = self.ui.date_entrance.dateTime().toString('yyyy-MM-dd')
        supplier = self.facade.get_id_supplier(self.comboBox_supplier.currentText())
        quantity = self.ui.spinBox_quantity.value()
        self.facade.insert_entrance(date, supplier, quantity)
        self.updateTableEntrance()

    def delete_entrance(self):
        """
        Отвечает за удаление выбранной картины.
        :return:
        """
        SelectedRow = self.table_entrance.currentRow()
        rowcount = self.table_entrance.rowCount()
        colcount = self.table_entrance.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_entrance.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_entrance.model().index(-1, -1)
            self.table_entrance.setCurrentIndex(ix)

    def new_supplier(self):
        supplier = self.ui.edit_supplier_name.text()
        self.facade.insert_supplier(supplier)
        self.updateTableSuppliers()

    def delete_supplier(self):
        """
        Отвечает за удаление выбранной картины.
        :return:
        """
        SelectedRow = self.table_suppliers.currentRow()
        rowcount = self.table_suppliers.rowCount()
        colcount = self.table_suppliers.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_suppliers.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_suppliers.model().index(-1, -1)
            self.table_suppliers.setCurrentIndex(ix)

    def new_employee(self):
        """
        Создает и показывает диалоговое окно добавления нового художника.
        :return:
        """
        dialog_client = DialogNewEmployee(self)
        dialog_client.setWindowTitle("Добавление нового художника")
        dialog_client.show()
        dialog_client.exec_()

    def delete_employee(self):
        """
        Отвечает за удаление выбранного художника.
        :return:
        """
        SelectedRow = self.table_employees.currentRow()
        rowcount = self.table_employees.rowCount()
        colcount = self.table_employees.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_employees.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_employees.model().index(-1, -1)
            self.table_employees.setCurrentIndex(ix)

    def getFromTableWorkwear(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД
        :return: data
        """
        rows = self.table_workwear.rowCount()
        cols = self.table_workwear.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_workwear.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableEmployee(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД
        :return: data
        """
        rows = self.table_employees.rowCount()
        cols = self.table_employees.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_employees.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableSupplier(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД.
        :return: data
        """
        rows = self.table_suppliers.rowCount()
        cols = self.table_suppliers.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_suppliers.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableTypes(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД.
        :return: data
        """
        rows = self.table_types_workwear.rowCount()
        cols = self.table_types_workwear.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_types_workwear.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableEntrance(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД.
        :return: data
        """
        rows = self.table_entrance.rowCount()
        cols = self.table_entrance.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_entrance.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableIssuance(self):
        """
        Получение данных из таблицы, чтобы потом записать их в БД.
        :return: data
        """
        rows = self.table_issuance.rowCount()
        cols = self.table_issuance.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_issuance.item(row, col).text())
            data.append(tmp)
        return data

    def create_new_issuance(self):
        """
        Оформление нового билета и его показ в ListWidget.
        :return:
        """
        self.date_title = QListWidgetItem("Дата выдачи:")
        self.date = str(self.date_issuance.dateTime().toString('yyyy-MM-dd'))
        self.employee_title = QListWidgetItem("Сотрудник:")
        self.employee = QListWidgetItem(self.comboBox_employee.currentText())
        self.term_of_use_title = QListWidgetItem("Срок использования:")
        self.term_of_use = str(self.date_term.dateTime().toString('yyyy-MM-dd'))
        self.workwear_title = QListWidgetItem("Одежда к выдаче:")
        self.workwear = QListWidgetItem(self.comboBox_workwear.currentText())
        self.add_new_issuance.clear()

        self.add_new_issuance.addItem(self.date_title)
        self.add_new_issuance.addItem(self.date)
        self.add_new_issuance.addItem(self.employee_title)
        self.add_new_issuance.addItem(self.employee)
        self.add_new_issuance.addItem(self.term_of_use_title)
        self.add_new_issuance.addItem(self.term_of_use)
        self.add_new_issuance.addItem(self.workwear_title)
        self.add_new_issuance.addItem(self.workwear)

    def add_workwear_to_issuance(self):
        """
        Добавление услуги в заказ
        :return:
        """
        self.workwear = QListWidgetItem(self.comboBox_workwear.currentText())
        self.add_new_issuance.addItem(self.workwear)

    def delete_issuance(self):
        """
        Отвечает за удаление выбранной картины.
        :return:
        """
        SelectedRow = self.table_issuance.currentRow()
        rowcount = self.table_issuance.rowCount()
        colcount = self.table_issuance.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_issuance.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_issuance.model().index(-1, -1)
            self.table_issuance.setCurrentIndex(ix)

    def save_issuance(self):
        """
        Отвечает за сохранение заказа в базу данных
        :return:
        """
        ignore_workwear = [0, 1, 2, 3, 4, 5, 6]
        ignore_title = [1, 3, 5]
        count = self.add_new_issuance.count()
        list_workwear = [ind for ind in range(count) if ind not in ignore_workwear]
        list_issuance = [ind for ind in range(count) if ind in ignore_title]
        issuance = []
        workwear = []
        for i in list_workwear:
            name = self.add_new_issuance.item(i).text()
            id_workwear = self.facade.get_id_workwear(name)
            workwear.append(id_workwear)

        for j in list_issuance:
            if j == 3:
                fio = self.add_new_issuance.item(j).text().split(' ')
                id_employee = self.facade.get_id_employee(fio[0], fio[1], fio[2])
                issuance.append(id_employee)
            else:
                issuance.append(self.add_new_issuance.item(j).text())

        for a in workwear:
            self.facade.insert_issuance(issuance[0], issuance[1], issuance[2], a)
        self.updateTableIssuance()

    def save_issuance_2(self):
        """
        Отвечает за сохранение данных о картинах в базу данных.
        Обновление таблицы в интерфейсе.
        :return:
        """
        data = self.getFromTableIssuance()
        for string in data:
            if string[1] != '':
                self.facade.update_issuance(int(string[0]), string[1], string[2], string[3], string[4])
            else:
                self.facade.delete_issuance(int(string[0]))
        self.updateTableIssuance()

    def save_employee(self):
        """
        Отвечает за сохранение данных о картинах в базу данных.
        Обновление таблицы в интерфейсе.
        :return:
        """
        data = self.getFromTableEmployee()
        for string in data:
            if string[1] != '':
                self.facade.update_employee(int(string[0]), string[1], string[2], string[3], string[4], string[5])
            else:
                self.facade.delete_employee(int(string[0]))
        self.updateTableEmployees()
        self.build_combobox_employee()

    def save_workwear(self):
        """
        Отвечает за сохранение данных о художниках в базу данных.
        Обновление таблицы в интерфейсе.
        :return:
        """
        data = self.getFromTableWorkwear()
        for string in data:
            if string[1] != '':
                self.facade.update_workwear(int(string[0]), string[1], string[2], string[3], string[4])
            else:
                self.facade.delete_workwear(int(string[0]))

        self.updateTableWorkwear()

    def save_types_workwear(self):
        """
        Отвечает за сохранение данных о выставленных картинах в базу данных.
        Обновление таблицы в интерфейсе.
        :return:
        """
        data = self.getFromTableTypes()
        for string in data:
            if string[1] != '':
                self.facade.update_type_of_workwear(string[0], string[1])
            else:
                self.facade.delete_type_of_workwear(string[0])
        self.updateTableTypes()

    def save_supplier(self):
        """
        Отвечает за сохранение данных о выставленных картинах в базу данных.
        Обновление таблицы в интерфейсе.
        :return:
        """
        data = self.getFromTableSupplier()
        for string in data:
            if string[1] != '':
                self.facade.update_supplier(string[0], string[1])
            else:
                self.facade.delete_supplier(string[0])
        self.updateTableSuppliers()

    def save_entrance(self):
        """
        Отвечает за сохранение данных о выставленных картинах в базу данных.
        Обновление таблицы в интерфейсе.
        :return:
        """
        data = self.getFromTableEntrance()
        for string in data:
            if string[1] != '':
                self.facade.update_entrance(string[0], string[1], string[2], string[3])
            else:
                self.facade.delete_entrance(string[0])
        self.updateTableEntrance()

    def build_combobox_employee(self):
        """
        Добавление списка посетителей в ComboBox.
        :return:
        """
        employee = self.facade.get_employees()
        self.comboBox_employee.clear()
        if self.comboBox_employee is not None:
            self.comboBox_employee.addItems(employee)
        logging.log(logging.INFO, 'ComboBox "Посетители" обновлён')

    def build_combobox_workwear(self):
        """
        Добавление списка выставок в ComboBox.
        :return:
        """
        workwear = self.facade.get_workwear()
        self.comboBox_workwear.clear()
        if self.comboBox_workwear is not None:
            self.comboBox_workwear.addItems(workwear)
        logging.log(logging.INFO, 'ComboBox "Выставки" обновлён')

    def build_combobox_supplier(self):
        """
        Добавление списка картин для выставления на выставку в ComboBox.
        :return:
        """
        supplier = self.facade.get_supplier()
        self.comboBox_supplier.clear()
        if self.comboBox_supplier is not None:
            self.comboBox_supplier.addItems(supplier)
        logging.log(logging.INFO, 'ComboBox "Категории" обновлён')

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается при успешном создании кода.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Штрих-код")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()

    def next_page(self):
        """
        Отвечает за переход к следующей странице
        :return:
        """
        if self.now_page != len(self.page_id)-1:
            self.now_page += 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def back_page(self):
        """
        Отвечает за переход к предыдущей странице
        :return:
        """
        if self.now_page != 0:
            self.now_page -= 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def open_auth(self):
        """
        Создает и показывает диалоговое окно авторизации.
        Вызывается в __init__ и в функции exit
        :return:
        """
        dialog = DialogAuth(self)
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()


class DialogAuth(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключением к кнопкам, объявление переменных, создание сцены для «graphicsView»
        """
        super(DialogAuth, self).__init__(parent)
        self.ui = uic.loadUi("auth.ui", self)
        self.facade = Facade()

        self.scene = QGraphicsScene(0, 0, 300, 80)
        self.ui.draw_captcha.setScene(self.scene)
        self.ui.btn_enter.clicked.connect(self.enter)
        self.ui.btn_new_captcha.clicked.connect(self.captcha_generation)
        self.ui.btn_hide_password.clicked.connect(self.vis_pas)
        self.visible_captcha(False)

        self.count_try_entry = 0
        self.now_captcha = None
        self.next_try = 0
        self.vis_p = False

    def vis_pas(self):
        """
        Вызывается при нажатии на кнопку «btn_hide_password».
        Скрывает и показывает пароль (в соответствии с переменной self.vis_p)
        """
        ed = self.ui.edit_password
        if self.vis_p:
            self.vis_p = False
            ed.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.vis_p = True
            ed.setEchoMode(QtWidgets.QLineEdit.Normal)

    def visible_captcha(self, visible=True):
        """
        Вызывается в __init__ (с параметром False) и при второй неуспешной попытки входа
        (неправильный ввод пароля или логина) с параметом True.
        :param visible:
        При False скрывает поле ввода, кнопку обновления и сцену для отрисовки капчи
        При True - показывает поле ввода, кнопку обновления и сцену для отрисовки капчи
        """
        self.ui.draw_captcha.setVisible(visible)
        self.ui.edit_captcha.setVisible(visible)
        self.ui.label_4.setVisible(visible)
        self.ui.btn_new_captcha.setVisible(visible)

    def captcha_generation(self):
        """
        Вызывается при второй неуспешной попытке входа и при нажатии на кнопку «btn_new_captcha».
        Выводит капчу в «graphicsView» и возвращает значение капчи в переменной self.now_captcha
        """
        self.scene.clear()
        syms = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        count_syms = 3
        now_syms = ['']*count_syms
        x, y = 30, 20

        self.scene.addLine(0, random.randint(20, 45), 200, random.randint(30, 60))

        for i in range(count_syms):
            now_syms[i] = syms[random.randint(0, 35)]
            x+=20
            text = self.scene.addText(f"{now_syms[i]}")
            text.setFont(QFont("MS Shell Dlg 2", 15))
            text.moveBy(x, y+random.randint(-10, 20))
        self.now_captcha = ''.join(now_syms)

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается при неверном вводе пользователем логина, пароля, капчи.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()

    def enter(self):
        """
        Вызывается при нажатии на кнопку btn_enter.
        Обрабатывает все случаи ввода данных (капчи, логина, пароля) и считает неуспешные попытки входа.
        Проверяет есть ли у пользователя блокировка и до скольки она длиться.
        При успешном входе передает в фасад время и логин успешного входа (для записи в бд),
        записывает индексы доступных страничек «Stacked Widget»
        (у разных сотрудников могут быть разные странички)
        """
        auth_log = self.ui.edit_login.text()
        auth_pas = self.ui.edit_password.text()

        if auth_log == '' or auth_pas == '':
            logging.log(logging.INFO, 'Ошибка. Заполните все поля!')
            self.mes_box('Заполните все поля!')

        elif self.now_captcha is not None and self.ui.edit_captcha.text() == '':    # если капча существует и она не пустая
            logging.log(logging.INFO, 'Ошибка. Введите капчу!')
            self.mes_box('Введите капчу!')
        else:
            password = "admin"
            name = "admin"

            if self.now_captcha is not None and self.now_captcha != self.ui.edit_captcha.text():
                logging.log(logging.INFO, 'Ошибка. Неправильно введена капча.')
                self.mes_box('Неправильно введена капча.')
            elif password != auth_pas:
                logging.log(logging.INFO, 'Ошибка. Неправильно введены данные.')
                self.mes_box('Неправильно введены данные.')
            elif password == auth_pas:
                logging.log(logging.INFO, 'Вход выполнен')

                if name == 'admin1':
                    self.parent().page_id = [0, 1, 2, 3, 4, 5, 6]
                else:   # Администратор
                    self.parent().page_id = [0, 1, 2, 3, 4, 5, 6]
                self.parent().show()
                self.close()


class DialogNewWorkwear(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключение к кнопке "Добавить"
        """
        super(DialogNewWorkwear, self).__init__(parent)
        self.ui = uic.loadUi("new_workwear.ui", self)
        self.facade = Facade()

        self.build_combobox_type()
        self.build_combobox_entrance()

        self.ui.btn_add_workwear.clicked.connect(self.add)

    def add(self):
        """
        Отвечает за добавление посетителя в базу данных
        :return:
        """
        self.name = self.ui.edit_name.text()
        self.type = self.facade.get_id_type(self.comboBox_type.currentText())
        self.cost = self.ui.edit_cost.text()
        self.entrance = self.comboBox_entrance.currentText()

        if self.name != '' and self.type != '' and self.cost != '' and self.entrance != '':
            self.facade.insert_workwear(self.name, self.type, self.cost, self.entrance)
            # self.parent().updateTableWorkwear()
        else:
            self.mes_box('Заполните все поля!')

    def build_combobox_type(self):
        """
        Добавление списка выставок в ComboBox.
        :return:
        """
        type = self.facade.get_type()
        self.comboBox_type.clear()
        if self.comboBox_type is not None:
            self.comboBox_type.addItems(type)
        logging.log(logging.INFO, 'ComboBox "Выставки" обновлён')

    def build_combobox_entrance(self):
        """
        Добавление списка выставок в ComboBox.
        :return:
        """
        entrance = self.facade.get_entrance()
        self.comboBox_entrance.clear()
        if self.comboBox_entrance is not None:
            self.comboBox_entrance.addItems(entrance)
        logging.log(logging.INFO, 'ComboBox "Выставки" обновлён')

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается, если какое-либо поле не заполнено.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()


class DialogNewEmployee(QDialog):
    def __init__(self, parent=None):
        """
        Отвечает за подключение к кнопке "Добавить"
        """
        super(DialogNewEmployee, self).__init__(parent)
        self.ui = uic.loadUi("new_employee.ui", self)
        self.facade = Facade()
        self.ui.btn_add_employee.clicked.connect(self.add)

    def add(self):
        """
        Отвечает за добавление художника в базу данных.
        :return:
        """
        self.surname = self.ui.edit_surname.text()
        self.name = self.ui.edit_name.text()
        self.lastName = self.ui.edit_lastName.text()
        self.profession = self.ui.edit_profession.text()
        self.post = self.ui.edit_post.text()

        if self.surname != '' and self.name != '' and self.lastName != '' and self.profession != '' and self.post != '':
            self.facade.insert_employee(self.surname, self.name, self.lastName, self.profession, self.post)
            #self.parent().updateTableEmployees()
        else:
            self.mes_box('Заполните все поля!')

    def mes_box(self, text):
        """
        Открывает messagebox с переданным текстом.
        Вызывается, если какое-либо поле не заполнено.
        :param text: текст для вывода в messagebox
        """
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()


class Builder:
    """
    Паттерн строитель.
    Это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
    """
    def __init__(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()
        self.auth()

    def auth(self):
        self.window.open_auth()
        self.qapp.exec()


if __name__ == '__main__':
    B = Builder()

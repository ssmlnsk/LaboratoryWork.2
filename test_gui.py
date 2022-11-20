import sys
from unittest import TestCase

from PyQt5 import QtCore
from PyQt5.QtCore import QDate, QItemSelectionModel
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from database import Database
from facade import Facade
from gui import MainWindow, DialogNewEmployee, DialogNewWorkwear


class TestPush(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        self.facade = Facade()
        self.db = Database()
        self.window = MainWindow()
        self.emp = DialogNewEmployee()
        self.ww = DialogNewWorkwear()

    def test_push_employee(self):
        btn_add = self.emp.ui.btn_add_employee

        self.emp.ui.edit_surname.setText("test_test")
        self.emp.ui.edit_name.setText("test_test")
        self.emp.ui.edit_lastName.setText("test_test")
        self.emp.ui.edit_profession.setText("test_test")
        self.emp.ui.edit_post.setText("test_test")

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)
        self.db.delete_employee()

    def test_push_workwear(self):
        btn_add = self.ww.ui.btn_add_workwear

        self.ww.ui.edit_name.setText("test_test")
        self.ww.ui.edit_cost.setValue(1200)

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_push_entrance(self):
        btn_add = self.window.ui.btn_new_entrance

        self.window.ui.date_entrance.setDate(QDate.fromString("2022-01-01"))
        self.window.ui.spinBox_quantity.setValue(20)

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_push_supplier(self):
        btn_add = self.window.ui.btn_new_supplier

        self.ww.ui.edit_supplier_name.setText("test_supplier")

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_push_type(self):
        btn_add = self.window.ui.btn_new_type

        self.ww.ui.edit_type.setText("test_type")

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_push_issuance(self):
        btn_add = self.window.ui.btn_new_issuance

        self.window.ui.date_issuance.setDate(QDate.fromString("2022-01-01"))
        self.window.ui.date_term.setDate(QDate.fromString("2022-02-01"))

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

        QTest.mouseClick(self.window.ui.btn_plus, QtCore.Qt.MouseButton.LeftButton)


class TestDeleteAndSave(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        self.facade = Facade()
        self.db = Database()
        self.window = MainWindow()

    def test_delete_employee(self):
        self.db.insert_employee("surname", "name", "lastName", "profession", "post")
        QTest.mouseClick(self.window.ui.btn_save_employees, QtCore.Qt.MouseButton.LeftButton)

        rowcount = self.window.table_employees.rowCount()
        self.window.table_employees.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.btn_delete_employee
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.btn_save_employees, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_workwear(self):
        self.db.insert_workwear("name", 1, 1000, 462266)
        QTest.mouseClick(self.window.ui.btn_save_workwear, QtCore.Qt.MouseButton.LeftButton)

        rowcount = self.window.table_workwear.rowCount()
        self.window.table_workwear.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.btn_delete_workwear
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.btn_save_workwear, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_type(self):
        self.db.insert_type_of_workwear("type")
        QTest.mouseClick(self.window.ui.btn_save_type, QtCore.Qt.MouseButton.LeftButton)

        rowcount = self.window.table_types_workwear.rowCount()
        self.window.table_types_workwear.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.btn_delete_type
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.btn_save_type, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_entrance(self):
        self.db.insert_entrance("2020-10-10", 1, 100)
        QTest.mouseClick(self.window.ui.btn_save_entrance, QtCore.Qt.MouseButton.LeftButton)

        rowcount = self.window.table_entrance.rowCount()
        self.window.table_entrance.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.btn_delete_entrance
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.btn_save_entrance, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_issuance(self):
        self.db.insert_issuance("2020-11-11", 1, "2020-11-12", 1)
        QTest.mouseClick(self.window.ui.btn_save_issuance, QtCore.Qt.MouseButton.LeftButton)

        rowcount = self.window.table_issuance.rowCount()
        self.window.table_issuance.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.btn_delete_issuance
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.btn_save_issuance, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_supplier(self):
        self.db.insert_supplier("supplier")
        QTest.mouseClick(self.window.ui.btn_save_supplier, QtCore.Qt.MouseButton.LeftButton)

        rowcount = self.window.table_suppliers.rowCount()
        self.window.table_suppliers.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.btn_delete_supplier
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.btn_save_supplier, QtCore.Qt.MouseButton.LeftButton)

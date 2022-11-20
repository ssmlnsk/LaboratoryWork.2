# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_workwear.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(617, 572)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(12, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Andale Mono")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/logo_mini.png"))
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setStyleSheet("font: 11pt \"Andale Mono\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setStyleSheet("background-color: rgb(203,241,245);\n"
"font: 9pt \"Andale Mono\";")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.edit_name = QtWidgets.QLineEdit(Dialog)
        self.edit_name.setObjectName("edit_name")
        self.horizontalLayout_9.addWidget(self.edit_name)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setStyleSheet("background-color: rgb(203,241,245);\n"
"font: 9pt \"Andale Mono\";")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.comboBox_type = QtWidgets.QComboBox(Dialog)
        self.comboBox_type.setObjectName("comboBox_type")
        self.horizontalLayout_8.addWidget(self.comboBox_type)
        self.horizontalLayout_8.setStretch(1, 100)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("background-color: rgb(203,241,245);\n"
"font: 9pt \"Andale Mono\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.edit_cost = QtWidgets.QSpinBox(Dialog)
        self.edit_cost.setReadOnly(False)
        self.edit_cost.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.edit_cost.setAccelerated(False)
        self.edit_cost.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.edit_cost.setKeyboardTracking(True)
        self.edit_cost.setProperty("showGroupSeparator", False)
        self.edit_cost.setMinimum(0)
        self.edit_cost.setMaximum(999999)
        self.edit_cost.setSingleStep(1)
        self.edit_cost.setObjectName("edit_cost")
        self.horizontalLayout_4.addWidget(self.edit_cost)
        self.horizontalLayout_4.setStretch(1, 100)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("background-color: rgb(203,241,245);\n"
"font: 9pt \"Andale Mono\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_20.addWidget(self.label_3)
        self.comboBox_entrance = QtWidgets.QComboBox(Dialog)
        self.comboBox_entrance.setObjectName("comboBox_entrance")
        self.horizontalLayout_20.addWidget(self.comboBox_entrance)
        self.horizontalLayout_20.setStretch(1, 100)
        self.verticalLayout_5.addLayout(self.horizontalLayout_20)
        self.verticalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_add_workwear = QtWidgets.QPushButton(Dialog)
        self.btn_add_workwear.setStyleSheet("background-color: rgb(113,201,206);\n"
"font: 9pt \"Andale Mono\";")
        self.btn_add_workwear.setObjectName("btn_add_workwear")
        self.horizontalLayout_3.addWidget(self.btn_add_workwear)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Учет и выдача спецодежды на предприятии"))
        self.label_2.setText(_translate("Dialog", "Добавить спецодежду"))
        self.label_6.setText(_translate("Dialog", "Наименование:"))
        self.label_8.setText(_translate("Dialog", "Тип:"))
        self.label_5.setText(_translate("Dialog", "Стоимость:"))
        self.label_3.setText(_translate("Dialog", "Поставка:"))
        self.btn_add_workwear.setText(_translate("Dialog", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

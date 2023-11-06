import sys
import sqlite3
from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon, QFont, QFontDatabase
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter
from PyQt5 import uic


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        uic.loadUi('design.ui', self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle('Конвертер валют')
        self.ui.input_amount.setPlaceholderText('Введите сумму')
        self.ui.output_amount.setPlaceholderText('Результат')
        self.ui.input_text_currency.setPlaceholderText('Введите аббревиатуру валюты')
        self.ui.output_text_currency.setPlaceholderText('Введите аббревиатуру валюты')
        self.ui.pushButton.clicked.connect(self.converter)
        font_id = QFontDatabase.addApplicationFont('Unbounded-VariableFont_wght.ttf')
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family, 18)
        custom_font_1 = QFont(font_family, 8)
        custom_font_2 = QFont(font_family, 10)
        self.ui.tabWidget.setFont(custom_font)
        self.ui.label_2.setFont(custom_font_1)
        self.ui.label_3.setFont(custom_font_1)
        self.ui.label_4.setFont(custom_font_1)
        self.ui.label_5.setFont(custom_font_1)
        self.ui.input_currency.setFont(custom_font_1)
        self.ui.input_text_currency.setFont(custom_font_1)
        self.ui.output_currency.setFont(custom_font_1)
        self.ui.output_text_currency.setFont(custom_font_1)
        self.ui.input_amount.setFont(custom_font_2)
        self.ui.output_amount.setFont(custom_font_2)
        self.ui.pushButton.setFont(custom_font_2)
        self.ui.label_8.setFont(custom_font)

    def converter(self):
        c = CurrencyConverter()
        input_currency = 'o'
        output_currency = 'o'
        f = CurrencyConverter(decimal=True)
        currs = list(f.currencies)
        self.ui.output_amount.setText('')

        if self.ui.input_currency.currentText() != 'Найдите валюту в списке' and self.ui.input_text_currency.toPlainText() == '':
            input_currency = self.ui.input_currency.currentText()[0:3]
        elif self.ui.input_currency.currentText() == 'Найдите валюту в списке' and self.ui.input_text_currency.toPlainText() != '':
            if self.ui.input_text_currency.toPlainText().upper() in c.currencies:
                input_currency = self.ui.input_text_currency.toPlainText()
            else:
                self.ui.input_text_currency.setText('')
                self.statusBar().showMessage('Неправильный формат ввода аббревиатуры, попробуйте снова')
        elif self.ui.input_currency.currentText() == 'Найдите валюту в списке' and self.ui.input_text_currency.toPlainText() == '':
            self.statusBar().showMessage('Выберите валюту в списке или введите аббревиатуру валюты')
        else:
            self.statusBar().showMessage('Выберите валюту в списке ИЛИ введите аббревиатуру валюты')

        if self.ui.output_currency.currentText() != 'Найдите валюту в списке' and self.ui.output_text_currency.toPlainText() == '':
            output_currency = self.ui.output_currency.currentText()[0:3]
        elif self.ui.output_currency.currentText() == 'Найдите валюту в списке' and self.ui.output_text_currency.toPlainText() != '':
            if self.ui.output_text_currency.toPlainText().upper() in currs:
                output_currency = self.ui.output_text_currency.toPlainText()
            else:
                self.statusBar().showMessage('Неправильный формат ввода аббревиатуры для конвертации, попробуйте снова')
        elif self.ui.output_currency.currentText() == 'Найдите валюту в списке' and self.ui.output_text_currency.toPlainText() == '':
            self.statusBar().showMessage('Выберите валюту в списке или введите аббревиатуру валюты')
        else:
            self.statusBar().showMessage('Выберите валюту в списке ИЛИ введите аббревиатуру валюты')

        if input_currency != 'o' and output_currency != 'o':
            input_amount = int(self.ui.input_amount.text())
            output_amount = round(
                c.convert(input_amount, '%s' % (input_currency.upper()), '%s' % (output_currency.upper())), 2)
            if '.' in str(output_amount) and str(output_amount)[str(output_amount).find('.') + 1] == '0':
                self.ui.output_amount.setText(str(output_amount)[:-2])
            else:
                self.ui.output_amount.setText(str(output_amount))

            res = f'{input_currency}({int(self.ui.input_amount.text())}) = {output_currency}({output_amount})'
            self.ui.history_list.addItem(res)


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
# pyuic5.exe design.ui -o ui.py

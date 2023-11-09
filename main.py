import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont, QFontDatabase
from ui import Ui_MainWindow
from currency_converter import CurrencyConverter
import re


class CurrencyConv(QtWidgets.QMainWindow):
    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        self.exp = ''

    # подключение дизайна из файла ui.py
    def init_UI(self):
        a = 'logo.ico'
        self.setWindowIcon(QIcon(a))
        self.setWindowTitle('Конвертер валют')
        self.ui.input_amount.setPlaceholderText('Введите сумму')
        self.ui.output_amount.setPlaceholderText('Результат')
        self.ui.input_text_currency.setPlaceholderText('Введите аббревиатуру валюты')
        self.ui.output_text_currency.setPlaceholderText('Введите аббревиатуру валюты')
        self.ui.pushButton.clicked.connect(self.converter)
        # font_id = QFontDatabase.addApplicationFont('Unbounded-VariableFont_wght.ttf')

        # связка кнопок с функциями
        lst_calc_btns = [self.ui.btn_0, self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4, self.ui.btn_5,
                         self.ui.btn_6,
                         self.ui.btn_7, self.ui.btn_8, self.ui.btn_9, self.ui.btn_baepsae, self.ui.btn_c,
                         self.ui.btn_ce,
                         self.ui.btn_div, self.ui.btn_dot, self.ui.btn_eq, self.ui.btn_minus, self.ui.btn_mult,
                         self.ui.btn_plus,
                         self.ui.btn_plus_min]
        for i in lst_calc_btns:
            i.clicked.connect(self.press)
        self.ui.clear_1.clicked.connect(self.delete_1)
        self.ui.clear_2.clicked.connect(self.delete_2)

        """
        # добавление шрифта Unbounded regular
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        custom_font = QFont(font_family, 18)
        custom_font_1 = QFont(font_family, 8)
        custom_font_2 = QFont(font_family, 10)

        for i in lst_calc_btns + [self.ui.input_amount, self.ui.output_amount, self.ui.pushButton, self.ui.label_8,
                                  self.ui.label, self.ui.lineEdit, self.ui.clear_1, self.ui.clear_2]:
            i.setFont(custom_font_2)

        lst_2 = [self.ui.label_2, self.ui.label_3, self.ui.label_4, self.ui.label_5,
                 self.ui.input_currency, self.ui.input_text_currency, self.ui.output_currency,
                 self.ui.output_text_currency]

        for i in lst_2:
            i.setFont(custom_font_1)
        self.ui.label_8.setFont(custom_font)
        self.ui.tabWidget.setFont(custom_font)
        """

        # очищение истории конвертера валют
    def delete_1(self):
        self.ui.history_list.clear()

    # очищение истории калькулятора
    def delete_2(self):
        self.ui.history_list_2.clear()

    # конвертирование
    def converter(self):
        c = CurrencyConverter()
        input_currency = 'o'  # аббревиатура валюты исходного числа
        output_currency = 'o'  # аббревиатура валюты сконвертированного числа
        f = CurrencyConverter(decimal=True)
        currs = list(f.currencies)  # список доступных валют для перевода
        self.ui.output_amount.setText('')

        # проверка ввода исходной валюты
        if (self.ui.input_currency.currentText() != 'Найдите валюту в списке'
                and self.ui.input_text_currency.toPlainText() == ''):
            input_currency = self.ui.input_currency.currentText()[0:3]
        elif (self.ui.input_currency.currentText() == 'Найдите валюту в списке'
              and self.ui.input_text_currency.toPlainText() != ''):
            if self.ui.input_text_currency.toPlainText().upper() in c.currencies:
                input_currency = self.ui.input_text_currency.toPlainText()
            else:
                self.ui.input_text_currency.setText('')
                self.statusBar().showMessage('Неправильный формат ввода аббревиатуры, попробуйте снова')
        elif (self.ui.input_currency.currentText() == 'Найдите валюту в списке'
              and self.ui.input_text_currency.toPlainText() == ''):
            self.statusBar().showMessage('Выберите валюту в списке или введите аббревиатуру валюты')
        else:
            self.statusBar().showMessage('Выберите валюту в списке ИЛИ введите аббревиатуру валюты')

        # проверка ввода валюты для конвертации в неё
        if (self.ui.output_currency.currentText() != 'Найдите валюту в списке'
                and self.ui.output_text_currency.toPlainText() == ''):
            output_currency = self.ui.output_currency.currentText()[0:3]
        elif (self.ui.output_currency.currentText() == 'Найдите валюту в списке'
              and self.ui.output_text_currency.toPlainText() != ''):
            if self.ui.output_text_currency.toPlainText().upper() in currs:
                output_currency = self.ui.output_text_currency.toPlainText()
            else:
                self.statusBar().showMessage('Неправильный формат ввода аббревиатуры для конвертации, попробуйте снова')
        elif (self.ui.output_currency.currentText() == 'Найдите валюту в списке'
              and self.ui.output_text_currency.toPlainText() == ''):
            self.statusBar().showMessage('Выберите валюту в списке или введите аббревиатуру валюты')
        else:
            self.statusBar().showMessage('Выберите валюту в списке ИЛИ введите аббревиатуру валюты')

        input_amount = self.ui.input_amount.text()  # переменная введённой суммы для конвертации

        if input_currency != 'o' and output_currency != 'o':
            if any(i for i in self.ui.input_amount.text() if not i.isdigit()) or self.ui.input_amount.text().count(
                    '.') > 1:  # если в вводе содержатся не числа
                self.ui.input_text_currency.setText('')
                self.statusBar().showMessage('Неправильны формат ввода суммы')
            elif '.' in self.ui.input_amount.text():  # если число вещественное
                input_amount = float(self.ui.input_amount.text())
            elif input_amount == '':  # если сумма не введена
                self.statusBar().showMessage('Введите сумму')
            else:
                input_amount = int(self.ui.input_amount.text())
            output_amount = round(
                c.convert(input_amount, '%s' % (input_currency.upper()), '%s' % (output_currency.upper())),
                2)  # конвертирование введённой суммы
            if '.' in str(output_amount) and str(output_amount)[-1] == '0':  # если в ответе лишний ноль в дробной части
                self.ui.output_amount.setText(str(output_amount)[:-2])
                output_amount = int(str(output_amount)[:-2])
            else:
                self.ui.output_amount.setText(str(output_amount))

            # занесение выражения в историю
            res = f'{input_currency}({int(self.ui.input_amount.text())}) = {output_currency}({output_amount})'
            self.ui.history_list.addItem(res)

    # проверка на правильный формат ввода функции конвертации для калькулятора
    def evaluate_expression(self, expression):
        c = CurrencyConverter()
        try:
            result = eval(expression, {"__builtins__": None}, {"c": c})
            return result
        except Exception as e:
            return f"Ошибка: {str(e)}"

    # функция конвертации для калькулятора
    def process_currency_conversion(self, expression):
        c = CurrencyConverter()
        pattern = r'([a-zA-Z]+)\(([\d.]+), ([a-zA-Z]+)\)'  # разбитие функции на составляющие по шаблону
        matches = re.finditer(pattern, expression)

        # замена функции конвертации валют на результат и возвращения обновленной строки
        for match in matches:
            original = match.group(0)
            from_currency = match.group(1)
            amount = float(match.group(2))
            to_currency = match.group(3)

            converted_amount = c.convert(amount, from_currency.upper(), to_currency.upper())  # конвертация
            expression = expression.replace(original, str(converted_amount))

        return expression

    # обработка нажатия кнопок калькулятора или ввода выражения
    def press(self):
        f = CurrencyConverter(decimal=True)
        sender = self.sender()
        if sender.text() not in ('CE', 'C', '=', '<-'):  # если пользователь нажимает числа
            self.exp += sender.text()
            self.ui.label.setText(self.exp)
        else:
            if sender.text() == 'C':  # удаление полного выражения
                self.exp = ''
                self.ui.label.setText(self.exp)
                self.ui.lineEdit.setText(self.exp)
            elif sender.text() == '<-':  # удаление последнего символа
                if self.exp[-1].isdigit():
                    self.exp = self.exp[:-1]
                    self.ui.label.setText(self.exp)
            elif sender.text() == '=':  # вывод вычисление и вывод ответа на решение выражения
                if len(self.exp) == 0:
                    self.exp = self.ui.label.text()
                else:
                    self.ui.label.setText(str(self.exp.replace(" ", "") + '='))
                if '/0' not in self.exp:  # если пользователь делит на ноль
                    if any(char for char in self.exp.upper() if
                           char.isalpha()):  # если в строке ввода выражения есть буквы
                        if any(word in self.exp.upper() for word in
                               list(f.currencies)):  # если в строке ввода есть подстроки с аббревиатурой валюты
                            converted_expression = self.process_currency_conversion(
                                self.exp)  # применение функции конвертирования
                            result = self.evaluate_expression(converted_expression)
                            if any(char for char in str(result) if char.isalpha()):  # если конвертер выдал ошибку
                                self.ui.lineEdit.setText('Неправильный формат ввода')
                            else:
                                self.ui.history_list_2.addItem(
                                    self.exp + ' = ' + str(result))  # добавление выражения в историю калькулятора
                                self.ui.lineEdit.setText(str(result))
                        else:
                            self.ui.lineEdit.setText('Неправильный формат ввода')
                    else:
                        self.ui.lineEdit.setText(str(eval(self.exp.replace(" ", ""))))
                        # быстрый подсчёт выражения с помощью функции eval
                        ed_res = re.sub(r'([+\-*/])', r' \1 ', self.exp)
                        self.ui.history_list_2.addItem(ed_res + ' = ' + str(eval(self.exp)))
                        # добавление выражения в историю калькулятора
                else:
                    self.ui.lineEdit.setText('Деление на ноль невозможно')
            elif sender.text() == 'CE':  # удаление последнего числа и арифметической операции
                if self.exp.isdigit() or (self.exp[-1] in '/*+-' and self.exp[:-1].isdigit()):
                    # если введено одно число или одно число и операция
                    self.exp = ''
                    self.ui.label.setText(self.exp)
                    self.ui.lineEdit.setText(self.exp)
                else:
                    match = re.search(r'([-+*/])\s*(\d+)\s*$', self.exp)
                    if match:
                        self.exp = self.exp[:match.start()]
                        self.ui.label.setText(str(self.exp))


app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show()

sys.exit(app.exec())
# pyuic5.exe design.ui -o ui.py
# pyinstaller --onefile --windowed --icon=d:\Users\Sofia\Documents\script_files_all\currency_converter_pqt\logo.ico main.py
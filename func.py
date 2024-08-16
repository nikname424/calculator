from calc1 import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
import sys

class Calculator(QMainWindow):
    def __init__(self): #привязка к ui
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.connectButtons() #подключаем кнопки

    def connectButtons(self): #инициализация кнопок
        self.ui.pushButton_11.clicked.connect(lambda: self.add_number('0')) #0
        self.ui.pushButton_3.clicked.connect(lambda: self.add_number('1')) #1
        self.ui.pushButton_2.clicked.connect(lambda: self.add_number('2')) #2
        self.ui.pushButton_4.clicked.connect(lambda: self.add_number('3')) #3
        self.ui.pushButton_5.clicked.connect(lambda: self.add_number('4')) #4
        self.ui.pushButton_6.clicked.connect(lambda: self.add_number('5')) #5
        self.ui.pushButton_7.clicked.connect(lambda: self.add_number('6')) #6
        self.ui.pushButton_8.clicked.connect(lambda: self.add_number('7')) #7
        self.ui.pushButton_9.clicked.connect(lambda: self.add_number('8')) #8
        self.ui.pushButton_10.clicked.connect(lambda: self.add_number('9')) #9

        self.ui.pushButton_13.clicked.connect(lambda: self.add_number('+')) #+
        self.ui.pushButton_14.clicked.connect(lambda: self.add_number('-')) #-
        self.ui.pushButton_15.clicked.connect(lambda: self.add_number('*')) #*
        self.ui.pushButton_16.clicked.connect(lambda: self.add_number('/')) #/
        self.ui.pushButton_12.clicked.connect(lambda: self.set_result()) #=
        self.ui.pushButton_17.clicked.connect(lambda: self.ui.label.clear()) #delete
    
    def add_number(self, num): #добавляем знаки в строку.
        text = self.ui.label.text() #получение текста.  
        if num == '0' and text == '':
            pass
        else:
            text += num
            
        self.ui.label.setText(text)

    def set_result(self): #считаем результат.
        text = self.ui.label.text() #получаем текст.
        result = eval(text) #вычисляем значения.
        
        self.ui.label.setText(str(result))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec())
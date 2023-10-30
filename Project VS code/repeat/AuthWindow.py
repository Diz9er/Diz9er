from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import sys, random

class Auth(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.login = 'User'
        self.password = '1234'
        self.captcha_fail = 0
        
        self.login_lbl = QLabel('Логин')
        self.login_edit = QLineEdit(self.login)
        self.password_lbl = QLabel('Пароль')
        self.password_edit = QLineEdit(self.password)
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.Auth_btn = QPushButton('Проверить')
        self.Auth_btn.clicked.connect(self.auth_func)
        
        QVBox = QVBoxLayout()
        QVBox.addWidget(self.login_lbl)
        QVBox.addWidget(self.login_edit)
        QVBox.addWidget(self.password_lbl)
        QVBox.addWidget(self.password_edit)
        QVBox.addWidget(self.Auth_btn)
        
        central_widget = QWidget()
        central_widget.setLayout(QVBox)
        self.setCentralWidget(central_widget)

    def auth_func(self):
        login_check = self.login_edit.text()
        password_check = self.password_edit.text()
        if login_check == self.login and password_check == self.password:
            Test_window = Test()
            Test_window.show()
            Auth_window.close() 
        else:
            self.captcha_fail += 1
            if self.captcha_fail >= 3:
                self.captcha_fail = 0
                self.Captcha_window = Captcha()
                self.Captcha_window.show()
                self.setDisabled(True)

class Captcha(QMainWindow):
    def __init__(self):
        super().__init__()

        self.captcha = 0000
        
        self.text_lbl = QLabel('Пройдите каптчу')
        self.captcha_lbl = QLabel()
        self.captcha_edit = QLineEdit()
        self.captcha_btn = QPushButton('Проверить')
        self.captcha_btn.clicked.connect(self.verify)
        
        self.generate()
        
        self.QVBox = QVBoxLayout()
        self.QVBox.addWidget(self.text_lbl)
        self.QVBox.addWidget(self.captcha_lbl)
        self.QVBox.addWidget(self.captcha_edit)
        self.QVBox.addWidget(self.captcha_btn)
        
        central_widget = QWidget()
        central_widget.setLayout(self.QVBox)
        self.setCentralWidget(central_widget)
        
    def generate(self):
        self.captcha = str(random.randint(1000,9999))
        self.captcha_lbl.setText(self.captcha)
    
    
    def verify(self):
        if self.captcha == self.captcha_edit.text():
            QMessageBox.information(self, 'Успех','Вы прошли каптчу')
            Auth_window.setDisabled(False)
            self.close()
        else:
            self.block_timer()
    
    
    def block_timer(self):
        self.setDisabled(True)
        
        self.block_time = 10
        self.block_label = QLabel()
        
        self.QVBox.addWidget(self.block_label)
        
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.timer_update)
        self.timer.start()
        
    def timer_update(self):
        self.block_label.setText('Блокировка будет длится еще ' + str(self.block_time) + ' секунд')
        self.block_time -= 1
        if self.block_time <= -2:
            self.timer.stop()
            self.block_label.setText('')
            self.QVBox.removeWidget(self.block_label)
            self.setDisabled(False)



class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        
        

app = QApplication(sys.argv)
Auth_window = Auth()
Auth_window.show()
app.exec()
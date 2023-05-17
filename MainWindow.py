from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
import sys
from sql_test import User
from db_setting import session
from sqlalchemy import func


class Auth(QWidget):
    def __init__(self):
        super().__init__()
        login_lbl = QLabel('Login:')
        password_lbl = QLabel('Password:')
        
        login_edit = QLineEdit()
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        login_btn = QPushButton('Log In')
        
        NextPrevLayout = QHBoxLayout()
        Next_btn = QPushButton('Next')
        Prev_btn = QPushButton('Prev')
        NextPrevLayout.addWidget(Prev_btn)
        NextPrevLayout.addWidget(Next_btn)
        Next_btn.clicked.connect(lambda: stack_widgets.setCurrentIndex(1))
        
        AuthLayout = QVBoxLayout()
        AuthLayout.addWidget(login_lbl)
        AuthLayout.addWidget(login_edit)
        AuthLayout.addWidget(password_lbl)
        AuthLayout.addWidget(password_edit)
        AuthLayout.addWidget(login_btn)
        AuthLayout.addLayout(NextPrevLayout)
        self.setLayout(AuthLayout)

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.login_lbl = QLabel('Login:')
        self.password_lbl = QLabel('Password:')
        self.password_repeat_lbl = QLabel('Repeat password:')
        
        self.login_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_repeat_edit = QLineEdit()
        self.password_repeat_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.register_btn = QPushButton('register')
        self.register_btn.clicked.connect(self.register_func)

        
        NextPrevLayout = QHBoxLayout()
        Next_btn = QPushButton('Next')
        Prev_btn = QPushButton('Prev')
        NextPrevLayout.addWidget(Prev_btn)
        NextPrevLayout.addWidget(Next_btn)
        Prev_btn.clicked.connect(lambda: stack_widgets.setCurrentIndex(0))
        Next_btn.clicked.connect(lambda: stack_widgets.setCurrentIndex(2))
        
        AuthLayout = QVBoxLayout()
        AuthLayout.addWidget(self.login_lbl)
        AuthLayout.addWidget(self.login_edit)
        AuthLayout.addWidget(self.password_lbl)
        AuthLayout.addWidget(self.password_edit)
        AuthLayout.addWidget(self.password_repeat_lbl)
        AuthLayout.addWidget(self.password_repeat_edit)
        AuthLayout.addWidget(self.register_btn)
        AuthLayout.addLayout(NextPrevLayout)
        self.setLayout(AuthLayout)
        
        
    def register_func(self):
            login = str(self.login_edit.text())
            password = str(self.password_edit.text())
            password_repeat = str(self.password_repeat_edit.text())
            checklogin = session.query(User.Login).filter(User.Login == login).first()
            
            if checklogin != None:
                QMessageBox.warning(self, "Ошибка", "Пользователь с таким именем уже существует")
                return
            elif login != "" and password != "" and password == password_repeat:
                LastId = session.query(func.max(User.id)).scalar()
                if LastId is None:
                    LastId = 0
                user = User(id=LastId + 1, Login=login, Password=password)
                session.add(user)
                session.commit()
                QMessageBox.information(self, "Success", "Вы успешно зарегистрированы")
            elif login == "" or password == "" or password_repeat == "": 
                QMessageBox.information(self, "info", "Введите данные")
                return
            else:
                QMessageBox.warning(self, "Error", "Неверно введенные данные")
                return
                


class DataBase(QWidget):
    def __init__(self):
        super().__init__()
        
        NextPrevLayout = QHBoxLayout()
        Next_btn = QPushButton('Next')
        Prev_btn = QPushButton('Prev')
        NextPrevLayout.addWidget(Prev_btn)
        NextPrevLayout.addWidget(Next_btn)
        Prev_btn.clicked.connect(lambda: stack_widgets.setCurrentIndex(1))
        
        usersbd = session.query(User.Login).all()
        listus = []
        for i in range(len(usersbd)):
            listus.append(usersbd[i][0])
        listusers = QListWidget()
        listusers.addItems(listus)
        
        DataBaseLayout = QVBoxLayout()
        DataBaseLayout.addWidget(listusers)
        DataBaseLayout.addLayout(NextPrevLayout)
        self.setLayout(DataBaseLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.AuthWidget = Auth()
        self.RegisterWidget = Register()
        self.DataBaseWidget = DataBase()
        
        global stack_widgets 
        stack_widgets = QStackedWidget()
        stack_widgets.addWidget(self.AuthWidget)
        stack_widgets.addWidget(self.RegisterWidget)
        stack_widgets.addWidget(self.DataBaseWidget)
        
        self.setCentralWidget(stack_widgets)
        
        
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
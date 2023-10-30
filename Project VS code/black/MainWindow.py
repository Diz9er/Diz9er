from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer
import sys, random
from DataBase import session, User
from sqlalchemy import func
    
    # Окно состоящее из трех страниц: 
    #     авторизация(не проработана),
    #     регистрация(с логикой и связью с бд),
    #     список пользователей(со связью с бд).


class Auth(QWidget):
    def __init__(self):
        super().__init__()
        self.failed = 0
        self.login_lbl = QLabel('Login:')
        self.password_lbl = QLabel('Password:')
        
        self.login_edit = QLineEdit("Admin")
        self.password_edit = QLineEdit("Admin")
        self.password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        self.login_btn = QPushButton('Log In')
        self.login_btn.clicked.connect(self.auth_func)
        
        NextPrevLayout = QHBoxLayout()
        Next_btn = QPushButton('Next')
        Prev_btn = QPushButton('Prev')
        NextPrevLayout.addWidget(Prev_btn)
        NextPrevLayout.addWidget(Next_btn)
        Next_btn.clicked.connect(lambda: stack_widgets.setCurrentIndex(1))
        
        AuthLayout = QVBoxLayout()
        AuthLayout.addWidget(self.login_lbl)
        AuthLayout.addWidget(self.login_edit)
        AuthLayout.addWidget(self.password_lbl)
        AuthLayout.addWidget(self.password_edit)
        AuthLayout.addWidget(self.login_btn)
        AuthLayout.addLayout(NextPrevLayout)
        self.setLayout(AuthLayout)
    
    def auth_func(self):
        login = str(self.login_edit.text())
        password = str(self.password_edit.text())
        checklogin = session.query(User.Login).filter(User.Login == login).first()
        checkpassword = session.query(User.Password).filter(User.Login == login).first()
        if login != "" and password != "": 
            if checklogin != None:
                if password == checkpassword[0]:
                    self.NewWin = NewWindow()
                    self.NewWin.show()
                    window.close()
                else: 
                    QMessageBox.warning(self, "Error", "Неверный пароль")
                    self.fail()
                        
            else:
                QMessageBox.warning(self, "Error", "Пользователь с таким именем не найден")
                self.fail()
                
        elif login == "" or password == "":
            QMessageBox.information(self, "info", "Введите данные")
            return
        else:
            QMessageBox.warning(self, "Error", "Неверно введенные данные")
            self.fail()
    
    def fail(self):
        self.failed = self.failed + 1
        if self.failed >= 5:
            self.captcha_dialog = CaptchaDialog()
            self.captcha_dialog.show()
            self.setEnabled(False)
            
            
class CaptchaDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        capcha = str(random.randint(1000,9999))
        capcha_lbl = QLabel(capcha)
        capcha_edit = QLineEdit()
        
        QVbox = QVBoxLayout()
        QVbox.addWidget(capcha_lbl)
        QVbox.addWidget(capcha_edit)
        self.setLayout(QVbox)
        


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
            listus.append(usersbd[i][i])
        listusers = QListWidget()
        listusers.addItems(listus)
        
        DataBaseLayout = QVBoxLayout()
        DataBaseLayout.addWidget(listusers)
        DataBaseLayout.addLayout(NextPrevLayout)
        self.setLayout(DataBaseLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 200)
        self.AuthWidget = Auth()
        self.RegisterWidget = Register()
        self.DataBaseWidget = DataBase()
        
        
        global stack_widgets 
        stack_widgets = QStackedWidget()
        stack_widgets.addWidget(self.AuthWidget)
        stack_widgets.addWidget(self.RegisterWidget)
        stack_widgets.addWidget(self.DataBaseWidget)
        self.setCentralWidget(stack_widgets)
        
        
class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 200)
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)        
        
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
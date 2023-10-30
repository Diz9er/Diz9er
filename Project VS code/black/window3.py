from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
        QVBoxLayout, QWidget, QFrame, QStackedWidget, QLineEdit)
import sys

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        login_lbl = QLabel('Login:')
        password_lbl = QLabel('Password:')
        error_lbl = QLabel('')
        
        login_edit = QLineEdit()
        password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        
        login_layout = QHBoxLayout()
        login_layout.addWidget(login_lbl)
        login_layout.addWidget(login_edit)

        password_layout = QHBoxLayout()
        password_layout.addWidget(password_lbl)
        password_layout.addWidget(password_edit)
        
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(error_lbl)
        
        login_btn = QPushButton('Login')
        login_btn.setDefault(True)
        login_btn.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))
        
        signup_btn = QPushButton('Sign Up')
        signup_btn.setDefault(False)
        signup_btn.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))
        
        buttons_layout.addWidget(login_btn)
        buttons_layout.addWidget(signup_btn)
        
        layout = QVBoxLayout()
        layout.addLayout(login_layout)
        layout.addLayout(password_layout)
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)

class SignupPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        login_lbl = QLabel('Login:')
        password_lbl = QLabel('Password:')
        confirm_password_lbl = QLabel('Confirm Password:')
        error_lbl = QLabel('')
        
        login_edit = QLineEdit()
        password_edit = QLineEdit()
        confirm_password_edit = QLineEdit()
        password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password_edit.setEchoMode(QLineEdit.EchoMode.Password)
        
        login_layout = QHBoxLayout()
        login_layout.addWidget(login_lbl)
        login_layout.addWidget(login_edit)

        password_layout = QHBoxLayout()
        password_layout.addWidget(password_lbl)
        password_layout.addWidget(password_edit)
        
        confirm_password_layout = QHBoxLayout()
        confirm_password_layout.addWidget(confirm_password_lbl)
        confirm_password_layout.addWidget(confirm_password_edit)
        
        buttons_layout = QVBoxLayout()
        buttons_layout.addWidget(error_lbl)
        
        signup_btn = QPushButton('Sign Up')
        signup_btn.clicked.connect(lambda: stacked_widget.setCurrentIndex(0))
        
        buttons_layout.addWidget(signup_btn)
        
        layout = QVBoxLayout()
        layout.addLayout(login_layout)
        layout.addLayout(password_layout)
        layout.addLayout(confirm_password_layout)
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Stacked Widget Example')
        
        global stacked_widget
        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(LoginPage())
        stacked_widget.addWidget(QWidget())
        stacked_widget.addWidget(SignupPage())
        
        layout = QVBoxLayout()
        layout.addWidget(stacked_widget)
        self.setLayout(layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
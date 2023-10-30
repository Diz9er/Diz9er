from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer, Qt
import random
import sys
from DataBase import User, session
from sqlalchemy import func

class CapchaDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Капча")
        self.label = QLabel("Введите капчу:")
        self.textbox = QLineEdit()
        self.button = QPushButton("Проверить")
        self.button.clicked.connect(self.verify_captcha)
        
        self.timer_label = QLabel("Таймер: 10")
        self.timer_counter = 10
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_timer)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textbox)
        layout.addWidget(self.timer_label)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def verify_captcha(self):
        captcha = self.textbox.text()
        print("Проверка капчи:", captcha)


        if captcha.lower() == self.label.text(): 
            self.accept()
        else:
            self.textbox.setDisabled(True)  
            self.timer_counter = 11
            self.generate_captcha()
            self.timer.start()
            QMessageBox.critical(self, "Ошибка", "Неправильная капча")

    def start_timer(self):
        
        self.timer_counter = 10
        self.timer.start()
        

    def update_timer(self):
        self.timer_counter -= 1
        self.timer_label.setText(f"Таймер: {self.timer_counter}")

        if self.timer_counter == 0:
            self.timer.stop()
            self.textbox.setDisabled(False)
            
        self.captcha_label = QLabel(self)
        self.captcha_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        

    def generate_captcha(self):
        captcha1 = str(random.randint(1000, 9999))
         
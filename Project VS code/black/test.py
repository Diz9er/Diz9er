import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QLabel
from PyQt6.QtCore import QTimer


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Вход в систему')
        self.setGeometry(200, 200, 300, 200)

        self.username_label = QLabel('Имя пользователя', self)
        self.username_label.setGeometry(50, 50, 100, 30)
        self.username_input = QLabel(self)
        self.username_input.setGeometry(150, 50, 100, 30)

        self.password_label = QLabel('Пароль', self)
        self.password_label.setGeometry(50, 90, 100, 30)
        self.password_input = QLabel(self)
        self.password_input.setGeometry(150, 90, 100, 30)

        self.login_button = QPushButton('Вход', self)
        self.login_button.setGeometry(100, 130, 100, 30)
        self.login_button.clicked.connect(self.login)

        self.attempts = 0

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Проверка имени пользователя и пароля
        if username == 'admin' and password == '123':
            self.show_main_window()
        else:
            self.show_captcha()
            self.block_ui()

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def show_captcha(self):
        self.captcha_dialog = CaptchaDialog()
        self.captcha_dialog.show()

    def block_ui(self):
        self.timer = QTimer()
        self.timer.singleShot(10000, self.unblock_ui)
        self.setEnabled(False)

    def unblock_ui(self):
        self.captcha_dialog.close()
        self.setEnabled(True)
        self.attempts = 0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Главное окно')
        self.setGeometry(200, 200, 300, 200)

        self.label = QLabel('Добро пожаловать!', self)
        self.label.setGeometry(50, 50, 200, 50)


class CaptchaDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Капча')
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel('Введите текст с картинки:', self)
        self.label.setGeometry(50, 50, 200, 30)

        self.input = QLabel(self)
        self.input.setGeometry(50, 90, 200, 30)

        self.button = QPushButton('OK', self)
        self.button.setGeometry(100, 140, 100, 30)
        self.button.clicked.connect(self.accept)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec())
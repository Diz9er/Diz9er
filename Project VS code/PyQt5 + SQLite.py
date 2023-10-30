import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QDialog, QVBoxLayout, QHBoxLayout, QDialogButtonBox
import sqlite3

class RegisterDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle('Регистрация')

        # Создаем виджеты для ввода логина, пароля и email
        self.login_label = QLabel(self)
        self.login_label.setText('Логин:')
        self.login_input = QLineEdit(self)

        self.password_label = QLabel(self)
        self.password_label.setText('Пароль:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        self.email_label = QLabel(self)
        self.email_label.setText('Email:')
        self.email_input = QLineEdit(self)

        # Создаем кнопки для сохранения и отмены регистрации
        self.buttons = QDialogButtonBox(self)
        self.buttons.setStandardButtons(QDialogButtonBox.Save | QDialogButtonBox.Cancel)

        # Размещаем виджеты на форме регистрации
        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

        # Подключаем сигналы от кнопок
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def get_values(self):
        # Возвращаем значения из полей ввода
        return (self.login_input.text(),
                self.password_input.text(),
                self.email_input.text())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle('Список пользователей')

        # Устанавливаем размеры окна и его положение на экране
        self.setGeometry(300, 300, 350, 250)

        # Создаем кнопки для авторизации, регистрации и вывода пользователей
        self.auth_button = QPushButton(self)
        self.auth_button.setText('Авторизация')
        self.auth_button.move(50, 50)
        self.auth_button.clicked.connect(self.auth)

        self.register_button = QPushButton(self)
        self.register_button.setText('Регистрация')
        self.register_button.move(50, 90)
        self.register_button.clicked.connect(self.register)

        self.users_button = QPushButton(self)
        self.users_button.setText('Список пользователей')
        self.users_button.move(50, 130)
        self.users_button.clicked.connect(self.get_users)

        # Создаем виджет для вывода данных из базы данных
        self.data_output = QTextEdit(self)
        self.data_output.move(170, 50)
        self.data_output.resize(150, 140)

        # Изначально скрываем виджет списка пользователей
        self.data_output.hide()

    def auth(self):
        # Создаем окно авторизации
        auth_window = AuthWindow()
        result = auth_window.exec_()

        # Если пользователь авторизовался, выводим его данные
        if result == QDialog.Accepted:
            self.data_output.show()
            self.data_output.setText("Добро пожаловать, " + auth_window.username + "!\nВаш Email: " + auth_window.email)
        else:
            # Иначе выводим сообщение об ошибке
            QMessageBox.warning(self, 'Ошибка', 'Неправильный логин или пароль.')

    def register(self):
        # Создаем окно регистрации
        register_dialog = RegisterDialog()
        result = register_dialog.exec_()

        # Если пользователь зарегистрирован, добавляем его в базу данных
        if result == QDialog.Accepted:
            values = register_dialog.get_values()

            # Подключаемся к базе данных
            conn = sqlite3.connect('users1.db')
            cur = conn.cursor()

            # Выполняем запрос на добавление пользователя в базу данных
            cur.execute("INSERT INTO users (login, password, email) VALUES (?, ?, ?)", values)

            # Закрываем соединение с базой данных
            cur.close()
            conn.commit()
            conn.close()

            # Выводим сообщение об успешной регистрации
            QMessageBox.information(self, 'Успешно', 'Пользователь зарегистрирован.')
        else:
            # Иначе ничего не делаем
            pass

    def get_users(self):
        # Подключаемся к базе данных
        conn = sqlite3.connect('users1.db')
        cur = conn.cursor()

        # Выполняем запрос на выборку всех пользователей из базы данных
        cur.execute("SELECT * FROM users")
        results = cur.fetchall()

        # Формируем строку для вывода списка пользователей
        users = ''
        for result in results:
            users += result[1] + ', '

        # Закрываем соединение с базой данных
        cur.close()
        conn.close()

        # Выводим список пользователей
        self.data_output.show()
        self.data_output.setText('Список пользователей:\n' + users[:-2])

class AuthWindow(QDialog):
    def __init__(self):
        super().__init__()

        # Устанавливаем заголовок окна
        self.setWindowTitle('Авторизация')

        # Создаем виджеты для ввода логина и пароля
        self.username_label = QLabel(self)
        self.username_label.setText('Логин:')
        self.username_input = QLineEdit(self)

        self.password_label = QLabel(self)
        self.password_label.setText('Пароль:')
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Создаем кнопки для авторизации и отмены
        self.buttons = QDialogButtonBox(self)
        self.buttons.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        # Размещаем виджеты на форме авторизации
        layout = QVBoxLayout()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.buttons)
        self.setLayout(layout)

        # Подключаем сигналы от кнопок
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)

    def accept(self):
        # Получаем логин и пароль из полей ввода
        username = self.username_input.text()
        password = self.password_input.text()

        # Подключаемся к базе данных
        conn = sqlite3.connect('users1.db')
        cur = conn.cursor()

        # Выполняем запрос на выборку пользователей по логину и паролю
        cur.execute("SELECT * FROM users WHERE login = ? AND password = ?", (username, password))

        # Получаем результат запроса
        result = cur.fetchone()

        # Если пользователь найден, сохраняем его имя и email и закрываем окно авторизации
        if result is not None:
            self.username = result[1]
            self.email = result[3]
            super().accept()
        else:
            # Иначе выводим сообщение об ошибке
            QMessageBox.warning(self, 'Ошибка', 'Неправильный логин или пароль.')

        # Закрываем соединение с базой данных
        cur.close()
        conn.close()

if __name__ == '__main__':
    # Создаем экземпляр приложения
    app = QApplication(sys.argv)

    # Создаем экземпляр главного окна
    main_window = MainWindow()

    # Отображаем окно
    main_window.show()

    # Запускаем главный цикл приложения
    sys.exit(app.exec_())
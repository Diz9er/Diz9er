from PyQt6.QtWidgets import *


class MainPage(QWidget):
    def __init__(self):
        super().__init__()

        # Создание списка элементов
        items = ["Item 1", "Item 2", "Item 3"]

        # Создание списка и добавление элементов в него
        self.list_widget = QListWidget()
        self.list_widget.addItems(items)

        # Создание второй страницы с формой ввода
        self.form_widget = QWidget()
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.surname_label = QLabel("Surname:")
        self.surname_input = QLineEdit()

        # Размещение элементов формы на странице
        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        self.form_widget.setLayout(layout)

        # Создание кнопок для переключения страниц
        self.show_list_button = QPushButton("Show List")
        self.show_list_button.clicked.connect(self.show_list)
        self.show_form_button = QPushButton("Show Form")
        self.show_form_button.clicked.connect(self.show_form)

        # Создание layout для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.show_list_button)
        button_layout.addWidget(self.show_form_button)

        # Создание layout для окна
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.list_widget)
        main_layout.addWidget(self.form_widget)

        # Установка layout и заголовка
        self.setLayout(main_layout)
        self.setWindowTitle("Multiple Pages Example")

    # Функция для переключения на страницу со списком элементов
    def show_list(self):
        self.list_widget.show()
        self.form_widget.hide()

    # Функция для переключения на страницу с формой для заполнения
    def show_form(self):
        self.list_widget.hide()
        self.form_widget.show()


if __name__ == '__main__':
    app = QApplication([])
    main_page = MainPage()
    main_page.show()
    app.exec()
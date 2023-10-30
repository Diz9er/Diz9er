from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QStackedWidget

class StartPage(QWidget):
    def __init__(self):
        super().__init__()
        
        # Создание виджетов
        self.label = QLabel('Это стартовая страница!')
        
        self.button_1 = QPushButton('Перейти на страницу 1')
        self.button_2 = QPushButton('Перейти на страницу 2')
        
        # Создание разметки
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button_1)
        layout.addWidget(self.button_2)
        
        # Установка разметки
        self.setLayout(layout)

class Page1(QWidget):
    def __init__(self):
        super().__init__()
        
        # Создание виджетов
        self.label = QLabel('Это страница 1!')
        self.text_edit = QTextEdit()
        self.button = QPushButton('Вернуться на стартовую страницу')
        
        # Создание разметки
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_edit)
        layout.addWidget(self.button)
        
        # Установка разметки
        self.setLayout(layout)
        
        # Соединение сигналов со слотами
        self.button.clicked.connect(self.go_to_start_page)
    
    def go_to_start_page(self):
        stacked_widget.setCurrentIndex(0)

class Page2(QWidget):
    def __init__(self):
        super().__init__()
        
        # Создание виджетов
        self.label = QLabel('Это страница 2!')
        self.line_edit = QLineEdit()
        self.button = QPushButton('Вернуться на стартовую страницу')
        
        # Создание разметки
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)
        
        # Установка разметки
        self.setLayout(layout)
        
        # Соединение сигналов со слотами
        self.button.clicked.connect(self.go_to_start_page)
    
    def go_to_start_page(self):
        stacked_widget.setCurrentIndex(0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Пример со страницами')
        
        # Создание виджетов
        self.start_page = StartPage()
        self.page_1 = Page1()
        self.page_2 = Page2()
        
        # Создание stacked виджета
        global stacked_widget
        stacked_widget = QStackedWidget()
        stacked_widget.addWidget(self.start_page)
        stacked_widget.addWidget(self.page_1)
        stacked_widget.addWidget(self.page_2)
        
        # Установка stacked виджета в центре главного окна
        self.setCentralWidget(stacked_widget)
        
        # Соединение сигналов со слотами
        self.start_page.button_1.clicked.connect(lambda: stacked_widget.setCurrentIndex(1))
        self.start_page.button_2.clicked.connect(lambda: stacked_widget.setCurrentIndex(2))

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
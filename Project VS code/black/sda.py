import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QStackedWidget, QVBoxLayout, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # создаем кнопки
        self.button1 = QPushButton('Layer 1')
        self.button2 = QPushButton('Layer 2')
        self.button3 = QPushButton('Layer 3')

        # создаем QStackedWidget и добавляем три слоя
        self.stacked_widget = QStackedWidget()
        self.layer1 = QWidget()
        self.layer2 = QWidget()
        self.layer3 = QWidget()
        self.stacked_widget.addWidget(self.layer1)
        self.stacked_widget.addWidget(self.layer2)
        self.stacked_widget.addWidget(self.layer3)

        # добавляем текст на каждый слой
        self.layer1_label = QLabel('This is layer 1')
        self.layer2_label = QLabel('This is layer 2')
        self.layer3_label = QLabel('This is layer 3')
        self.layer1_layout = QVBoxLayout()
        self.layer1_layout.addWidget(self.layer1_label)
        self.layer1.setLayout(self.layer1_layout)
        self.layer2_layout = QVBoxLayout()
        self.layer2_layout.addWidget(self.layer2_label)
        self.layer2.setLayout(self.layer2_layout)
        self.layer3_layout = QVBoxLayout()
        self.layer3_layout.addWidget(self.layer3_label)
        self.layer3.setLayout(self.layer3_layout)

        # создаем макет и добавляем кнопки и QStackedWidget
        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.stacked_widget)

        # устанавливаем макет для главного окна
        self.setLayout(layout)

        # устанавливаем обработчики событий для кнопок
        self.button1.clicked.connect(self.show_layer1)
        self.button2.clicked.connect(self.show_layer2)
        self.button3.clicked.connect(self.show_layer3)

    def show_layer1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_layer2(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_layer3(self):
        self.stacked_widget.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

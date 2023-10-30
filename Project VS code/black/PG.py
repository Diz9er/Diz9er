import sys

from PyQt6.QtWidgets import QApplication,  QMainWindow, QPushButton, QVBoxLayout, QLabel, QLayout, QLineEdit, QWidget, QMessageBox, QStackedWidget
from style import style
from sql_test import Student, Group, Course
from DataBase import session
session
name = session.query(Student.firstname).filter(Student.id > 0).first()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        
        self.page1 = QWidget()
        self.page2 = QWidget()
        self.page3 = QWidget()
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        
        self.page1_label = QLabel(name[0], self.page1)

        self.page1_label.move(50, 50)

        self.page1_button = QPushButton('Назад', self.page1)
        self.page1_button.move(50, 100)

        self.page1_button = QPushButton('Вперед', self.page1)
        self.page1_button.move(150, 100)
        self.page1_button.clicked.connect(self.show_page2)

        layout = QVBoxLayout()
        lbl_1 = QLabel("lbl_1")
        lbl_2 = QLabel("lbl_2")
        txt_login = QLineEdit()
        txt_pass = QLineEdit()
        txt_pass.setEchoMode(QLineEdit.EchoMode.Password)

        self.page2_label = QLabel('Страница 2', self.page2)
        self.page2_label.move(50, 50)
        self.page2_login = QLineEdit(self.page2)
        self.page2_pass = QLineEdit(self.page2)

        self.page2_button = QPushButton('Назад', self.page2)
        self.page2_button.move(50, 100)
        self.page2_button.clicked.connect(self.show_page1)
        
        self.page2_button = QPushButton('Вперед', self.page2)
        self.page2_button.move(150, 100)
        self.page2_button.clicked.connect(self.show_page3)

        
        self.page3_label = QLabel('Страница 3', self.page3)
        self.page3_label.move(50, 50)

        self.page3_button = QPushButton('Назад', self.page3)
        self.page3_button.move(50, 100)
        self.page3_button.clicked.connect(self.show_page2)

        self.page3_button = QPushButton('Вперед', self.page3)
        self.page3_button.move(150, 100)


        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page1(self):
        self.stacked_widget.setCurrentWidget(self.page1)

    def show_page2(self):
        self.stacked_widget.setCurrentWidget(self.page2)

    def show_page3(self):
        self.stacked_widget.setCurrentWidget(self.page3)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet(style)
    window.show()
    sys.exit(app.exec())

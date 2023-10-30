from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer, Qt
import random
import sys
from DataBase import User, session
from sqlalchemy import func

class CarQuiz(QWidget):
    def __init__(self, login):
        super().__init__()
        self.setWindowTitle("Car Quiz")
        self.login2 = login
        self.questions = [
            {
                'question': "Какая форма кузова вам нравится?",
                'options': ["Седан", "Хэтчбек", "Внедорожник", "Купе"]
            },
            {
                'question': "Какой тип топлива вы предпочитаете?",
                'options': ["Бензин", "Дизель", "Электричество", "Гибрид"]
            },
            {
                'question': "Какой размер вам важен?",
                'options': ["Компактный", "Средний", "Большой", "Огромный"]
            },
            {
                'question': "Какой у вас бюджет?",
                'options': ["Низкий", "Средний", "Высокий"]
            }
        ]
        self.answers = []
        self.current_question = 0
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.question_label = QLabel()
        layout.addWidget(self.question_label)

        self.options = []
        for _ in range(len(self.questions[self.current_question]['options'])):
            option = QRadioButton()
            layout.addWidget(option)
            self.options.append(option)

        next_button = QPushButton("Далее")
        next_button.clicked.connect(self.next_question)
        layout.addWidget(next_button)

        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question]
        self.question_label.setText(question['question'])

        options = question['options']
        for i in range(len(options)):
            self.options[i].setText(options[i])
            self.options[i].setChecked(False)

    def next_question(self):
        selected_option = None
        for option in self.options:
            if option.isChecked():
                selected_option = option.text()
                break

        if selected_option is not None:
            self.answers.append(selected_option)
            self.current_question += 1

            if self.current_question < len(self.questions):
                self.show_question()
            else:
                self.show_result()

    def show_result(self):
        result_label = QLabel()
        result_label.setText("Ваша идеальная марка машины: " + self.calculate_result())
        layout = self.layout()
        layout.itemAt(layout.count() - 1).widget().hide()
        layout.addWidget(result_label)

    def calculate_result(self):
        answer = "Toyota"
        self.write_to_file(answer)
        return answer
        
    
    def write_to_file(self,answer):
        file = "Answer.txt"
        ans = self.login2 + ":" + answer
        with open(file, 'a') as file:
            file.write(ans + "\n")
            
class Test(QWidget):
    def __init__(self):
        super().__init__()
        Test_lbl = QLabel("Test\n")
        Test_lbl_2 = QLabel("Выберите верные правила поведения студента в кабинете")
        self.rBtn_1_True = QCheckBox("Не прикасаться к экрану монитора")
        self.rBtn_2_True = QCheckBox("Работать за компьютером чистыми сухими руками")
        self.rBtn_3_True = QCheckBox("Не трогать провода и разъемы соединительных кабелей")
        self.rBtn_4_True = QCheckBox("Не размещать на рабочем месте посторонние предметы")
        self.rBtn_5_False = QCheckBox("Обсуждать учебные процессы безмерным тоном")
        self.rBtn_6_False = QCheckBox("Не беспокоиться о чистоте своей обуви")
        self.rBtn_7_False = QCheckBox("Самостоятельно исправлять любые неисправности ПК")
        self.rBtn_8_False = QCheckBox("Пользоваться компьютером без действительной надобности")
        self.rBtn_9_False = QCheckBox("Свободно по своему желанию передвигаться по кабинету")
        self.Test_btn = QPushButton("Проверить")
        self.Test_btn.clicked.connect(self.Test_btn_func) 
        QVBox = QVBoxLayout()
        self.setLayout(QVBox)
        QVBox.addWidget(Test_lbl)
        QVBox.addWidget(Test_lbl_2)
        QVBox.addWidget(self.rBtn_1_True)
        QVBox.addWidget(self.rBtn_2_True)
        QVBox.addWidget(self.rBtn_5_False)
        QVBox.addWidget(self.rBtn_6_False)
        QVBox.addWidget(self.rBtn_3_True)
        QVBox.addWidget(self.rBtn_7_False)
        QVBox.addWidget(self.rBtn_4_True)
        QVBox.addWidget(self.rBtn_8_False)
        QVBox.addWidget(self.rBtn_9_False)
        QVBox.addWidget(self.Test_btn)
    
    def Test_btn_func(self):
        score = 0
        bad_score = 0
        if self.rBtn_1_True.isChecked() == True:
            score += 1
        if self.rBtn_2_True.isChecked() == True:
            score += 1
        if self.rBtn_3_True.isChecked() == True:
            score += 1
        if self.rBtn_4_True.isChecked() == True:
            score += 1
        if self.rBtn_5_False.isChecked() == True:
            bad_score += 1
        if self.rBtn_6_False.isChecked() == True:
            bad_score += 1
        if self.rBtn_7_False.isChecked() == True:
            bad_score += 1
        if self.rBtn_8_False.isChecked() == True:
            bad_score += 1
        if self.rBtn_9_False.isChecked() == True:
            bad_score += 1
        score = (score*100)/4
        bad_score = (bad_score*100)/5
        print(f"Ваш результат содержит {score}% верных и {bad_score}% неверных ответов")
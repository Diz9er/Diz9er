from PyQt6.QtWidgets import *
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
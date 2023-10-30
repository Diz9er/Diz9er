# импортируем необходимые модули
from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
import sys

# создаем приложение
app = QApplication(sys.argv)

# создаем таблицу
tableWidget = QTableWidget()
tableWidget.setColumnCount(2) # устанавливаем количество колонок

# устанавливаем заголовки для колонок
tableWidget.setHorizontalHeaderLabels(['Name', 'ID'])

# добавляем данные в таблицу
tableWidget.setRowCount(3) # устанавливаем количество строк
tableWidget.setItem(0, 0, QTableWidgetItem("Иван")) # добавляем ячейки для таблицы
tableWidget.item(0,0).setData(100, "001") # устанавливаем ID элемента в пользовательском флаге
tableWidget.setItem(1, 0, QTableWidgetItem("Алексей"))
tableWidget.item(1,0).setData(100, "002")
tableWidget.setItem(2, 0, QTableWidgetItem("Марина"))
tableWidget.item(2,0).setData(100, "003")

# выводим таблицу на экран
tableWidget.show()

# запускаем приложение
sys.exit(app.exec())
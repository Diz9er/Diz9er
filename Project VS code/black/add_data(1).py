from sql_test import Student, Group, Course
from DataBase import session
session
# i=2
# while True: 
#     _what = input("Добавить нового студента?(да,нет):")
#     if _what == "Нет" or _what == "нет" or _what == "НЕТ":
#         break
#     _student = Student(
#     secondname = input("Введите фамилию студента:"),
#     firstname = input("Введите имя студента:"),
#     middlename = input("Введите отчество студента:"),
#     group_id = input("Введите айди группы студента:")
#     )
#     session.add(_student)
# _group = Group(
# id = 1,
# group_name = '1isip',
# course_id = 1
# )
# session.add(_group)

# _course = Course(
#     id = 1,
#     course_name = '2'
# )
# session.add(_course)


# sql_select_student = select(Student).where 
# for row in session.execute(sql_select_student):
#     print(row)



print(session.query(Student.id,Student.middlename).filter(Student.firstname == "Максим").all())

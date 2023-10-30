from sql_test import Student, Group, Course
from DataBase import session
session

# _course = Course(
#     id = 1,
#     course_name = '2'
# )
# session.add(_course)

# _group = Group(
#     id = 1,
#     group_name = "ISIP",
#     course_id = 1
# )

# _student = Student(
#     id = 1,
#     firstname = "Максим",
#     secondname = "Иванов",
#     middlename = "Иванович",
#     group_id = 1
#     )

# session.add(_student)
# session.commit()

# print(session.query(Student.secondname, Student.firstname, Student.middlename).filter(Student.id > 0).all())
# name = session.query(Student.firstname).filter(Student.id > 0).first()
# print(name[0])
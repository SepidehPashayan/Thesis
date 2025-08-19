import json

from sqlalchemy import true

class Student():
    def __init__(self):
        pass
    def get_student(self):
        self.username = input("username:")
        self.password = input("password:")
    def read_information_student(self):
        flag = False
        with open ('student.json','r')as s:
            students = json.load(s)
        for student in students:
            if student['username']== int(self.username) and  student['password']== int(self.password) :
                print('\n')
                print(f"welcome {student['name']} {student['family']}")
                flag =True
                break
        if flag==False:
            print("\tsorry you don't access to the site")
        


class Teacher():
    def __init__(self):
        pass
    def get_teacher(self):
        self.username = input("username:")
        self.password = input("password:")
    def read_information_teacher(self):
        flag = False
        with open ('teacher.json','r')as t:
            teachers = json.load(t)
        for teacher in teachers:
            if teacher['username']== int(self.username) and  teacher['password']== int(self.password) :
                print('\n')
                print(f"welcome {teacher['name']} {teacher['family']}")
                flag = True
                break
        if flag == False:
            print("\tsorry you don't access to the site")

print("1.Student")
print("2.Teacher")
while True:
    x = int(input("enter:"))
    if x==1:
        greet = "welcome student"
        print(greet.center(50,'.'))
        stu = Student()
        stu.get_student()
        stu.read_information_student()
        break
    elif x==2:
        greet = "welcome teacher"
        print(greet.center(50,'.'))
        tea = Teacher()
        tea.get_teacher()
        tea.read_information_teacher()
        break
    print("\tError:wrong number")

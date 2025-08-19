import json
import PyPDF2
import ts

class Student():
    def __init__(self):
        pass
    def get_student(self):
        self.username = input("username:")
        self.password = input("password:")
    def read_information(self):
        for x in range(1):
            new_data = json.load(s1)
            if new_data['username']==self.username and new_data['password']==self.password:
                print(f"welcome {new_data['name']} {new_data['family']}")
class Teacher():
    def __init__(self):
        pass
    def get_teacher(self):
        self.username = input("username:")
        self.password = input("password:")

print("1.Student")
print("2.Teacher")
while True:
    x = int(input("enter:"))
    if x==1:
        greet = "welcome student"
        print(greet.center(50,'.'))
        stu = Student()
        stu.get_student()
        stu.read_information()
        break
    elif x==2:
        greet = "welcome teacher"
        print(greet.center(50,'.'))
        tea = Teacher()
        tea.get_teacher()
        break
    print("\tError:wrong number")

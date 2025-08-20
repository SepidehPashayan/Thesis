import json
import datetime
import uuid

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
        return flag
    def request(self):
        with open ('course.json','r')as c:
            courses = json.load(c)
            for course in courses:
                print(course)
            now = datetime.datetime.now()
            uniq_id = str(uuid.uuid4())
            while True:
                try:
                    z=int(input("please enter the id :"))
                except ValueError:
                    print("Error:you must enter a number")
                    continue
                if z==1 or z==2:
                    for cou in courses:
                        if z==cou['id']:
                            name = cou['teacher_name']
                            fam = cou['teacher_family']
                    r1={
                        'request_id':uniq_id,
                        'date':now.ctime(),
                        'student_id':int(self.username),
                        'teacher_name':name,
                        'teacher_family':fam,
                        'condition':'waiting for the response'
                    }
                    break
                else:
                    print("\tError:you must enter 1 or 2")
        with open('request.json','a')as r:
            json.dump(r1,r,indent=4)




        


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
        if stu.read_information_student():
            print("1.request for thesis")
            print("2.see the thesis condition")
            y=int(input("enter:"))
            if y==1:
                stu.request()
            else:
                print("jfxh")
        break
    elif x==2:
        greet = "welcome teacher"
        print(greet.center(50,'.'))
        tea = Teacher()
        tea.get_teacher()
        tea.read_information_teacher()
        break
    else:
        print("\tError:wrong number")

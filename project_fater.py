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
                print(f".....welcome {student['name']} {student['family']}.....")
                print('\n')
                flag =True
                break
        if flag==False:
            print("\tsorry you don't access to the site")
        return flag
    def request(self):
        with open ('course.json','r')as c:
            courses = json.load(c)
            for course in courses:
                print('\n')
                print(f"id:{course['id']}")
                print(f"name:{course['name']}")
                print(f"teacher's name:{course['teacher_name']}")
                print(f"teacher's lastname:{course['teacher_family']}")
                print(f"year:{course['year']}")
                print(f"term:{course['y']}")
                print(f"capacity:{course['cap']}")
                print(f"resources:{course['curr']}")
                print(f"session:{course['session']}")
                print(f"unit:{course['unit']}")
                print("\n")
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
        try:
            with open('request.json','r')as r:
                requests = json.load(r)
        except (FileNotFoundError,json.JSONDecodeError):
            requests=[]

        requests.append(r1)
        with open('request.json','w')as r:
            json.dump(requests,r,indent=4)
        print("request saved successfully")
    def see_reactions(self):
        with open ('request.json','r')as r:
            requests = json.load(r)
            own_requests = [req for req in requests  if req['student_id']==int(self.password)]
            if own_requests:
                for req in own_requests:
                    print('\n')
                    print(f"id:{req['request_id']}")
                    print(f"date:{req['date']}")
                    print(f"student_id:{req['student_id']}")
                    print(f"teacher's name:{req['teacher_name']}")
                    print(f"teacher's last name:{req['teacher_family']}")
                    print(f"condition:{req['condition']}")
                    print('\n')
            else:
                print("No requests found for you")
                        




        


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
                print(f".....welcome {teacher['name']} {teacher['family']}.....")
                print('\n')
                self.name = teacher['name']
                self.family = teacher['family']
                flag = True
                break
        if flag == False:
            print("\tsorry you don't access to the site")
        return flag
    def see_requests(self):
        try:
            with open ('request.json','r')as r:
                requests = json.load(r)
                own_requests = [req for req in requests  if req['teacher_name']==self.name and req['teacher_family']==self.family]
                if own_requests:
                    for req in own_requests:
                        print('\n')
                        print(f"id:{req['request_id']}")
                        print(f"date:{req['date']}")
                        print(f"student_id:{req['student_id']}")
                        print(f"teacher's name:{req['teacher_name']}")
                        print(f"teacher's last name:{req['teacher_family']}")
                        print(f"condition:{req['condition']}")
                        print('\n')
                        if req['condition']=='waiting for the response':
                            print("1.Accept")
                            print("2.Reject")
                            while True:
                                x=int(input("choose:"))
                                if x in [1,2]:
                                    break
                                print("\tError:wrong number")
                            if x==1:
                                req['condition']='Accept'
                                print("answer saved successfully")
                            elif x==2:
                                req['condition']='Reject'
                                print("answer saved successfully")
                        with open('request.json','w')as r:
                            json.dump(requests,r,indent=4)
                else:
                        print("No requests found for you")
        except (FileNotFoundError,json.JSONDecodeError):
            print("\tError:the file is empty")
                
                
                    

                        



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
                stu.see_reactions()
        break
    elif x==2:
        greet = "welcome teacher"
        print(greet.center(50,'.'))
        tea = Teacher()
        tea.get_teacher()
        if tea.read_information_teacher():
            print("1.see the requests")
            z=int(input("enter:"))
            if z==1:
                tea.see_requests()
            else:
                print("hgkf")
        break
    else:
        print("\tError:wrong number")

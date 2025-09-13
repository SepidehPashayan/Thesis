import json
import datetime
import uuid

class Student:
    def __init__(self):
        pass

    def get_student(self):
        self.username = input("username:")
        self.password = input("password:")

    def read_information_student(self):
        flag = False
        with open('student.json', 'r') as s:
            students = json.load(s)
        for student in students:
            if student['username'] == int(self.username) and student['password'] == int(self.password):
                print(f".....welcome {student['name']} {student['family']}.....")
                flag = True
                break
        if not flag:
            print("sorry you don't access to the site")
        return flag

    def request(self):
        with open('course.json', 'r') as c:
            courses = json.load(c)
            for course in courses:
                if course['cap'] != 0:
                    print(f"id:{course['id']}")
                    print(f"name:{course['name']}")
                    print(f"teacher's name:{course['teacher_name']} {course['teacher_family']}")
                    print(f"year:{course['year']}")
                    print(f"term:{course['y']}")
                    print(f"capacity:{course['cap']}")
                    print(f"resources:{course['curr']}")
                    print(f"session:{course['session']}")
                    print(f"unit:{course['unit']}")
                    print("")

            now = datetime.datetime.now()
            uniq_id = str(uuid.uuid4())

            while True:
                try:
                    z = int(input("please enter the id :"))
                except ValueError:
                    print("Error: you must enter a number")
                    continue

                valid_ids = [course['id'] for course in courses if course['cap'] > 0]
                if z in valid_ids:
                    for cou in courses:
                        if z == cou['id']:
                            name = cou['teacher_name']
                            fam = cou['teacher_family']
                    r1 = {
                        'request_id': uniq_id,
                        'date': now.ctime(),
                        'student_id': int(self.username),
                        'teacher_name': name,
                        'teacher_family': fam,
                        'condition': 'waiting for the response',
                        'request_type': 'thesis'
                    }
                    break
                else:
                    print("Error: invalid id")

        try:
            with open('request.json', 'r') as r:
                requests = json.load(r)
        except (FileNotFoundError, json.JSONDecodeError):
            requests = []

        requests.append(r1)
        with open('request.json', 'w') as r:
            json.dump(requests, r, indent=4)
        print("request saved successfully")

    def see_reactions(self):
        with open('request.json', 'r') as r:
            requests = json.load(r)
            own_requests = [req for req in requests if req['student_id'] == int(self.username)]
            if own_requests:
                for req in own_requests:
                    print(f"id:{req['request_id']}")
                    print(f"date:{req['date']}")
                    print(f"student_id:{req['student_id']}")
                    print(f"teacher:{req['teacher_name']} {req['teacher_family']}")
                    print(f"condition:{req['condition']}")
                    print("")
                    if req['condition'] == 'Reject':
                        i = input("do you want to send a request again?(yes|no):")
                        if i.lower() == 'yes':
                            self.request()
            else:
                print("No requests found for you")

    def defense(self):
        try:
            with open('request.json', 'r') as r:
                requests = json.load(r)
        except (FileNotFoundError, json.JSONDecodeError):
            print("No requests found")
            return

        sid = int(self.username)
        own_requests = [req for req in requests if req.get('student_id') == sid]
        now = datetime.datetime.now()
        eligible = []
        for req in own_requests:
            if req.get('condition') != 'Accept':
                continue
            date_str = req.get('date')
            if not date_str:
                continue

            try:
                saved_date = datetime.datetime.strptime(date_str, "%a %b %d %H:%M:%S %Y")
            except Exception:
                try:
                    saved_date = datetime.datetime.fromisoformat(date_str)
                except Exception:
                    continue

            days = (now - saved_date).days
            if days >= 60:
                eligible.append((req, saved_date, days))

        if not eligible:
            print("Error: you can't request for defense")
            return

        for req, saved_date, days in eligible:
            print(f"id: {req.get('request_id')}")
            print(f"date accepted: {req.get('date')}")
            print(f"teacher: {req.get('teacher_name')} {req.get('teacher_family')}")
            print(f"elapsed days: {days}")
            ans = input("do you want to request for defense?(yes/no): ").strip().lower()
            if ans == 'yes':
                new_req = {
                    'request_id': str(uuid.uuid4()),
                    'date': now.ctime(),
                    'student_id': sid,
                    'teacher_name': req.get('teacher_name'),
                    'teacher_family': req.get('teacher_family'),
                    'condition': 'waiting for defense response',
                    'request_type': 'defense'
                }
                try:
                    with open('request_defense.json', 'r') as f:
                        defense_requests = json.load(f)
                except (FileNotFoundError, json.JSONDecodeError):
                    defense_requests = []
                defense_requests.append(new_req)
                with open('request_defense.json', 'w') as f:
                    json.dump(defense_requests, f, indent=4)
                print("the defense request was registered")
            else:
                print("failed")


class Teacher:
    def __init__(self):
        pass

    def get_teacher(self):
        self.username = input("username:")
        self.password = input("password:")

    def read_information_teacher(self):
        flag = False
        with open('teacher.json', 'r') as t:
            teachers = json.load(t)
        for teacher in teachers:
            if teacher['username'] == int(self.username) and teacher['password'] == int(self.password):
                print(f".....welcome {teacher['name']} {teacher['family']}.....")
                self.name = teacher['name']
                self.family = teacher['family']
                flag = True
                break
        if not flag:
            print("sorry you don't access to the site")
        return flag

    def see_requests(self):
        try:
            with open('request.json', 'r') as r:
                requests = json.load(r)
                own_requests = [req for req in requests if req['teacher_name'] == self.name and req['teacher_family'] == self.family]
                if own_requests:
                    for req in own_requests:
                        print(f"id:{req['request_id']}")
                        print(f"date:{req['date']}")
                        print(f"student_id:{req['student_id']}")
                        print(f"teacher:{req['teacher_name']} {req['teacher_family']}")
                        print(f"condition:{req['condition']}")
                        print("")
                        if req['condition'] == 'waiting for the response':
                            print("1.Accept")
                            print("2.Reject")
                            while True:
                                try:
                                    x = int(input("choose:"))
                                    if x in [1, 2]:
                                        break
                                    print("Error: wrong number")
                                except ValueError:
                                    print("Error: wrong input")

                            if x == 1:
                                req['condition'] = 'Accept'
                                with open('course.json', 'r') as c:
                                    courses = json.load(c)
                                    for course in courses:
                                        if course['teacher_name'] == req['teacher_name'] and course['teacher_family'] == req['teacher_family']:
                                            if course['cap'] > 0:
                                                course['cap'] -= 1
                                    with open('course.json', 'w') as c:
                                        json.dump(courses, c, indent=4)
                            elif x == 2:
                                req['condition'] = 'Reject'
                        with open('request.json', 'w') as r:
                            json.dump(requests, r, indent=4)
                else:
                    print("No requests found for you")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: the file is empty")

    def see_defense_requests(self):
        try:
            with open('request_defense.json', 'r') as r:
                requests = json.load(r)
                own_requests = [req for req in requests if req['teacher_name'] == self.name and req['teacher_family'] == self.family]
                if own_requests:
                    for req in own_requests:
                        print(f"id:{req['request_id']}")
                        print(f"date:{req['date']}")
                        print(f"student_id:{req['student_id']}")
                        print(f"teacher:{req['teacher_name']} {req['teacher_family']}")
                        print(f"condition:{req['condition']}")
                        print("")
                        if req['condition'] == 'waiting for defense response':
                            print("1.Accept")
                            print("2.Reject")
                            while True:
                                try:
                                    x = int(input("choose:"))
                                    if x in [1, 2]:
                                        break
                                    print("Error: wrong number")
                                except ValueError:
                                    print("Error: wrong input")

                            if x == 1:
                                req['condition'] = 'Accept'
                            elif x == 2:
                                req['condition'] = 'Reject'
                        with open('request_defense.json', 'w') as r:
                            json.dump(requests, r, indent=4)
                else:
                    print("No defense requests found for you")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: the file is empty")


print("1.Student")
print("2.Teacher")
while True:
    try:
        x = int(input("enter:"))
    except ValueError:
        print("Error: wrong input")
        continue

    if x == 1:
        print("welcome student".center(50, '.'))
        stu = Student()
        stu.get_student()
        if stu.read_information_student():
            print("1.request for thesis")
            print("2.see the thesis condition")
            print("3.request for defense")
            y = int(input("enter:"))
            if y == 1:
                stu.request()
            elif y == 2:
                stu.see_reactions()
            elif y == 3:
                stu.defense()
        break
    elif x == 2:
        print("welcome teacher".center(50, '.'))
        tea = Teacher()
        tea.get_teacher()
        if tea.read_information_teacher():
            print("1.see the requests")
            print("2.see defense requests")
            z = int(input("enter:"))
            if z == 1:
                tea.see_requests()
            elif z == 2:
                tea.see_defense_requests()
        break
    else:
        print("Error: wrong number")

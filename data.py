import json

s1 = {'name':'Sepideh','family':'Pashayan','username':402103242,'password':402103242}
s2 = {'name':'Atieh','family':'Jafarzadeh','username':402103206,'password':402103206}

t1 = {'name':'Atieh','family':'Firozeh','username':111,'password':111}
t2 = {'name':'Abdolreza','family':'Rasoli','username':222,'password':222}

c1 = {
    'id':1,
    'name':'programming basics',
    'teacher_name':'Atieh',
    'teacher_family':'Firozeh',
    'year':1404,
    'y':'first',
    'cap':5,
    'curr':'books',
    'session':16,
    'unit':3
}

c2 = {
    'id':2,
    'name':'theory of languages and machines',
    'teacher_name':'Abdolreza',
    'teacher_family':'Rasoli',
    'year':1404,
    'y':'first',
    'cap':5,
    'curr':'PDF',
    'session':16,
    'unit':3
}

students = [s1, s2]
with open('student.json', 'w') as s:
    json.dump(students, s, indent=4)

teachers = [t1, t2]
with open('teacher.json', 'w') as t:
    json.dump(teachers, t, indent=4)

courses = [c1, c2]
with open('course.json', 'w') as c:
    json.dump(courses, c, indent=4)

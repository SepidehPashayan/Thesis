import json

s1 = {'name':'sepideh','family':'pashayan','username':402103242,'password':402103242}
s2 = {'name':'atieh','family':'jafarzadeh','username':402103206,'password':402103206}

t1 = {'name':'atieh','family':'firozeh','username':111,'password':111}
t2 = {'name':'abdolreza','family':'rasoli','username':222,'password':222}

students = [s1,s2]
with open('student.json','w')as s:
    json.dump(students , s , indent=4)

teachers = [t1,t2]
with open('teacher.json','w')as t:
    json.dump(teachers , t , indent=4)
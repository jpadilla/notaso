# Users
from users.models import User
import json
file = open('users.json')
js = json.load(file)
for i in js:
    gender = i['sex']
    if gender:
        gender = gender.upper()
    print i['id']
    u = User(id=i['id'], first_name=i['first_name'], last_name=i['last_name'], gender=gender, facebook_user_id=i['fbid'], is_active=True, is_admin=False, email=i['email'], password="!")
    u.save()


# Professors
from professors.models import Professor
from universities.models import University
from departments.models import Department
from users.models import User
import json
file = open('professors2.json')
js = json.load(file)
for i in js:
    gender = i['sex'].upper()
    names = i['name'].split(" ")
    print names
    if len(names) == 1:
        fname = names[0]
    elif len(names) == 2:
        fname = names[0]
        lname = names[1]
    else:
        if names[0].endswith("."):
            fname = names[0] + " " + names[1]
            if len(names[2]) <= 2 and not names[2] == "de":
                fname += " " + names[2]
                lname = " ".join(names[3:])
            else:
                lname = " ".join(names[2:])
        else:
            fname = names[0]
            if len(names[1]) <= 2:
                fname += " " + names[1]
                lname = " ".join(names[2:])
            else:
                lname = " ".join(names[1:])
    print fname + " - " + lname
    u = Professor(id=i['id'], first_name=fname, last_name=lname, gender=gender, university=University.objects.get(name=i['name']), department=Department.objects.get(id=i['department_id']), created_by=User.objects.get(id=i['created_by']))
    u.save()


# Universities
from universities.models import University
import json

file_university = open('universities_2.json')
js_university = json.load(file_university)

file_university = open('universities/fixtures/universities.json')
js_university_first = json.load(file_university)

for u in js_university:
    for s in js_university_first:
        if s['fields']['name'] == u['name'] and s['fields']['city'] == u['campus']:
            uni = University(
                id = u['id'],
                name = s['fields']['name'],
                city = s['fields']['city'],
                emblem = s['fields']['emblem'],
                slug = s['fields']['slug']
                )
            uni.save()
            print "changed id " + u['id']
        else:
            uni = University(
                id = u['id'],
                name = u['name'],
                city = u['campus'],
                emblem = u['emblem'],
                slug = " "
                )
            uni.save()
            print "created university " + u['id']

from universities.models import University
import json

file_with_slug = open('universities/fixtures/universities.json')
js_with_slug = json.load(file_with_slug)

file_without_slug = open('universities/fixtures/universities_final.json')
js_without_slug = json.load(file_without_slug)

for j in file_without_slug:
    for i in file_with_slug:
        if i['fields']['name'] == j['name'] and i['fields']['city'] == j['campus']:
            uni = University(
                slug = i['fields']['slug']
                )
            uni.save()


# Comments
from professors.models import Professor
from users.models import User
from comments.models import Comment

import json
from datetime import datetime
c = open('comments.json')
comments = json.load(c)
for i in comments:
    user_id = i['user_id']
    if User.objects.filter(id=user_id).count() > 0:
        jd = i['johnDoe']
        if jd == "1":
            jd = True
        else:
            jd = False
    date = datetime.strptime(i['date'],'%Y-%m-%d %H:%M:%S')
    body = i['content']
    if not body:
       body = ""
    responsibility = i['rating_1']
    workload = i['rating_2']
    difficulty = i['rating_3']
    personality = i['rating_4']
    if not responsibility:
        responsibility = 0
    if not workload:
        workload = 0
    if not difficulty:
        difficulty = 0
    if not personality:
        personality = 0
    if Professor.objects.filter(pk=i['professor_id']).count() > 0:    
        comment = Comment(created_by=User.objects.get(id=user_id),professor=Professor.objects.get(pk=i['professor_id']),body = body,created_at=date,is_anonymous = jd,responsibility=responsibility,workload = workload,difficulty=difficulty,personality=personality)
        comment.save()
    else:
        print user_id + " - " + i['id'] + " ---- " + "not found"
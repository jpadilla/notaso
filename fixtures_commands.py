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


from professors.models import Professor
from universities.models import University
from departments.models import Department
from users.models import User
import json

file_professor = open('professors2.json')
js_professor= json.load(file_professor)

file = open('universities/fixtures/universities.json')
js = json.load(file)

file_university = open('webappli_notaso.json')
js_university = json.load(file_university)

...
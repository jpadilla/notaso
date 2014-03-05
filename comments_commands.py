from professors.models import Professor
from users.models import User
from comments.models import Comment

import json
from datetime import datetime
u = open('users.json')
c = open('webappli_notaso.json')
users = json.load(u)
comments = json.load(c)
for i in comments:
     user_id = i['user_id']
     for j in users:
        if user_id == j['fields']['notaso_user_id']:
            email = j['fields']['email']
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
                comment = Comment(created_by=User.objects.get(email=email),professor=Professor.objects.get(pk=i['professor_id']),body = body,created_at=date,is_anonymous = jd,responsibility=responsibility,workload = workload,difficulty=difficulty,personality=personality)
                comment.save()
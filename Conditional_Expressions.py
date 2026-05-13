from rest_framework.fields import BooleanField
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import F, Q, Case, When
from django.db.models import Value

course = Course.objects.annotate(
    is_python = Case(
        When(tags__name='python', then=True),
        default=False,
    )
)
print(course.values('title', 'is_python'))
#<QuerySet [
    # {'title': 'Django for Beginners', 'is_python': True}, 
    # {'title': 'Django for Beginners', 'is_python': False}, 
    # {'title': 'Django for Beginners', 'is_python': False}, 
    # {'title': 'REST APIs with Django', 'is_python': True}, 
    # {'title': 'REST APIs with Django', 'is_python': False},
    # {'title': 'REST APIs with Django', 'is_python': False}, 
    # {'title': 'Docker & DevOps', 'is_python': False}, 
    # {'title': 'Docker & DevOps', 'is_python': False}]>
    
course = Course.objects.annotate(
    tag = Case(
        When(tags__name='python', then=Value('python')),
        When(tags__name='beginner', then=Value('beginner')),
        When(tags__name='django', then=Value('django')),
        default=Value('null'),
    )
)
print(course.values('title', 'tag'))
#<QuerySet [
    # {'title': 'Django for Beginners', 'tag': 'python'}, 
    # {'title': 'Django for Beginners', 'tag': 'django'}, 
    # {'title': 'Django for Beginners', 'tag': 'beginner'}, 
    # {'title': 'REST APIs with Django', 'tag': 'python'}, 
    # {'title': 'REST APIs with Django', 'tag': 'django'}, 
    # {'title': 'REST APIs with Django', 'tag': 'null'}, 
    # {'title': 'Docker & DevOps', 'tag': 'null'}, 
    # {'title': 'Docker & DevOps', 'tag': 'null'}]>



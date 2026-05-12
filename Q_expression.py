import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import F, Q

student = Student.objects.filter(
    Q(name__startswith='a') | Q(name__startswith='c') & Q(name__endswith='s')
)
print(student.values('name'))
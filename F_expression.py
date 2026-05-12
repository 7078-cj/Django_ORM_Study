import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import F

# course = Course.objects.all().first()
# course.price = F('price') + 1
# course.save()

Course.objects.update(price=F('price') + 1)
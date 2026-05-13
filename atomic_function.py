import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import Prefetch, Count, Avg, Min, Max, Sum, CharField, Value, Subquery, OuterRef, Exists
from django.db.models.functions import Upper,Length,Concat
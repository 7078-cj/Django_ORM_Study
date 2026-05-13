import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import Prefetch, Count, Avg, Min, Max, Sum, CharField, Value, Subquery, OuterRef, Exists
from django.db.models.functions import Upper,Length,Concat

tag = Tag.objects.filter(name__in=['python','django'])

courses = Course.objects.filter(tags__in=Subquery(tag.values('pk')))
print(courses)

coursess = Course.objects.all()
tag_outer = Tag.objects.filter(courses=OuterRef('pk'))


coursess = coursess.annotate(
    tagss=Subquery(tag_outer.values('name'))
)
print(coursess.values('title','tagss'))
#it only gets the first tag
#<QuerySet [
    # {'title': 'Django for Beginners', 'tagss': 'python'}, 
    # {'title': 'REST APIs with Django', 'tagss': 'python'}, 
    # {'title': 'Docker & DevOps', 'tagss': 'docker'}]>

# latest_lesson = Lesson.objects.filter(
#     course=OuterRef('pk')
# ).order_by('-created_at')

# course_lesson = Course.objects.annotate(
#     latest_lesson_title=Subquery(latest_lesson.values('title')[:1])
# )
# #latest lesson per course
# print(course_lesson)

#Avoid N+1 queries (advanced filtering)
python_tag = Course.objects.filter(
    pk__in=Subquery(
        Tag.objects.filter(name='python').values('courses')
    )
)
#filter courses that have a “python” tag
print(python_tag)


python_tag = Tag.objects.filter(
    courses=OuterRef('pk'),
    name='python'
)

python_course_exists = Course.objects.annotate(
    has_python=Exists(python_tag)
)
print(python_course_exists.values('title','has_python'))

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson

all_students = Student.objects.all()
print(all_students)

course_student = Course.objects.filter(students__name="Carol Reyes")
print(course_student)
# <QuerySet [<Course: Django for Beginners>, 
# <Course: REST APIs with Django>, <Course: Docker & DevOps>]>
#this show course that has Carol Reyes as student

course_student_w_d = Course.objects.filter(students__name="Carol Reyes", title__startswith="d")
print(course_student_w_d)
# <QuerySet [<Course: Django for Beginners>, <Course: Docker & DevOps>]>

#finding multiple students in th course
students = ["Bob Cruz", "Carol Reyes"]
course_students = Course.objects.filter(students__name__in=students)
print(course_students)
# <QuerySet [<Course: Django for Beginners>, 
# <Course: Django for Beginners>, 
# <Course: REST APIs with Django>, 
# <Course: REST APIs with Django>, 
# <Course: Docker & DevOps>]>

course_wo_students = Course.objects.exclude(title__startswith="d")
print(course_wo_students)
# <QuerySet [<Course: REST APIs with Django>]>

students_lt_e = Student.objects.filter(name__lt="e")
print(students_lt_e)
# <QuerySet [<Student: Alice Santos>, <Student: Bob Cruz>, <Student: Carol Reyes>]>

students_gt_B = Student.objects.filter(name__gt="B")
print(students_gt_B)
# <QuerySet [<Student: Bob Cruz>, <Student: Carol Reyes>]>

course_price_range = Course.objects.filter(price__range=(30.00,50.00))
print(course_price_range)
# <QuerySet [<Course: REST APIs with Django>, <Course: Docker & DevOps>]>

students_order_by_name = Student.objects.order_by("name")
print(students_order_by_name)
# <QuerySet [<Student: Alice Santos>, <Student: Bob Cruz>, <Student: Carol Reyes>]>
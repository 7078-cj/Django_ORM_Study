import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import Prefetch, Count, Avg, Min, Max, Sum, CharField, Value
from django.db.models.functions import Upper,Length,Concat

studnt = Student.objects.values('name')
print(studnt)
# <QuerySet [
    # {'name': 'Alice Santos'}, 
    # {'name': 'Bob Cruz'}, 
    # {'name': 'Carol Reyes'}
    # ]>
    
upper_tudnt = Student.objects.values(name_upper=Upper('name'))
print(upper_tudnt)
#<QuerySet [
    # {'name_upper': 'ALICE SANTOS'}, 
    # {'name_upper': 'BOB CRUZ'}, 
    # {'name_upper': 'CAROL REYES'}]>
    
course = Course.objects.filter(title__startswith='d').values('title', 'students__name')
print(course)
#<QuerySet [
    # {'title': 'Django for Beginners', 'students__name': 'Alice Santos'}, 
    # {'title': 'Django for Beginners', 'students__name': 'Bob Cruz'}, 
    # {'title': 'Django for Beginners', 'students__name': 'Carol Reyes'}, 
    # {'title': 'Docker & DevOps', 'students__name': 'Alice Santos'}, 
    # {'title': 'Docker & DevOps', 'students__name': 'Carol Reyes'}]>

course_list = Course.objects.values_list('title')
print(course_list)
# <QuerySet [
    # ('Django for Beginners',), 
    # ('REST APIs with Django',), 
    # ('Docker & DevOps',)]>
    
count_of_id = Course.objects.aggregate(Count('id'))
print(count_of_id)
#{'id__count': 3}

count_of_id_total = Course.objects.aggregate(total=Count('id'))
print(count_of_id_total)
#{'total': 3}

count_of_price_avg= Course.objects.aggregate(avg=Avg('price'))
print(count_of_price_avg)
#{'avg': Decimal('39.9900000000000')}

count_of_price_avg_d= Course.objects.filter(title__startswith='d').aggregate(avg=Avg('price'))
print(count_of_price_avg_d)
#{'avg': Decimal('34.9900000000000')}

count_of_price_min= Course.objects.aggregate(min=Min('price'))
print(count_of_price_min)
#{'min': Decimal('29.9900000000000')}

count_of_price_max= Course.objects.aggregate(max=Max('price'))
print(count_of_price_max)
#{'max': Decimal('49.9900000000000')}

count_of_price_sum= Course.objects.aggregate(sum=Sum('price'))
print(count_of_price_sum)
#{'sum': Decimal('119.970000000000')}

count_of_price_sum_min_max= Course.objects.aggregate(sum=Sum('price'),
                                                    max=Max('price'),
                                                    min=Min('price'))
print(count_of_price_sum_min_max)
#{'sum': Decimal('119.970000000000'), 
# 'max': Decimal('49.9900000000000'), 
# 'min': Decimal('29.9900000000000')}

course_annotate = Course.objects.annotate(len_title=Length('title'))
print(course_annotate.values('title','len_title'))
#<QuerySet [
    # {'title': 'Django for Beginners', 'len_title': 20}, 
    # {'title': 'REST APIs with Django', 'len_title': 21}, 
    # {'title': 'Docker & DevOps', 'len_title': 15}]>
    
course_annotate_filter = Course.objects.annotate(len_title=Length('title')).filter(title__startswith='d')
print(course_annotate_filter.values('title','len_title'))
#<QuerySet [
    # {'title': 'Django for Beginners', 'len_title': 20}, 
    # {'title': 'Docker & DevOps', 'len_title': 15}]>
    
concatenation = Concat(
    'name',
    Value('[Total Course Price: '), Sum('courses__price'), Value(']'),
    output_field=CharField()
)

students_w_concatenation = Student.objects.annotate(total=concatenation, num_of_courses=Count('courses'))
print(students_w_concatenation.values('name', 'total','num_of_courses'))
#<QuerySet [
    # {'name': 'Alice Santos', 'total': 'Alice Santos[Total Course Price: 69.98]', 'num_of_courses': 2}, 
    # {'name': 'Bob Cruz', 'total': 'Bob Cruz[Total Course Price: 79.98]', 'num_of_courses': 2}, 
    # {'name': 'Carol Reyes', 'total': 'Carol Reyes[Total Course Price: 119.97]', 'num_of_courses': 3}]>


sold = students_w_concatenation = Student.objects.annotate(total=Sum('courses__price'))
total_sales_courses = sold.aggregate(total_sales=Sum('total'))
print(total_sales_courses.values())
#dict_values([Decimal('269.930000000000')])

import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson
from django.db.models import Prefetch


def measure(queryset, label):
    import time
    start = time.perf_counter()
    result = list(queryset)
    end = time.perf_counter()
    print(f"{label}: {end - start:.6f}s -> {result}")
    return result

def measure_with_access(queryset, label):
    import time
    start = time.perf_counter()

    result = []
    for s in queryset:
        courses = list(s.courses.all())
        lessons = [list(c.lessons.all()) for c in courses]
        result.append((s, courses, lessons))

    end = time.perf_counter()
    print(f"{label}: {end - start:.6f}s")
    return result

def measure_with_access_selectrelated(queryset, label):
    import time
    start = time.perf_counter()

    result = []
    for x in queryset:
        y = x.category
        result.append((x, y))

    end = time.perf_counter()
    print(f"{label}: {end - start:.6f}s")
    return result

measure_with_access(
    Student.objects.all(),
    "student_wo_prefetch"
)

measure_with_access(
    Student.objects.prefetch_related("courses","courses__lessons"),
    "student_w_prefetch"
)

# student_wo_prefetch: 0.016186s
# student_w_prefetch: 0.006360s

measure_with_access_selectrelated(
    Course.objects.all(),
    "course_wo_selectrelated"
)

measure_with_access_selectrelated(
    Course.objects.select_related("category"),
    "course_w_selectrelated"
)

# course_wo_selectrelated: 0.003253s
# course_w_selectrelated: 0.002579s

measure_with_access(
    Student.objects.all(),
    "student_wo_prefetch"
)

measure_with_access(
    Student.objects.prefetch_related(
        Prefetch(
            "courses",
            queryset=Course.objects.prefetch_related("lessons")#this pre fetches the lessons related in the courses
        )#this prefetch the Object Course relates in Student
    ),#this prefetches the courses related to the student,
    "student_w_prefetch"
)

# student_wo_prefetch: 0.013622s
# student_w_prefetch: 0.003585s

measure_with_access(
    Student.objects.all(),
    "student_wo_prefetch"
)

measure_with_access(
    Student.objects.select_related(
        # only works if Student had FK/OneToOne fields (yours doesn't here)
    ).prefetch_related(
        Prefetch(
            "courses",
            queryset=Course.objects.select_related("category").prefetch_related("lessons")
        )
    ),#this prefetches the courses related to the student,
    "student_w_prefetch_select_related"
)

# student_wo_prefetch:               0.016383s
# student_w_prefetch:                0.006252s
# student_wo_prefetch:               0.017116s
# student_w_prefetch_select_related: 0.004800s
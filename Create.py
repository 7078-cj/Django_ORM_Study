import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Student, Profile, Category, Tag, Course, Lesson

# ── Categories ──
web = Category.objects.create(name="Web Development")
data_sci = Category.objects.create(name="Data Science")
devops = Category.objects.create(name="DevOps")

# ── Tags ──
python = Tag.objects.create(name="python")
django_tag = Tag.objects.create(name="django")
docker = Tag.objects.create(name="docker")
sql = Tag.objects.create(name="sql")
beginner = Tag.objects.create(name="beginner")
advanced = Tag.objects.create(name="advanced")

# ── Students & Profiles (One-to-One) ──
alice = Student.objects.create(name="Alice Santos", email="alice@mail.com")
Profile.objects.create(student=alice, bio="Hi I'm Alice!")

bob = Student.objects.create(name="Bob Cruz", email="bob@mail.com")
Profile.objects.create(student=bob, bio="Hi I'm Bob!")

carol = Student.objects.create(name="Carol Reyes", email="carol@mail.com")
Profile.objects.create(student=carol, bio="Hi I'm Carol!")

# ── Courses (One-to-Many with Category) ──
django_course = Course.objects.create(
    title="Django for Beginners",
    category=web,
    description="Learn Django from scratch.",
    price=29.99
)

api_course = Course.objects.create(
    title="REST APIs with Django",
    category=web,
    description="Build production-ready APIs.",
    price=49.99
)

docker_course = Course.objects.create(
    title="Docker & DevOps",
    category=devops,
    description="Containerize and deploy apps.",
    price=39.99
)

# ── Lessons (One-to-Many with Course) ──
Lesson.objects.create(course=django_course, title="Intro to Django",     duration_minutes=15, order=1)
Lesson.objects.create(course=django_course, title="Models & Migrations", duration_minutes=30, order=2)
Lesson.objects.create(course=django_course, title="Views & Templates",   duration_minutes=25, order=3)

Lesson.objects.create(course=api_course, title="DRF Setup",          duration_minutes=20, order=1)
Lesson.objects.create(course=api_course, title="Serializers",        duration_minutes=35, order=2)
Lesson.objects.create(course=api_course, title="Auth & Permissions", duration_minutes=45, order=3)

Lesson.objects.create(course=docker_course, title="Intro to Docker",  duration_minutes=20, order=1)
Lesson.objects.create(course=docker_course, title="Docker Compose",   duration_minutes=30, order=2)
Lesson.objects.create(course=docker_course, title="CI/CD Pipelines",  duration_minutes=50, order=3)

# ── Many-to-Many: Tags ──
django_course.tags.add(python, django_tag, beginner)
api_course.tags.add(python, django_tag, advanced)
docker_course.tags.add(docker, advanced)

# ── Many-to-Many: Students ──
django_course.students.add(alice, bob, carol)
api_course.students.add(bob, carol)
docker_course.students.add(alice, carol)

print("✅ Done!")
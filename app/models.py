from django.db import models

# Create your models here.
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# ──────────────────────────────────────────
# One-to-One: Each Student has one Profile
# ──────────────────────────────────────────
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name}'s Profile"


# ──────────────────────────────────────────
# One-to-Many: One Course has many Lessons
# ──────────────────────────────────────────
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="courses")
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Many-to-Many: Course has many Tags, Tag has many Courses
    tags = models.ManyToManyField(Tag, related_name="courses", blank=True)

    # Many-to-Many: Course has many Students, Student has many Courses
    students = models.ManyToManyField(Student, related_name="courses", blank=True)

    comments = GenericRelation("Comment")

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    duration_minutes = models.PositiveIntegerField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    number_in_stock = models.PositiveSmallIntegerField()
    
    comments = GenericRelation("Comment")

    def __str__(self):
        return self.name
    
class OutOfStockProduct(Product):
    class Meta:
        proxy = True
    
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(number_in_stock__lte=0)
    
    def save(self, *args, **kwargs):
        if self._state.adding:
            self.number_in_stock = 0
        
        super().save(*args, **kwargs)
        
    objects = Manager()
    


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    number_of_items = models.PositiveSmallIntegerField()
    
class Comment(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveSmallIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
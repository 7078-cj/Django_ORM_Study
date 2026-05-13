import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from django.contrib.contenttypes.models import ContentType
from app.models import Course, Product, Comment

course = Course.objects.first()
product = Product.objects.first()

course_ct = ContentType.objects.get_for_model(Course)

# comment1 = Comment.objects.create(
#     text="This course is excellent!",
#     content_type=course_ct,
#     object_id=course.id
# )

product_ct = ContentType.objects.get_for_model(Product)

# comment2 = Comment.objects.create(
#     text="Great product quality!",
#     content_type=product_ct,
#     object_id=product.id
# )

# comments_for_course = Comment.objects.filter(
#     content_type=course_ct,
#     object_id=course.id
# )

comments_for_course = course.comments.all() #with generic relation
print(comments_for_course.values())
#<QuerySet [
    # {'id': 1, 'text': 'This course is excellent!','content_type_id': 10, 'object_id': 1}, 
    # {'id': 3, 'text': 'This course is excellent!', 'content_type_id': 10, 'object_id': 1}, 
    # {'id': 5, 'text': 'This course is excellent!', 'content_type_id': 10, 'object_id': 1}]>

# product_for_course = Comment.objects.filter(
#     content_type=product_ct,
#     object_id=product.id
# )

product_for_course = product.comments.all() #with generic relation
print(product_for_course.values())
#<QuerySet [
    # {'id': 2, 'text': 'Great product quality!', 'content_type_id': 13, 'object_id': 1}, 
    # {'id': 4, 'text': 'Great product quality!', 'content_type_id': 13, 'object_id': 1}, 
    # {'id': 6, 'text': 'Great product quality!', 'content_type_id': 13, 'object_id': 1}]>
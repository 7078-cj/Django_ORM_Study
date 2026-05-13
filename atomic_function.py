import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from app.models import Product
from django.db.models import Prefetch, Count, Avg, Min, Max, Sum, CharField, Value, Subquery, OuterRef, Exists
from django.db.models.functions import Upper,Length,Concat
from django.db import transaction

with transaction.atomic():
    product = Product.objects.select_for_update().get(name='Smartphone Stand')
    
    if product.number_in_stock > 0:
        product.number_in_stock -= 1
        product.save()
# What actually happens under the hood
# Transaction starts
# Database finds "Laptop"
# That row is locked (WRITE LOCK)
# Other transactions trying to access it with select_for_update() will wait
# When your block finishes → lock is released

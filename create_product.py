
import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()
from app.models import Product

products_mock = [
    {"name": "Laptop", "number_in_stock": 15},
    {"name": "Mechanical Keyboard", "number_in_stock": 42},
    {"name": "Wireless Mouse", "number_in_stock": 67},
    {"name": "27-inch Monitor", "number_in_stock": 8},
    {"name": "USB-C Hub", "number_in_stock": 25},
    {"name": "External SSD 1TB", "number_in_stock": 12},
    {"name": "Gaming Chair", "number_in_stock": 5},
    {"name": "Webcam HD", "number_in_stock": 30},
    {"name": "Noise Cancelling Headphones", "number_in_stock": 9},
    {"name": "Smartphone Stand", "number_in_stock": 0},  # edge case: out of stock
]

Product.objects.bulk_create([
    Product(**data) for data in products_mock
])
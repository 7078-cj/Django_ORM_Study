import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()


from app.models import Product, OutOfStockProduct

OutOfStockProduct.objects.create(name="speeaker")
print(OutOfStockProduct.objects.all())
#<QuerySet [<OutOfStockProduct: Smartphone Stand>]>
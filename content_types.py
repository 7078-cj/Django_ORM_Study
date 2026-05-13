import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from django.contrib.contenttypes.models import ContentType

content_types = ContentType.objects.all()
print(content_types)
#<QuerySet [
    # <ContentType: Administration | log entry>, 
    # <ContentType: Authentication and Authorization | permission>, 
    # <ContentType: Authentication and Authorization | group>, 
    # <ContentType: Authentication and Authorization | user>, 
    # <ContentType: Content Types | content type>, 
    # <ContentType: Sessions | session>, 
    # <ContentType: App | category>, 
    # <ContentType: App | student>, 
    # <ContentType: App | tag>, 
    # <ContentType: App | course>, 
    # <ContentType: App | lesson>, 
    # <ContentType: App | profile>, 
    # <ContentType: App | product>, 
    # <ContentType: App | order>]>
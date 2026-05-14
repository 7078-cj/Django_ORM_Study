import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OrmStudy.settings")
django.setup()

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D

from app.models import Place


def seed_data():
    print("Seeding data...")

    Place.objects.all().delete()

    places = [
        ("Cafe Makati", "cafe", 121.0244, 14.5500),
        ("Coffee BGC", "cafe", 121.0509, 14.5547),
        ("Restaurant Manila", "restaurant", 120.9842, 14.5995),
        ("Mall of Asia", "mall", 120.9810, 14.5350),
        ("QC Food Hub", "restaurant", 121.0437, 14.6760),
    ]

    for name, category, lng, lat in places:
        Place.objects.create(
            name=name,
            category=category,
            location=Point(lng, lat, srid=4326)  # ✅
        )

    print("Data seeded.\n")


def query_nearby():
    print("Query: Nearby places within 5km\n")

    user_location = Point(121.0244, 14.5500, srid=4326)  # ✅

    qs = Place.objects.annotate(
        distance=Distance("location", user_location)
    ).filter(
        location__distance_lte=(user_location, D(km=5))
    ).order_by("distance")

    for p in qs:
        print(f"{p.name} - {round(p.distance.km, 2)} km")


def query_nearest():
    print("\nQuery: Top 3 nearest\n")

    user_location = Point(121.0244, 14.5500, srid=4326)  # ✅

    qs = Place.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[:3]

    for p in qs:
        print(f"{p.name} - {round(p.distance.km, 2)} km")


def run():
    seed_data()
    query_nearby()
    query_nearest()


if __name__ == "__main__":
    run()
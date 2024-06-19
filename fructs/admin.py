from django.contrib import admin
from .models import Category, FromCountry, Fructs, Review


admin.site.register(Category)
admin.site.register(FromCountry)
admin.site.register(Fructs)
admin.site.register(Review)
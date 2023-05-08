from django.contrib import admin

from apps.home.models import RealEstate, ImageHome, CategoryHome


admin.site.register(CategoryHome)
admin.site.register(RealEstate)
admin.site.register(ImageHome)
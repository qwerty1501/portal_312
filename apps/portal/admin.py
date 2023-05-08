from django.contrib import admin
from apps.portal.models import Category, Product, BannerOne, BannerTwo, BannerThree, BannerFour, News


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(BannerOne)
admin.site.register(BannerTwo)
admin.site.register(BannerThree)
admin.site.register(BannerFour)
admin.site.register(News)
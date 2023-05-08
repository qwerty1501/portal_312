from django.contrib import admin

from apps.service.models import CategoryService, Service, Comment

 
admin.site.register(CategoryService)
admin.site.register(Service)
admin.site.register(Comment)
from django.contrib import admin

from apps.job.models import CategoryJob, Job


admin.site.register(CategoryJob)
admin.site.register(Job)
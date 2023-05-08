from rest_framework import serializers as s
from apps.job.models import CategoryJob, Job


class CategoryJobSerializer(s.ModelSerializer):
    class Meta:
        model = CategoryJob
        fields = ['logo', 'name', 'id']


class JobSerializer(s.ModelSerializer):
    category_job = CategoryJobSerializer()
    
    class Meta:
        model = Job
        fields = ['category_job', 'name', 'image', 'release_date', 'price', 'description', 'id']
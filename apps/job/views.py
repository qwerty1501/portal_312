from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from apps.job.models import CategoryJob, Job
from apps.job.serializers import CategoryJobSerializer, JobSerializer

# JOB CATEGORY
class CategoryJobListAPIView(ListAPIView):
    queryset = CategoryJob.objects.all()
    serializer_class = CategoryJobSerializer
    
    
class CategoryJobRetrieveAPIView(RetrieveAPIView):
    queryset = CategoryJob.objects.all()
    serializer_class = CategoryJobSerializer
    
# JOB
class JobListAPIView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['name', 'price']
    search_fields = ['name', 'price']
    
    
class JobRetrieveAPIView(RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filter_fields = ['name', 'price']
    search_fields = ['name', 'price']
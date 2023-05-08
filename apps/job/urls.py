from django.urls import path

from apps.job.views import CategoryJobListAPIView, CategoryJobRetrieveAPIView, JobListAPIView, JobRetrieveAPIView


urlpatterns = [
    # Категория
    path("category-job-list", CategoryJobListAPIView.as_view(), name=""),
    path("category-job/<int:pk>/", CategoryJobRetrieveAPIView.as_view(), name=""),
    path("category-job", CategoryJobRetrieveAPIView.as_view(), name=""),
    # Работа
    path("job-list", JobListAPIView.as_view(), name=""),
    path("job/<int:pk>/", JobRetrieveAPIView.as_view(), name=""),
    path("job", JobRetrieveAPIView.as_view(), name=""),
]
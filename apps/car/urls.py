from django.urls import path

from apps.car.views import CategoryRetrieve, CategoryList, CarListCreateAPIView, CarDeleteView,\
    ImageCarListAPIView, ImageCarRetrieveAPIView


urlpatterns = [
    # Категория
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>', CategoryRetrieve.as_view()),
    # Автомобиль
    path("car/", CarListCreateAPIView.as_view(), name=""),
    path("car/delete/<int:pk>/", CarDeleteView.as_view(), name=""),
    # Фото машин
    path("image-car-list", ImageCarListAPIView.as_view(), name=""),
    path("image-car", ImageCarRetrieveAPIView.as_view(), name=""),
    path("image-car/<int:pk>/", ImageCarRetrieveAPIView.as_view(), name="")
]
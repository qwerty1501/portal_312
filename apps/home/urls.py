from django.urls import path

from apps.home.views import CategoryHomeListAPIView, RealEstateListCreateAPIView, RealEstateDeleteView,\
    ImageHomeListAPIView, ImageHomeRetrieveAPIView, CategoryHomeRetriveAPIView, RealEstateUpdateView


urlpatterns = [
    # Категория
    path("category-home-list/", CategoryHomeListAPIView.as_view(), name=""),
    path("category-home-list/<int:pk>/", CategoryHomeRetriveAPIView.as_view(), name=""),
    # Недвижимость
    path("home/", RealEstateListCreateAPIView.as_view(), name=""),
    path("home/update/<int:pk>/", RealEstateUpdateView.as_view(), name=""),
    path("home/delete/<int:pk>/", RealEstateDeleteView.as_view(), name=""),
    # Фото Недвижимость 
    path("image-home-list/", ImageHomeListAPIView.as_view(), name=""),
    path("image-home/", ImageHomeRetrieveAPIView.as_view(), name=""),
    path("image-home/<int:pk>/", ImageHomeRetrieveAPIView.as_view(), name="")
]
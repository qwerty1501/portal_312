from django.urls import path

from apps.portal.views import CategoryListAPIView, CategoryRetrieveAPIView, ProductListAPIView, ProductRetrieveAPIView,\
    ImageProdListAPIView, ImageProdRetrieveAPIView, BannerOneListAPIView, BannerTwoListAPIView,\
    BannerThreeListAPIView, BannerFourListAPIView, NewsListAPIView


urlpatterns = [
    # Категория
    path("category-list", CategoryListAPIView.as_view(), name=""),
    path("category/<int:pk>/", CategoryRetrieveAPIView.as_view(), name=""),
    path("category", CategoryRetrieveAPIView.as_view(), name=""),
    # Автомобиль
    path("product-list", ProductListAPIView.as_view(), name=""),
    path("product", ProductRetrieveAPIView.as_view(), name=""),
    path("product/<int:pk>/", ProductRetrieveAPIView.as_view(), name=""),
    # Фото машин
    path("image-prod-list", ImageProdListAPIView.as_view(), name=""),
    path("image-prod", ImageProdRetrieveAPIView.as_view(), name=""),
    path("image-prod/<int:pk>/", ImageProdRetrieveAPIView.as_view(), name=""),
    # Баннеры
    path("banner-one", BannerOneListAPIView.as_view(), name=""),
    path("banner-one/<int:pk>", BannerOneListAPIView.as_view(), name=""),
    path("banner-two", BannerTwoListAPIView.as_view(), name=""),
    path("banner-two/<int:pk>", BannerTwoListAPIView.as_view(), name=""),
    path("banner-three", BannerThreeListAPIView.as_view(), name=""),
    path("banner-three/<int:pk>", BannerThreeListAPIView.as_view(), name=""),
    path("banner-four", BannerFourListAPIView.as_view(), name=""),
    path("banner-four/<int:pk>", BannerFourListAPIView.as_view(), name=""),
    # Новости
    path("news", NewsListAPIView.as_view(), name=""),
    path("news/<int:pk>", NewsListAPIView.as_view(), name="")
]
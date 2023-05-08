from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls.static import static

from .yasg import urlpatterns as doc_urls
from . import settings
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('administration', AdministrationAPIViewSet)
# router.register('files', FileAPIViewSet)

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('apps.car.urls')),
    path('job/', include('apps.job.urls')),
    path('user/', include('apps.user.urls')),
    path('home/', include('apps.home.urls')),
    path('portal/', include('apps.portal.urls'))
] 

urlpatterns += doc_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
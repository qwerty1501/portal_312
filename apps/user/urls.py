from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.user.views import UserMVS, UserLoginView, ResetPasswordMVS, \
            CustomTokenRefreshView, ShowHideAvatarView, SendMailAPIView, SendMailUserApiView


userPlural = {
    'get': 'list',
    'post': 'create'
}

useSingle = {
    'get': 'retrieve',
    'patch': 'update'
}

useSingle2 = {
    'get': 'retrieve',
    'post': 'create',
}

useSingle3 = {
    'get': 'retrieve',
    'patch': 'update',
    'post': 'create',
    'delete': 'destroy'
}

urlpatterns = [
    path('', UserMVS.as_view(userPlural)),
    path('<uuid:uniqueId>/', UserMVS.as_view(useSingle)),

    path('login/', UserLoginView.as_view()),
    path('check/', CustomTokenRefreshView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('reset-password/', ResetPasswordMVS.as_view({'post': 'create'})),
    path('reset-password/<uuid:resetPasswordUUID>/', ResetPasswordMVS.as_view({'get': 'retrieve', 'patch': 'update'})),
    path('send-mail-message/',  SendMailAPIView.as_view()),
    path('send-mail-order/', SendMailUserApiView.as_view()),
    path('avatar-flip/<uuid:uniqueId>/', ShowHideAvatarView.as_view()),
]

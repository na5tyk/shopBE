from django.contrib import admin
from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .viewsets import UserAddressViewSet, RegisterViewSet

router = DefaultRouter()
router.register(r'user_address', UserAddressViewSet, basename='user_address')

urlpatterns = [
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^register/$', RegisterViewSet.as_view({ 'post': 'create' }), name='register'),
    url(r'', include(router.urls)),
]

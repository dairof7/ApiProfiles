from django.conf.urls import url
from django.urls import path
from .views import *
from django.urls import path, include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('test_viewset', TestViewSet, basename='test_viewset')
router.register('profile', Profile)

app_name = 'profiles_api'
urlpatterns = [
    path('get_users/', GetUsers.as_view(), name='get all users'),
    path('', include(router.urls))
]
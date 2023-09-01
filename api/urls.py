from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi',views.StudentAPI, basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace='log_in_out')),
    # path('gettoken/',obtain_auth_token),  # used in CLI token generator
]

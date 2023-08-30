from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

#creating a router object
router = DefaultRouter()

#register student viewset with router
router.register('studentapi',views.StudentAPI,basename='student')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls', namespace = 'log_in')), # To create log in and log out prompt
]

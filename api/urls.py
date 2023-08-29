from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

#creating a router object
router = DefaultRouter()

#register student viewset with router
router.register('studentapi',views.StudentAPI,basename='student')

urlpatterns = [
    path('',include(router.urls)),
]

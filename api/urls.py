from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/',views.StudentAPI.as_view()), #used in class view api
]

from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentAPI.as_view()),
    # path('studentapi/<int:pk>/',views.RUDStudentAPI.as_view()),
]

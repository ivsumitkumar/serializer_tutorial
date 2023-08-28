from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/',views.studentapi),
    path('studentapi/<int:pk>',views.studentapi),
]

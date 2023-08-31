from django.urls import path, include
from . import views

urlpatterns = [
    path('studentapi/',views.studentapi),
    path('studentapi/<int:pk>',views.studentapi),
    # path('auth/',include('rest_framework.urls', namespace='log_in_out')),
]

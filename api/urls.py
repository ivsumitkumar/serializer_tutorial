from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from api.auth import CustomToken
urlpatterns = [
    path('studentapi/',views.studentapi),
    path('studentapi/<int:pk>',views.studentapi),
    path('auth/',include('rest_framework.urls', namespace='log_in_out')),
    # path('gettoken/',obtain_auth_token),  # used in CLI token generator
    path('gettoken/',CustomToken.as_view()),
]

from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('studentapi/',views.StudentAPI.as_view()), #used in class view api
    path('gettoken/',TokenObtainPairView.as_view(),name='get_token'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verify_token'),
]

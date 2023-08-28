from django.urls import path,include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

#creating a router
router = DefaultRouter()

#Register Student Viewse with Router
router.register('studentapi',views.StudentModelViewSet,basename='student')


urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='get_token'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh_token'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verify_token'),
]

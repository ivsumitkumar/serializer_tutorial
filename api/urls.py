from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerAPI, basename='singer')
router.register('song', views.SongAPI, basename='song')


urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='log_in_out')),
]

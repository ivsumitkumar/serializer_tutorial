from django.urls import path, include
from api import views


urlpatterns = [
    path('', views.StudentList.as_view()),
    path('auth/',include('rest_framework.urls',namespace='log_in_out')),
    # path('studentcreate/',views.StudentCreate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentRetrieve.as_view()),
    # path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
    # path('studentapi/<int:pk>/',views.StudentDestroy.as_view()),
]


# from django.urls import include
# from rest_framework.routers import DefaultRouter


# Used in custom and UserRatedThrottle
# router = DefaultRouter()
# router.register('studentapi',views.StudentAPI, basename='student')

# urlpatterns = [
#     path('',include(router.urls)),
#     path('auth/',include('rest_framework.urls', namespace='log_in_out')),
# ]

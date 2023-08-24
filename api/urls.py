from django.urls import path
from . import views

urlpatterns = [
    path('<int:x>',views.student_detail,name='student_detail'),
    path('',views.all_student,name='student_list'),
    path('studentapi/',views.student_api,name='student_api'),
]

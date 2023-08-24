from django.urls import path
from . import views

urlpatterns = [
    path('stucreate/',views.Student_create,name='student_create'),
    path('<int:x>',views.student_detail,name='student_detail'),
    path('',views.all_student,name='student_list'),
]

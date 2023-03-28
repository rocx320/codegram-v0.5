from django.urls import path
from . import views

urlpatterns = [
    path('student/signup/', views.student_signup, name='student_signup'),
    path('recruiter/signup/', views.recruiter_signup, name='recruiter_signup'),

]
    
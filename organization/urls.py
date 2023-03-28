from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    #path('student/signup/', views.student_signup, name='student_signup'),
    path('recruiter/signup/', views.recruiter_signup, name='recruiter_signup'),
    path('login/', auth_view.LoginView.as_view(), name = 'login'),
    

]
    
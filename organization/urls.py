from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('student/signup/', views.student_signup, name='student_signup'),
    path('recruiter/signup/', views.recruiter_signup, name='recruiter_signup'),
    path('recruiter/login/', auth_views.LoginView.as_view(template_name = "login.html",redirect_authenticated_user=True), name='log-in'),
    

]
    
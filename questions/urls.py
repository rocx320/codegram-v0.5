from django.urls import path
from . import views


urlpatterns = [
    #CRUD Functions
    path('', views.QuestionListView.as_view(), name ="questions")
    
]

from django.shortcuts import render
from django.views.generic import ListView
from .models import Question
# Create your views here.

def home(request):
    return render(request,'index.html')


#CRUD
 
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
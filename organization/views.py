from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import StudentSignupForm, RecruiterSignupForm
from .models import Student, Recruiter
from django.contrib.auth import views as auth_views
'''
def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST)
        if form.is_valid():
            # create a new user
            user = form.save(commit=False)
            user.is_student = True
            user.save()

            # create a new student
            student = Student.objects.create(user=user)

            # log in the user and redirect to the home page
            login(request, user)
            return redirect('login')
    else:
        form = StudentSignupForm()
    return render(request, 'student_signup.html', {'form': form})
    '''

def recruiter_signup(request):
    if request.method == 'POST':
        form = RecruiterSignupForm(request.POST)
        if form.is_valid():
            # create a new user
            user = form.save(commit=False) 
            user.is_recruiter = True
            user.save()

            # create a new recruiter
            recruiter = Recruiter.objects.create(user=user, company_email=form.cleaned_data.get('company_email'), company_name=form.cleaned_data.get('company_name'))

                
            # log in the user and redirect to the home page
            login(request, user)
            return redirect('login')
    else:
        form = RecruiterSignupForm()
    return render(request, 'recruiter_signup.html', {'form': form})

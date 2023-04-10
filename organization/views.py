from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import StudentSignupForm, RecruiterSignupForm
from .models import Student, Recruiter
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

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
            return redirect('login.html')
    else:
        form = RecruiterSignupForm()
    return render(request, 'recruiter_signup.html', {'form': form})


def recruiter_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active and user.is_recruiter:
                login(request, user)
                messages.success(request, 'Login successfull')
                print("Successfully logged in")
                return redirect('index1.html')
            else:
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request, 'index1.html')


def index1(request):
    user = request.user
    all_users = User.objects.all()
    follow_status = Follow.objects.filter(following=user, follower=request.user).exists()

    profile = Profile.objects.all()

    posts = Stream.objects.filter(user=user)
    group_ids = []

    
    for post in posts:
        group_ids.append(post.post_id)
        
    post_items = Post.objects.filter(id__in=group_ids).all().order_by('-posted')

    query = request.GET.get('q')
    if query:
        users = User.objects.filter(Q(username__icontains=query))

        paginator = Paginator(users, 6)
        page_number = request.GET.get('page')
        users_paginator = paginator.get_page(page_number)


    context = {
        'post_items': post_items,
        'follow_status': follow_status,
        'profile': profile,
        'all_users': all_users,
        # 'users_paginator': users_paginator,
    }
    return render(request, 'index1.html', context)
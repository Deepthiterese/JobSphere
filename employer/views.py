from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from portal.models import Job
from portal.forms import JobForm

def employer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('employer_login')
    return render(request, 'employer_register.html')

def employer_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('employer_dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'employer_login.html')


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('employer_dashboard')
    else:
        form = JobForm()

   
    jobs = Job.objects.filter(posted_by=request.user).order_by('-posted_at')

    return render(request, 'dashboard.html', {'form': form, 'jobs': jobs})

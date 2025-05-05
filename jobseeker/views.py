from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from portal.models import Job, Application
from portal.forms import ApplicationForm
import requests
from django.core.paginator import Paginator
from django.utils.html import strip_tags


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'jobseeker_register.html', {'error': 'Username already exists'})
        
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('jobseeker_home')

    return render(request, 'jobseeker_register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('jobseeker_home')
        else:
            return render(request, 'jobseeker_login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'jobseeker_login.html')


def logout_view(request):
    logout(request)
    return redirect('jobseeker_login')



@login_required
def home(request):
    location = request.GET.get('location')
    category = request.GET.get('category')
    company = request.GET.get('company')

    local_jobs = Job.objects.all()
    if location:
        local_jobs = local_jobs.filter(location__icontains=location)
    if category:
        local_jobs = local_jobs.filter(category__icontains=category)
    if company:
        local_jobs = local_jobs.filter(company__icontains=company)

    applied_job_ids = Application.objects.filter(applicant=request.user).values_list('job_id', flat=True)

    for job in local_jobs:
        job.applied = job.id in applied_job_ids

    api_jobs = []
    try:
        response = requests.get('https://remoteok.io/api')
        if response.status_code == 200:
            response.encoding = 'utf-8'  
            data = response.json()
            for item in data[1:]:  
                description = item.get('description', '')
                clean_description = strip_tags(description)
                job_data = {
                    'title': item.get('position'),
                    'company': item.get('company'),
                    'location': item.get('location', 'Remote'),
                    'description': clean_description[:150],
                    'url': item.get('url'),
                    'applied': False  
                }
                if location and location.lower() not in job_data['location'].lower():
                    continue
                if company and company.lower() not in job_data['company'].lower():
                    continue
                api_jobs.append(job_data)
    except Exception as e:
        print("API Error:", e)

    # Combine local and API jobs
    all_jobs = list(local_jobs) + api_jobs

    paginator = Paginator(all_jobs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobseeker_home.html', {'page_obj': page_obj})


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('jobseeker_home')
    else:
        form = ApplicationForm()
    return render(request, 'apply.html', {'form': form, 'job': job})


from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    company = models.CharField(max_length=100)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    linkedin = models.URLField(blank=True)
    years_of_experience = models.IntegerField()
    resume = models.FileField(upload_to='')
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.job.title}"

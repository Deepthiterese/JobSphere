from django.contrib import admin
from .models import Job, Application
from django.utils.html import format_html


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'resume_link', 'phone_number', 'years_of_experience')  

    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">View Resume</a>', obj.resume.url)
        return "-"
    resume_link.short_description = 'Resume'

admin.site.register(Job)
admin.site.register(Application)

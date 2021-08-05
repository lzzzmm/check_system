from django.contrib import admin

# Register your models here.
from My_project.models import Sign

class SignAdmin(admin.ModelAdmin):
    list_display = ('my_user', 'sign_status', 'sign_time')
    list_per_page = 30




admin.site.register(Sign, SignAdmin)


from django.contrib import admin
from dut.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'date_created', 'comments']

admin.site.register(Project, ProjectAdmin)

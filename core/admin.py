from django.contrib import admin
from core.models import Project, Courses, Publication

# Register your models here.
admin.site.register(Project)
admin.site.register(Courses)
admin.site.register(Publication)
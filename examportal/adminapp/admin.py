from django.contrib import admin
from . models import Course,Faculty,Admin,Student

admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Faculty)
admin.site.register(Student)

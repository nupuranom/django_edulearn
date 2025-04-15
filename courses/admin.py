from django.contrib import admin
from .models import Course,Lesson,Student
#from django.contrib.auth.models import User
# Register the User model in the admin panel
#admin.site.register(User)

# Register your models here.
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Student)
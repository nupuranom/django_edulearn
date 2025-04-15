# from django.db import models

# # Create your models here.
# #-->inherit je seita bole dite hobe jate bujte pare eita ekat model class  ==>model clSS INHERIT KORTECHE
# class Course(models.Model): 
#     title=models.CharField(max_length=200)
#     description=models.TextField() 
#     duration=models.IntegerField(help_text='Duration in hours')
#     thumbnail=models.ImageField(upload_to='course_thumbnail/',null=True,blank=True)
#     def __str__(self):
#         return self.title+'('+str(self.duration)+')'

# class Lesson(models.Model):
#     title=models.CharField(max_length=200)
#     content=models.TextField()
#     #course is not the class,it's the relation between Course and lession
#     course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
#     #on_delete =cascading option
#     def __str__(self):
#         return self.title
    
# class Student(models.Model):
#     name=models.CharField(max_length=200)
#     email=models.EmailField(unique=True)
#     enrolled_courses=models.ManyToManyField(Course,related_name='students')
#     def __str__(self):
#         return self.name

from django.db import models

class Course(models. Model):
    title = models. CharField(max_length = 200)
    description = models. TextField()
    duration = models.IntegerField(help_text = "Duration in hours")
    thumbnail = models.ImageField(upload_to = 'course_thumbnails/', null

    = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Lesson(models. Model):
    course = models. ForeignKey(Course, on_delete= models. CASCADE, related_name = 'lessons')

    title = models. CharField(max_length = 200)
    content = models. TextField()
    video_url = models.URLField(null=True, blank=True)
    completion_status = models.BooleanField(default=False)
    def __str__(self):
        return self.title

class Student(models. Model):
    name = models. CharField(max_length = 200)
    email = models. EmailField(unique = True)
    enrolled_courses = models. ManyToManyField(Course, related_name = 'students')
    completed_lessons = models.ManyToManyField(Lesson, related_name='completed_by', blank=True)

    def __str__(self):
        return self. name
# from django.shortcuts import render
# from .models import Course
# from django.shortcuts import get_object_or_404
# # Create your views here.
# def home(request):
#     courses=Course.objects.all()
    
#     return render(request,'courses/index.html',{'allcourses':courses})  #'allcourses'=value,courses=variable
# def desc(request):
#     return render(request,'courses/desc.html')
# def course_details(request,course_id):
#     course=get_object_or_404(Course,id=course_id)
#     lessons=course.lessons.all()
#     return render(request,'courses/desc.html',{'lessons': lessons,'course':course})


#--------------------------lab 4 extended---------------------

# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Course, Lesson
# from .forms import CourseForm, LessonForm

# # Course List
# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'courses/course_list.html', {'courses': courses})

# # Course Detail
# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     lessons = course.lessons.all()
#     return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

# # Create Course
# def course_create(request):
#     if request.method == "POST":
#         form = CourseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Course created successfully!")
#             return redirect('course_list')
#     else:
#         form = CourseForm()
#     return render(request, 'courses/course_form.html', {'form': form})

# # Update Course
# def course_update(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == "POST":
#         form = CourseForm(request.POST, request.FILES, instance=course)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Course updated successfully!")
#             return redirect('course_list')
#     else:
#         form = CourseForm(instance=course)
#     return render(request, 'courses/course_form.html', {'form': form})

# # Delete Course
# def course_delete(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == "POST":
#         course.delete()
#         messages.success(request, "Course deleted successfully!")
#         return redirect('course_list')
#     return render(request, 'courses/course_confirm_delete.html', {'course': course})
# # Create Lesson
# def lesson_create(request):
#     if request.method == "POST":
#         form = LessonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Lesson created successfully!")
#             return redirect('course_list')
#     else:
#         form = LessonForm()
#     return render(request, 'courses/lesson_form.html', {'form': form})

# # Update Lesson
# def lesson_update(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)

#     if request.method == "POST":
#         form = LessonForm(request.POST, instance=lesson)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Lesson updated successfully!")
#             return redirect('course_list')
#     else:
#         form = LessonForm(instance=lesson)

#     return render(request, 'courses/lesson_form.html', {'form': form})

# # Delete Lesson
# def lesson_delete(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     if request.method == "POST":
#         lesson.delete()
#         messages.success(request, "Lesson deleted successfully!")
#         return redirect('course_list')

#     return render(request, 'courses/lesson_confirm_delete.html', {'lesson': lesson})

#-----------------lab 5------------
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Course, Lesson, Student
# from .forms import CourseForm, LessonForm, CourseEnrollmentForm

# # Course List
# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'courses/course_list.html', {'courses': courses})

# # Course Detail
# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     lessons = course.lessons.all()
#     return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

# # Create Course
# def course_create(request):
#     if request.method == "POST":
#         form = CourseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Course created successfully!")
#             return redirect('course_list')
#     else:
#         form = CourseForm()
#     return render(request, 'courses/course_form.html', {'form': form})

# # Update Course
# def course_update(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == "POST":
#         form = CourseForm(request.POST, request.FILES, instance=course)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Course updated successfully!")
#             return redirect('course_list')
#     else:
#         form = CourseForm(instance=course)
#     return render(request, 'courses/course_form.html', {'form': form})

# # Delete Course
# def course_delete(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == "POST":
#         course.delete()
#         messages.success(request, "Course deleted successfully!")
#         return redirect('course_list')
#     return render(request, 'courses/course_confirm_delete.html', {'course': course})

# # Create Lesson
# def lesson_create(request):
#     if request.method == "POST":
#         form = LessonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Lesson created successfully!")
#             return redirect('course_list')
#     else:
#         form = LessonForm()
#     return render(request, 'courses/lesson_form.html', {'form': form})

# # Update Lesson
# def lesson_update(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)

#     if request.method == "POST":
#         form = LessonForm(request.POST, instance=lesson)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Lesson updated successfully!")
#             return redirect('course_list')
#     else:
#         form = LessonForm(instance=lesson)

#     return render(request, 'courses/lesson_form.html', {'form': form})

# # Delete Lesson
# def lesson_delete(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     if request.method == "POST":
#         lesson.delete()
#         messages.success(request, "Lesson deleted successfully!")
#         return redirect('course_list')

#     return render(request, 'courses/lesson_confirm_delete.html', {'lesson': lesson})


# def enroll_student(request):
#     if request.method == 'POST':
#         form = CourseEnrollmentForm(request.POST)
#         if form.is_valid():
#             student_name = form.cleaned_data['student_name']
#             student_email = form.cleaned_data['student_email']
#             course = form.cleaned_data['course']

#             # Check if the student already exists
#             student, created = Student.objects.get_or_create(email=student_email)
#             student.name = student_name  # Ensure the name is saved
#             student.save()

#             # Check if the student is already enrolled in the course
#             if course in student.enrolled_courses.all():
#                 messages.error(request, "You are already registered for this course.")
#             else:
#                 student.enrolled_courses.add(course)
#                 messages.success(request, f"Successfully enrolled in {course.title}!")

#             return redirect('enroll_student')  # Redirect to the same page

#     else:
#         form = CourseEnrollmentForm()

#     return render(request, 'courses/enroll_student.html', {'form': form})


# def student_list(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     students = course.students.all()  # Fetch all students enrolled in the course
#     return render(request, 'courses/student_list.html', {'course': course, 'students': students})

#--------------lab 6-------------
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from .models import Course, Lesson, Student
# from .forms import CourseForm, LessonForm, CourseEnrollmentForm

# # Authentication Views
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful!")
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'courses/register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             messages.success(request, "Login successful!")
#             return redirect('/')
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
#     return render(request, 'courses/login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     messages.success(request, "You have been logged out.")
#     return redirect('/')

# # Course List
# def course_list(request):
#     courses = Course.objects.all()
#     return render(request, 'courses/course_list.html', {'courses': courses})

# # Course Detail
# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     lessons = course.lessons.all()
#     return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

# # Create Course
# @login_required
# def course_create(request):
#     if request.method == "POST":
#         form = CourseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Course created successfully!")
#             return redirect('course_list')
#     else:
#         form = CourseForm()
#     return render(request, 'courses/course_form.html', {'form': form})

# # Update Course
# @login_required
# def course_update(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == "POST":
#         form = CourseForm(request.POST, request.FILES, instance=course)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Course updated successfully!")
#             return redirect('course_list')
#     else:
#         form = CourseForm(instance=course)
#     return render(request, 'courses/course_form.html', {'form': form})

# # Delete Course
# @login_required
# def course_delete(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     if request.method == "POST":
#         course.delete()
#         messages.success(request, "Course deleted successfully!")
#         return redirect('course_list')
#     return render(request, 'courses/course_confirm_delete.html', {'course': course})

# # Create Lesson
# @login_required
# def lesson_create(request):
#     if request.method == "POST":
#         form = LessonForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Lesson created successfully!")
#             return redirect('course_list')
#     else:
#         form = LessonForm()
#     return render(request, 'courses/lesson_form.html', {'form': form})

# # Update Lesson
# @login_required
# def lesson_update(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)

#     if request.method == "POST":
#         form = LessonForm(request.POST, instance=lesson)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Lesson updated successfully!")
#             return redirect('course_list')
#     else:
#         form = LessonForm(instance=lesson)

#     return render(request, 'courses/lesson_form.html', {'form': form})

# # Delete Lesson
# @login_required
# def lesson_delete(request, lesson_id):
#     lesson = get_object_or_404(Lesson, id=lesson_id)
#     if request.method == "POST":
#         lesson.delete()
#         messages.success(request, "Lesson deleted successfully!")
#         return redirect('course_list')

#     return render(request, 'courses/lesson_confirm_delete.html', {'lesson': lesson})

# # Enroll Student
# def enroll_student(request):
#     if request.method == 'POST':
#         form = CourseEnrollmentForm(request.POST)
#         if form.is_valid():
#             student_name = form.cleaned_data['student_name']
#             student_email = form.cleaned_data['student_email']
#             course = form.cleaned_data['course']

#             # Check if the student already exists
#             student, created = Student.objects.get_or_create(email=student_email)
#             student.name = student_name  # Ensure the name is saved
#             student.save()

#             # Check if the student is already enrolled in the course
#             if course in student.enrolled_courses.all():
#                 messages.error(request, "You are already registered for this course.")
#             else:
#                 student.enrolled_courses.add(course)
#                 messages.success(request, f"Successfully enrolled in {course.title}!")

#             return redirect('enroll_student')  # Redirect to the same page

#     else:
#         form = CourseEnrollmentForm()

#     return render(request, 'courses/enroll_student.html', {'form': form})

# # Student List
# def student_list(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     students = course.students.all()  # Fetch all students enrolled in the course
#     return render(request, 'courses/student_list.html', {'course': course, 'students': students})
#---------6----
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Course, Lesson, Student
from .forms import CourseForm, LessonForm, CourseEnrollmentForm, UserUpdateForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CourseSerializer


class EnrollStudentAPI(APIView):
    def post(self, request):
        student_email = request.data.get('email')
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        student, created = Student.objects.get_or_create(email=student_email)
        if course in student.enrolled_courses.all():
            return Response({'message': f'{student.email} is already enrolled in {course.title}'})
        student.enrolled_courses.add(course)
        return Response({'message': f'{student.email} has been enrolled in {course.title}'})
    
    
class CourseListAPI(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetailAPI(APIView):
    def get(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'description', 'duration', 'thumbnail']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')
    
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        context['lessons'] = course.lessons.all()  

        if self.request.user.is_authenticated:
            try:
                student = Student.objects.get(email=self.request.user.email)
                context['student'] = student  
            except Student.DoesNotExist:
                context['student'] = None  
        else:
            context['student'] = None  

        return context



# Homepage after login
def home(request):
    return render(request, 'courses/home.html')  # Ensure this template exists

# Authentication Views
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('course_list')  # Redirects to courses list
    else:
        form = UserCreationForm()
    return render(request, 'courses/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('course_list')  # Redirects to courses list
        else:
            messages.error(request, "Invalid credentials.")
    else:
        form = AuthenticationForm()
    return render(request, 'courses/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')  # Redirect to login page

# Profile Update View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')  # Redirect to the same profile page
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'courses/profile.html', {'form': form})

# Course List
@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

# Course Detail
# def course_detail(request, course_id):
#     course = get_object_or_404(Course, id=course_id)
#     lessons = course.lessons.all()
#     return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = course.lessons.all()

    student = Student.objects.filter(email=request.user.email).first()

    return render(request, 'courses/course_detail.html', {'course': course, 'lessons': lessons, 'student': student})


@login_required
def course_details(request,id):
     course= get_object_or_404(Course,id=id)
     lessons=course.lessons.all()
     return render(request,'courses/course-details.html',{'lessons':lessons})



# Create Course
@login_required
def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully!")
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

# Update Course
@login_required
def course_update(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

# Delete Course
@login_required
def course_delete(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if request.method == "POST":
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect('course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

# Create Lesson
@login_required
def lesson_create(request):
    if request.method == "POST":
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Lesson created successfully!")
            return redirect('course_list')
    else:
        form = LessonForm()
    return render(request, 'courses/lesson_form.html', {'form': form})

# Update Lesson
@login_required
def lesson_update(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)

    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, "Lesson updated successfully!")
            return redirect('course_list')
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'courses/lesson_form.html', {'form': form})

# Delete Lesson
@login_required
def lesson_delete(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    if request.method == "POST":
        lesson.delete()
        messages.success(request, "Lesson deleted successfully!")
        return redirect('course_list')

    return render(request, 'courses/lesson_confirm_delete.html', {'lesson': lesson})

# Enroll Student
def enroll_student(request):
    if request.method == 'POST':
        form = CourseEnrollmentForm(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            student_email = form.cleaned_data['student_email']
            course = form.cleaned_data['course']

            # Check if the student already exists
            student, created = Student.objects.get_or_create(email=student_email)
            student.name = student_name  # Ensure the name is saved
            student.save()

            # Check if the student is already enrolled in the course
            if course in student.enrolled_courses.all():
                messages.error(request, "You are already registered for this course.")
            else:
                student.enrolled_courses.add(course)
                messages.success(request, f"Successfully enrolled in {course.title}!")

            return redirect('enroll_student')  # Redirect to the same page

    else:
        form = CourseEnrollmentForm()

    return render(request, 'courses/enroll_student.html', {'form': form})

# Student List
def student_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()  # Fetch all students enrolled in the course
    return render(request, 'courses/student_list.html', {'course': course, 'students': students})

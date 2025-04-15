# # ---------from django.contrib import admin
# from django.urls import path
# from .views import home,desc,course_details

# urlpatterns = [
#    #----------- path('admin/', admin.site.urls),
#      path('',home,name='home'),
#       path('<int:course_id>/',course_details,name='course_details'),
#      path('desc/',desc,name='desc'),
     
# ]
#----------------------lab 4 extended------------
# from django.urls import path
# from .views import (
#     course_list, course_detail, course_create, course_update, course_delete,
#     lesson_create, lesson_update, lesson_delete
# )

# urlpatterns = [
#     # Course URLs
#     path('', course_list, name='course_list'),
#     path('<int:course_id>/', course_detail, name='course_detail'),
#     path('create/', course_create, name='course_create'),
#     path('<int:course_id>/update/', course_update, name='course_update'),
#     path('<int:course_id>/delete/', course_delete, name='course_delete'),

#     # Lesson URLs
#     path('lesson/create/', lesson_create, name='lesson_create'),
#     path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
#     path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),
# ]


#---------------------lab 5--------------------
# from django.urls import path
# from .views import (
#     course_list, course_detail, course_create, course_update, course_delete,
#     lesson_create, lesson_update, lesson_delete, enroll_student, student_list
# )

# urlpatterns = [
#     # Course URLs
#     path('', course_list, name='course_list'),
#     path('<int:course_id>/', course_detail, name='course_detail'),
#     path('create/', course_create, name='course_create'),
#     path('<int:course_id>/update/', course_update, name='course_update'),
#     path('<int:course_id>/delete/', course_delete, name='course_delete'),

#     # Lesson URLs
#     path('lesson/create/', lesson_create, name='lesson_create'),
#     path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
#     path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),

#     # Student Enrollment URL
#     path('enroll/', enroll_student, name='enroll_student'),
#     path('courses/<int:course_id>/students/', student_list, name='student_list'),

# ]

#lab 5------------------------

# from django.urls import path
# from .views import (
#     course_list, course_detail, course_create, course_update, course_delete,
#     lesson_create, lesson_update, lesson_delete, enroll_student, student_list
# )

# urlpatterns = [
#     # Course URLs
#     path('', course_list, name='course_list'),
#     path('<int:course_id>/', course_detail, name='course_detail'),
#     path('create/', course_create, name='course_create'),
#     path('<int:course_id>/update/', course_update, name='course_update'),
#     path('<int:course_id>/delete/', course_delete, name='course_delete'),

#     # Lesson URLs
#     path('lesson/create/', lesson_create, name='lesson_create'),
#     path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
#     path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),

#     # Student Enrollment URL
#     path('enroll/', enroll_student, name='enroll_student'),
    
#     # Student List URL
#     path('<int:course_id>/students/', student_list, name='student_list'),
# ]
#--------lab 6--------
# from django.urls import path
# from django.contrib.auth import views as auth_views
# from .views import (
#     course_list, course_detail, course_create, course_update, course_delete,
#     lesson_create, lesson_update, lesson_delete, enroll_student, student_list,
#     register, user_login, user_logout, profile # Added profile view
# )

# urlpatterns = [
#     # Authentication URLs
#     path('', course_list, name='course_list'),
#     path('register/', register, name='register'),
#     path('login/', user_login, name='login'),
#     path('logout/', user_logout, name='logout'),

#     # Course URLs
#     path('', course_list, name='course_list'),
#     path('<int:course_id>/', course_detail, name='course_detail'),
#     path('create/', course_create, name='course_create'),
#     path('<int:course_id>/update/', course_update, name='course_update'),
#     path('<int:course_id>/delete/', course_delete, name='course_delete'),

#     # Lesson URLs
#     path('lesson/create/', lesson_create, name='lesson_create'),
#     path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
#     path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),

#     # Student Enrollment URL
#     path('enroll/', enroll_student, name='enroll_student'),
    
#     # Student List URL
#     path('<int:course_id>/students/', student_list, name='student_list'),

#     # Profile URL
#     path('profile/', profile, name='profile'),  # Profile URL

#     # Password Change URLs
#     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='courses/password_change.html'), name='password_change'),
#     path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='courses/password_change_done.html'), name='password_change_done'),

#     # Password Reset URLs
#     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='courses/password_reset.html'), name='password_reset'),
#     path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='courses/password_reset_done.html'), name='password_reset_done'),
#     path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='courses/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='courses/password_reset_complete.html'), name='password_reset_complete'),
# ]

#--------------lab 8-----------
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    course_create, course_update, course_delete,
    lesson_create, lesson_update, lesson_delete, enroll_student, student_list,
    register, user_login, user_logout, profile,
    CourseListView, CourseDetailView, CourseCreateView, CourseListAPI, CourseDetailAPI, EnrollStudentAPI # Only use CBVs for listing and detail
)

urlpatterns = [
    # Authentication URLs
    path('', CourseListView.as_view(), name='course_list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('create/', CourseCreateView.as_view(), name='course_create'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('api/courses/', CourseListAPI.as_view(), name='api_course_list'),
    path('api/courses/<int:pk>/', CourseDetailAPI.as_view(), name='api_course_detail'),
    path('api/enroll/', EnrollStudentAPI.as_view(), name='api_enroll_student'),

    # Course URLs
    path('create/', course_create, name='course_create'),
    path('<int:course_id>/update/', course_update, name='course_update'),
    path('<int:course_id>/delete/', course_delete, name='course_delete'),

    # Lesson URLs
    path('lesson/create/', lesson_create, name='lesson_create'),
    path('lesson/<int:lesson_id>/update/', lesson_update, name='lesson_update'),
    path('lesson/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),

    # Student Enrollment URL
    path('enroll/', enroll_student, name='enroll_student'),
    
    # Student List URL
    path('<int:course_id>/students/', student_list, name='student_list'),

    # Profile URL
    path('profile/', profile, name='profile'),

    # Password Change URLs
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='courses/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='courses/password_change_done.html'), name='password_change_done'),

    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='courses/password_reset.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='courses/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='courses/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='courses/password_reset_complete.html'), name='password_reset_complete'),
]

"""
URL configuration for deptmanagementsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login_view'),
    # path('forum/', forum_view),
    # path('article/', article_view),
    path('add_marks/', add_marks, name='add-marks'),
    path('view_marks/', view_marks, name='view-marks'),
    path('home/', view_home, name='home'),
    path('forum_details/<int:forum_id> ', forum_details, name="forum-details"),
    path('forum_list/', forum_list, name='forum-list'),
    path('add_forum/', add_forum, name='add-forum'),
    path('submit_comment/<int:forum_id>', submit_comment, name='submit-comment'),
    path('add_student/', add_student, name='add-student'),
    path('view_student/', view_student, name='view-student'),
    path('add_complaint/', add_complaint, name='add-complaint'),
    path('complaint_details/<int:complaint_id>', complaint_details, name='complaint-details'),
    path('delete_complaint/<int:complaint_id>', delete_complaint, name='delete-complaint'),
    path('logout/', logout_view, name='logout'),
    path('test/', test, name="test"),
    path('delete_student/<int:student_id>/', delete_student, name='delete_student'),
    path('register_user/', register_user, name="register-user"),
    path('users/', view_users, name='user-list'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),

]

"""
URL configuration for class_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views
from classes import views as classes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.Register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('enrollments/new', classes_views.EnrollmentCreateView.as_view(template_name='classes/enrollment.html'), name='Enrollment Page'),
    #path('enrollments/new', classes_views.class_list, name='Enrollment Page'),
    path('enrollments/', users_views.UserEnrollmentListView.as_view(), name='Enrollment Record'),
    path('enrollments/<int:pk>/delete/', users_views.UserEnrollmentDeleteView.as_view(template_name='users/enrollment_delete.html'), name = 'Enrollment Delete'),
    path('', include('users.urls')),
]
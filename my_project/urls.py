"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from my_project.settings import MEDIA_URL
from users import views as u_views
from django.contrib.auth import views as auth_view

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),

    path('admin_form/',u_views.admin_form,name='admin_form'),
    path('admin_class_form/',u_views.admin_form_class,name='admin_class_form'),
    path('admin_crispy_form/',u_views.admin_crispy_form,name='admin_crispy_form'),

    path('admin_login/', auth_view.LoginView.as_view(template_name= 'users/login.html'), name='admin_login'), # login Url
    path('admin_logout/', auth_view.LogoutView.as_view(template_name= 'users/logout.html'), name='admin_logout'),# log-out url
    path('profile/',u_views.profile,name='profile'),


]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

    


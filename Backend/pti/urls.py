"""pti URL Configuration

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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_view
from django.conf.urls.static import static
from django.conf import settings

from home import views as homeViews
from forum import views as forumViews
from umkm import views as umkmViews

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', homeViews.index, name='home'),
    path('berita/', include('berita.urls')),
    url(r'forum/$', forumViews.index),
    url(r'umkm/$', umkmViews.index),
    # url(r'login/$',homeViews.login),
    url(r'login/$',  auth_view.LoginView.as_view(template_name='home/login.html'), name="login"),
    url(r'logout/$',  auth_view.LogoutView.as_view(template_name='home/logout.html'), name="logout"),
    url(r'register/$',homeViews.register, name='register')
]

"""amol_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls.static import static
from . import views
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('read_blog/<slug:id>/', views.read_blog, name='read_blog'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('search', views.search, name='search'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('bihar_blog_admin_data', views.bihar_blog_admin_data, name='bihar_blog_admin_data'),
    path('upload', views.upload, name="upload"),
    path('about_us', views.about_us, name="about_us"),
    path('logout', views.logout, name="logout"),
    path('profile/<slug:id>', views.profile, name="profile")  
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




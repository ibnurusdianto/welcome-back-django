"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
# jangan lupa import views
from . import views


"""
Jika ingin membuat url lainnya berarti harus menambahkan pathnya di dalam list urlpatterns
dan gunakan modul yang diinginkan
contoh saya membuat url pattern home dan menyimpannya di dalam module
views.py dan function home sesuai dengan url pattern yang dibuat

lalu jangan lupa import semua dari module yang dibuat, contoh saya 
mengimport views
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # contoh membuat url pattern home 
    path('', views.home), # homepage 
    path('about/', views.about), # about page
]

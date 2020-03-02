"""test_django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from nikka.views import first_name, last_name

nikka_patterns =([
    path('first_name', first_name, name='first_name'),
    path('last_name', last_name, name='last_name'),
], 'nikka')

urlpatterns = [
    path('polls/', include('polls.urls'), name='polls'),
    path('admin/', admin.site.urls),
    path('nikka/', include(nikka_patterns)),
]

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
from nikka.views import first_name, last_name, full_name, EntryDetailsView, AuthorDetailsView, BlogDetailsView

nikka_patterns =([
    path('first_name/', first_name, name='first_name'),
    path('last_name/', last_name, name='last_name'),
    path('full_name/', full_name, name='full_name'),
    path('entry_details/<int:pk>', EntryDetailsView.as_view(), name='entry_details'),
    path('author_details/<int:pk>', AuthorDetailsView.as_view(), name='author_details'),
    path('blog_details/<int:pk>', BlogDetailsView.as_view(), name='blog_details'),
], 'nikka')


urlpatterns = [
    path('polls/', include('polls.urls'), name='polls'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('admin/', admin.site.urls),
    path('nikka/', include(nikka_patterns)),
]


"""virginproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from virgin import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('productcategory/<int:id>', views.productcategory),
    path('productsubcategory/<int:id>', views.productsubcategory),
    path('projects/', views.projects),
    path('contact/', views.contact),
    path('blog/', views.blog),
    path('send', views.send),
    path('sendhome', views.sendhome),
    path('blogdetail/<int:id>', views.blogdetail),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

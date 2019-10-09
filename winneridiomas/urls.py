"""winneridiomas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import include, handler404, handler500
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    #Login
    url(r'^login', LoginView.as_view(template_name='site/login.html'), name="Login"),
    url(r'^logout$', LogoutView.as_view(template_name='site/login.html'), name="login"),

    #Pagina Principal
    url(r'^', include('website.urls')),
    url(r'^login', LoginView.as_view(template_name='site/login.html'), name="login"),
    url(r'^logout', LogoutView.as_view(template_name='site/login.html'), name="login"),


    url(r'^/', include('website.urls')),

    #Admin
    url(r'^admin/', admin.site.urls),
    
]

handler404 = 'website.views.error_404'

handler500 = 'website.views.error_500'


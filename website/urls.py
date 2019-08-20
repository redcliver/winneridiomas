from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    url(r'^$', views.paginaPrincipal),
    url(r'^cursos', views.cursos),
]


from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^novo', views.alunoNovo),
    url(r'^editar', views.alunoEdita),
    url(r'^buscar', views.alunoBusca),
]


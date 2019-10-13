from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'^suporte/$', views.suporte),
    url(r'^aluno/$', views.alunoGeral),
    url(r'^aluno/novo', views.alunoNovo),
    url(r'^aluno/buscar', views.alunoBuscar),
    url(r'^aluno/editar', views.alunoEditar),
    url(r'^colaborador/$', views.colaboradorGeral),
    url(r'^colaborador/novo', views.colaboradorNovo),
    url(r'^colaborador/buscar', views.colaboradorBuscar),
    url(r'^colaborador/editar', views.colaboradorEditar),
    url(r'^classe/$', views.classeGeral),
    url(r'^classe/novo', views.classeNovo),
    url(r'^classe/buscar', views.classeBuscar),
    url(r'^classe/editar', views.classeEditar),
]


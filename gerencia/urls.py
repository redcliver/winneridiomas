from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.home),
    url(r'^suporte/$', views.suporte),
    url(r'^aluno/$', views.alunoGeral),
    url(r'^aluno/novo', views.alunoNovo),
    url(r'^aluno/visualizar', views.alunoVisualizar),
    url(r'^aluno/editar', views.alunoEditar),
    url(r'^aluno/salvar', views.alunoSalvar),
    url(r'^colaborador/$', views.colaboradorGeral),
    url(r'^colaborador/novo', views.colaboradorNovo),
    url(r'^colaborador/buscar', views.colaboradorBuscar),
    url(r'^colaborador/editar', views.colaboradorEditar),
    url(r'^classe/$', views.classeGeral),
    url(r'^classe/novo', views.classeNovo),
    url(r'^classe/buscar', views.classeBuscar),
    url(r'^classe/editar', views.classeEditar),
    url(r'^teste/$', views.testeGeral),
    url(r'^teste/novo', views.testeNovo),
]

urlpatterns += static(settings.MEDIA_URL, documento_root=settings.MEDIA_ROOT)

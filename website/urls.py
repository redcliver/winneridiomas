from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.paginaPrincipal),
    url(r'^cursos', views.cursos),
    url(r'^unidades', views.unidades),
    url(r'^nivelamento', views.nivelamento),
    url(r'^contato', views.viewContato),
    url(r'^entrar', views.entrar),
    url(r'^instituicao', views.instituicao),
    url(r'^metodo', views.metodo),
    url(r'^colaboradores', views.colaboradores),
    url(r'^registro', views.viewRegistro),
]


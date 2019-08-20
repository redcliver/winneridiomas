from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.paginaPrincipal),
    url(r'^cursos', views.cursos),
    url(r'^unidades', views.cursos),
    url(r'^nivelamento', views.cursos),
    url(r'^contato', views.cursos),
    url(r'^entrar', views.cursos),
    url(r'^instituicao', views.cursos),
    url(r'^metodo', views.cursos),
    url(r'^colaboradores', views.cursos),
]


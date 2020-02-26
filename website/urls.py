from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.paginaPrincipal),
    url(r'^cursos', views.cursos),
    url(r'^nivelamento', views.nivelamento),
    url(r'^contato', views.viewContato),
    url(r'^entrar', views.entrar),
    url(r'^instituicao', views.instituicao),
    url(r'^metodo', views.metodo),
    url(r'^colaboradores', views.colaboradores),
    url(r'^registro', views.viewRegistro),
    url(r'^parceiros', views.parceiros),
    url(r'^indiqueParceiro', views.indiqueParceiro),
    url(r'^unidades', views.unidades),
    url(r'^tresLagoas', views.tresLagoas),
    url(r'^aguaClara', views.aguaClara),
    url(r'^ribasRioPardo', views.ribasRioPardo),
    url(r'^kids', views.kids),
    url(r'^adult', views.adult),
    url(r'^inCompany', views.inCompany),
    url(r'^business', views.business),
    url(r'^testPreparation', views.testPreparation),
    url(r'^vip', views.vip),
]


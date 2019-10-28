from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.eventoGeral),
    url(r'^novo', views.eventoNovo),
    url(r'^busca', views.upload),
]


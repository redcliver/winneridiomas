from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$', views.eventoGeral),
    url(r'^novo', views.eventoNovo),
    url(r'^busca', views.upload),
]


urlpatterns += static(settings.MEDIA_URL, documento_root=settings.MEDIA_ROOT)

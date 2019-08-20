from django.shortcuts import render

# Create your views here.
def paginaPrincipal(request):
    return render(request, 'site/home.html', {'title': 'Home'})

def cursos(request):
    return render(request, 'site/cursos.html', {'title': 'Cursos'})


def error_404(request, exception):
    return render(request, 'site/404.html', {'title': 'Error'})

def error_500(request):
    return render(request, 'site/500.html', {'title': 'Error'})
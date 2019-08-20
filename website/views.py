from django.shortcuts import render

# Create your views here.
def paginaPrincipal(request):
    return render(request, 'site/home.html', {'title': 'Home'})

def cursos(request):
    return render(request, 'site/cursos.html', {'title': 'Cursos'})

def unidades(request):
    return render(request, 'site/unidades.html', {'title': 'Unidades'})

def nivelamento(request):
    return render(request, 'site/nivelamento.html', {'title': 'Nivelamento'})

def contato(request):
    return render(request, 'site/contato.html', {'title': 'Contato'})

def entrar(request):
    return render(request, 'site/login.html', {'title': 'Entrar'})

def instituicao(request):
    return render(request, 'site/instituicao.html', {'title': 'Instituicao'})

def metodo(request):
    return render(request, 'site/metodo.html', {'title': 'Metodo'})

def colaboradores(request):
    return render(request, 'site/colaboradores.html', {'title': 'Colaboradores'})




def error_404(request, exception):
    return render(request, 'site/404.html', {'title': 'Error'})

def error_500(request):
    return render(request, 'site/500.html', {'title': 'Error'})
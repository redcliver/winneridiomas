from django.shortcuts import render

# Create your views here.
def paginaPrincipal(request):
    return render(request, 'site/home.html', {'title':'Home'})

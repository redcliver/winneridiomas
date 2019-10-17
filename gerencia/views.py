from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/home.html', {'title':'Home', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})
    
def suporte(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/suporte.html', {'title':'Suporte', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoGeral(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/aluno/home.html', {'title':'Aluno', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoNovo(request):
    if request.user.is_authenticated:
        teste = request.user.pk
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/aluno/novo.html', {'title':'Novo Aluno', 
                                                        'msgTelaInicial':msgTelaInicial,
                                                        'teste':teste})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoBuscar(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/aluno/buscar.html', {'title':'Buscar Aluno', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoEditar(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/aluno/editar.html', {'title':'Editar Aluno', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})


def colaboradorGeral(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/colaborador/home.html', {'title':'Colaborador', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradorNovo(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/colaborador/novo.html', {'title':'Novo Colaborador', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradorBuscar(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/colaborador/buscar.html', {'title':'Buscar Colaborador', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradorEditar(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/colaborador/editar.html', {'title':'Editar Colaborador', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def classeGeral(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/classe/home.html', {'title':'Classe', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def classeNovo(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/classe/novo.html', {'title':'Nova Classe', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def classeBuscar(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/classe/buscar.html', {'title':'Buscar Classe', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def classeEditar(request):
    if request.user.is_authenticated:
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'gerencia/classe/editar.html', {'title':'Editar Classe', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

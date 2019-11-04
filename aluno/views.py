from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        alunoVisivel = False
        colaboradorVisivel = False
        classeVisivel = False
        aulasVisivel = False
        contasVisivel = False
        caixaVisivel = False
        estoqueVisivel = False
        controleVisivel = False
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'aluno/home.html', {'title':'Home', 
                                                        'alunoVisivel':alunoVisivel,
                                                        'colaboradorVisivel':colaboradorVisivel, 
                                                        'classeVisivel':classeVisivel, 
                                                        'aulasVisivel':aulasVisivel, 
                                                        'contasVisivel':contasVisivel, 
                                                        'caixaVisivel':caixaVisivel, 
                                                        'estoqueVisivel':estoqueVisivel, 
                                                        'controleVisivel':controleVisivel,
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoNovo(request):
    if request.user.is_authenticated:
        alunoVisivel = False
        colaboradorVisivel = False
        classeVisivel = False
        aulasVisivel = False
        contasVisivel = False
        caixaVisivel = False
        estoqueVisivel = False
        controleVisivel = False
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'aluno/novo.html', {'title':'Novo', 
                                                        'alunoVisivel':alunoVisivel,
                                                        'colaboradorVisivel':colaboradorVisivel, 
                                                        'classeVisivel':classeVisivel, 
                                                        'aulasVisivel':aulasVisivel, 
                                                        'contasVisivel':contasVisivel, 
                                                        'caixaVisivel':caixaVisivel, 
                                                        'estoqueVisivel':estoqueVisivel, 
                                                        'controleVisivel':controleVisivel,
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})


def alunoBusca(request):
    if request.user.is_authenticated:
        alunoVisivel = False
        colaboradorVisivel = False
        classeVisivel = False
        aulasVisivel = False
        contasVisivel = False
        caixaVisivel = False
        estoqueVisivel = False
        controleVisivel = False
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'aluno/buscar.html', {'title':'Buscar', 
                                                        'alunoVisivel':alunoVisivel,
                                                        'colaboradorVisivel':colaboradorVisivel, 
                                                        'classeVisivel':classeVisivel, 
                                                        'aulasVisivel':aulasVisivel, 
                                                        'contasVisivel':contasVisivel, 
                                                        'caixaVisivel':caixaVisivel, 
                                                        'estoqueVisivel':estoqueVisivel, 
                                                        'controleVisivel':controleVisivel,
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})


def alunoEdita(request):
    if request.user.is_authenticated:
        alunoVisivel = False
        colaboradorVisivel = False
        classeVisivel = False
        aulasVisivel = False
        contasVisivel = False
        caixaVisivel = False
        estoqueVisivel = False
        controleVisivel = False
        now = datetime.datetime.now().strftime('%H')
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            
        return render (request, 'aluno/editar.html', {'title':'Editar', 
                                                        'alunoVisivel':alunoVisivel,
                                                        'colaboradorVisivel':colaboradorVisivel, 
                                                        'classeVisivel':classeVisivel, 
                                                        'aulasVisivel':aulasVisivel, 
                                                        'contasVisivel':contasVisivel, 
                                                        'caixaVisivel':caixaVisivel, 
                                                        'estoqueVisivel':estoqueVisivel, 
                                                        'controleVisivel':controleVisivel,
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})
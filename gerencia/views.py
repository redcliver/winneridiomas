from django.shortcuts import render
import datetime
from .models import alunoModel
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

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
        if request.method == 'POST' and request.POST.get('nome') != None:
            nome = request.POST.get('nome')
            sobrenome = request.POST.get('sobrenome')
            cpf = request.POST.get('cpf')
            rg = request.POST.get('rg')
            dataNasc = request.POST.get('dataNasc')
            email = request.POST.get('email')
            celular = request.POST.get('celular')
            telefone = request.POST.get('telefone')
            classe = request.POST.get('classe')
            cep = request.POST.get('cep')
            endereco = request.POST.get('endereco')
            numero = request.POST.get('numero')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            sobrenomeList = sobrenome.split()
            usuario = nome[0].lower() + sobrenomeList[-1].lower()
            numAleatorio = get_random_string(length=4, allowed_chars='1234567890')
            senha = nome.lower() + numAleatorio
            tipo = "ALUNO"
            novoUsuario = User.objects.create_user(username=usuario, password=senha ,first_name=nome, last_name=tipo, email=email)
            novoUsuario.save()
            novoAluno = alunoModel(user=novoUsuario,
                                   nome=nome, 
                                   sobrenome=sobrenome, 
                                   cpf=cpf, 
                                   rg=rg, 
                                   data_nascimento=dataNasc, 
                                   email=email, 
                                   celular=celular, 
                                   telefone=telefone, 
                                   classe=classe, 
                                   cep=cep,
                                   endereco=endereco,
                                   numero=numero,
                                   bairro=bairro,
                                   cidade=cidade,
                                   estado=estado)
            novoAluno.save()
            message = "O aluno : " + nome + " "+ sobrenome +", foi adicionado com sucesso!"
            acessoUsuario = "Usuário: " + usuario 
            acessoSenha = "Senha : " + senha
            return render (request, 'gerencia/aluno/novoAfter.html', {'title':'Novo Aluno', 
                                                        'msgTelaInicial':msgTelaInicial,
                                                        'message':message,
                                                        'acessoUsuario':acessoUsuario,
                                                        'acessoSenha':acessoSenha})
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

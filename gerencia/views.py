from django.shortcuts import render
import datetime
from evento.models import eventoModel
from .models import alunoModel, colaboradorModel, salaModel, cidadeModel
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
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
    return render (request, 'site/login.html', {'title':'Login'})
    
def suporte(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
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
    return render (request, 'site/login.html', {'title':'Login'})

def alunoGeral(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
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
    return render (request, 'site/login.html', {'title':'Login'})

def alunoNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            teste = request.user.pk
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            cidades = cidadeModel.objects.filter(liberacao=1).order_by('-nome')
            classes = salaModel.objects.filter(liberacao=1).order_by('-nome')
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
                classeID = request.POST.get('classeID')
                cep = request.POST.get('cep')
                endereco = request.POST.get('endereco')
                numero = request.POST.get('numero')
                bairro = request.POST.get('bairro')
                cidadeID = request.POST.get('cidadeID')
                sobrenomeList = sobrenome.split()
                usuario = nome[0].lower() + sobrenomeList[-1].lower()
                numAleatorio = get_random_string(length=4, allowed_chars='1234567890')
                senha = nome.lower() + numAleatorio
                tipo = "ALUNO"
                novoUsuario = User.objects.create_user(username=usuario, password=senha ,first_name=nome, last_name=tipo, email=email)
                novoUsuario.save()
                cidadeObj = cidadeModel.objects.filter(id=cidadeID).get()
                classeObj = salaModel.objects.filter(id=classeID).get()
                novoAluno = alunoModel(user=novoUsuario,
                                    nome=nome, 
                                    sobrenome=sobrenome, 
                                    cpf=cpf, 
                                    rg=rg, 
                                    dataNasc=dataNasc, 
                                    email=email, 
                                    celular=celular, 
                                    telefone=telefone, 
                                    classe=classeObj, 
                                    cep=cep,
                                    endereco=endereco,
                                    numero=numero,
                                    bairro=bairro,
                                    cidadeEstado=cidadeObj)
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
                                                            'teste':teste,
                                                            'today':today,
                                                            'cidades':cidades,
                                                            'classes':classes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            alunos = alunoModel.objects.filter(user__last_name="ALUNO", liberacao=1).order_by('-nome')
            if request.method == 'POST' and request.POST.get('alunoID') != None:
                alunoID = request.POST.get('alunoID')
                alunoObj = alunoModel.objects.filter(user__id=alunoID).get()

                return render (request, 'gerencia/aluno/visualizar.html', {'title':'Visualizar Aluno', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'alunoObj':alunoObj})
            return render (request, 'gerencia/aluno/buscar.html', {'title':'Buscar Aluno', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'alunos':alunos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            alunos = alunoModel.objects.filter(user__last_name="ALUNO", liberacao=1).order_by('-nome')
            if request.method == 'POST' and request.POST.get('alunoID') != None:
                alunoID = request.POST.get('alunoID')
                alunoObj = alunoModel.objects.filter(user__id=alunoID).get()
                alunoDataNasc = alunoObj.dataNasc.strftime('%Y-%m-%d')
                return render (request, 'gerencia/aluno/editarForm.html', {'title':'Editar Aluno', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'alunoObj':alunoObj,
                                                            'alunoDataNasc':alunoDataNasc})
            return render (request, 'gerencia/aluno/editar.html', {'title':'Selecionar Aluno', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'alunos':alunos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def alunoSalvar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
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
            if request.method == 'POST' and request.POST.get('alunoID') != None:
                alunoID = request.POST.get('alunoID') 
                alunoObj = alunoModel.objects.filter(user__id=alunoID).get()
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
                usuario = request.POST.get('usuario')
                alunoObj.nome = nome
                alunoObj.sobrenome = sobrenome
                alunoObj.cpf = cpf
                alunoObj.rg = rg
                alunoObj.dataNasc = dataNasc
                alunoObj.user.email = email
                alunoObj.celular = celular
                alunoObj.telefone = telefone
                alunoObj.classe = classe
                alunoObj.cep = cep
                alunoObj.endereco = endereco
                alunoObj.numero = numero
                alunoObj.bairro = bairro
                alunoObj.cidade = cidade
                alunoObj.estado = estado
                alunoObj.user.last_name = usuario
                alunoObj.save()
                return render (request, 'gerencia/aluno/home.html', {'title':'Aluno', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'alunoObj':alunoObj})
            return render (request, 'gerencia/aluno/home.html', {'title':'Aluno', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def colaboradorGeral(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
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
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradorNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            cidades = cidadeModel.objects.filter(liberacao=1).order_by('-nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/colaborador/novo.html', {'title':'Novo Colaborador', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'cidades':cidades})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradorBuscar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            colaboradores = colaboradorModel.objects.filter(liberacao=1).order_by('-nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/colaborador/buscar.html', {'title':'Buscar Colaborador', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'colaboradores':colaboradores})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def colaboradorEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            colaboradores = colaboradorModel.objects.filter(liberacao=1).order_by('-nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/colaborador/editar.html', {'title':'Editar Colaborador', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'colaboradores':colaboradores})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def classeGeral(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
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
    return render (request, 'site/login.html', {'title':'Login'})

def classeNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            cidades = cidadeModel.objects.filter(liberacao=1).order_by('-nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/classe/novo.html', {'title':'Nova Classe', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'cidades':cidades})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def classeBuscar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            classes = salaModel.objects.filter(liberacao=1).order_by('-nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/classe/buscar.html', {'title':'Buscar Classe', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'classes':classes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def classeEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            classes = salaModel.objects.filter(liberacao=1).order_by('-nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/classe/editar.html', {'title':'Editar Classe', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'classes':classes})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def eventoGeral(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now().strftime('%H')
            now = int(now)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/eventos/home.html', {'title':'Eventos', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
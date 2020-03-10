from django.shortcuts import render
import datetime
from evento.models import eventoModel
from .models import alunoModel, colaboradorModel, salaModel, cidadeModel, perguntaModel, respostaModel
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

def testeGeral(request):
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
                
            return render (request, 'gerencia/nivelamento/home.html', {'title':'Nivelamento', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def testeNovo(request):
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
            if request.method == "POST" and request.POST.get('pergunta') != None:
                pergunta = request.POST.get('pergunta')
                pontuacao = request.POST.get('pontuacao')
                respostaCorreta = request.POST.get('respostaCorreta')
                respostaAlternativa1 = request.POST.get('respostaAlternativa1')
                respostaAlternativa2 = request.POST.get('respostaAlternativa2')
                respostaAlternativa3 = request.POST.get('respostaAlternativa3')
                novaPergunta = perguntaModel(pergunta=pergunta, pontuacao=pontuacao)
                novaPergunta.save()
                if respostaCorreta != None:
                    novaResposta = respostaModel(resposta= respostaCorreta, tipo=1)
                    novaResposta.save()
                    novaPergunta.respostas.add(novaResposta)
                    novaPergunta.save()
                if respostaAlternativa1 != None:
                    novaResposta = respostaModel(resposta= respostaAlternativa1)
                    novaResposta.save()
                    novaPergunta.respostas.add(novaResposta)
                    novaPergunta.save()
                if respostaAlternativa2 != None:
                    novaResposta = respostaModel(resposta= respostaAlternativa2)
                    novaResposta.save()
                    novaPergunta.respostas.add(novaResposta)
                    novaPergunta.save()
                if respostaAlternativa3 != None:
                    novaResposta = respostaModel(resposta= respostaAlternativa3)
                    novaResposta.save()
                    novaPergunta.respostas.add(novaResposta)
                    novaPergunta.save()

                msgConfirmacao = "Nova pergunta cadastrada com sucesso!"
                return render (request, 'gerencia/nivelamento/novo.html', {'title':'Nova Pergunta', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'msgConfirmacao':msgConfirmacao})
                
            return render (request, 'gerencia/nivelamento/novo.html', {'title':'Nova Pergunta', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def testeBusca(request):
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
            
            perguntas = perguntaModel.objects.filter(estado=1).all().order_by('id')
            if request.method == "POST" and request.POST.get('perguntaID') != None:
                perguntaID = request.POST.get('perguntaID')
                perguntaObj = perguntaModel.objects.get(id=perguntaID)
                respostasObj = perguntaObj.respostas.all()
                return render (request, 'gerencia/nivelamento/visualizar.html', {'title':'Visualizar Pergunta', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'perguntaObj':perguntaObj,
                                                            'respostasObj':respostasObj})
                
            return render (request, 'gerencia/nivelamento/buscar.html', {'title':'Visualizar Pergunta', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'perguntas':perguntas})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def testeEdita(request):
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
            try:
                perguntaIDGet = request.GET.get('perguntaID')
                perguntaObjGet = perguntaModel.objects.get(id=perguntaIDGet)
                resposta1 = perguntaObjGet.respostas.all()[0]
                resposta2 = perguntaObjGet.respostas.all()[1]
                resposta3 = perguntaObjGet.respostas.all()[2]
                resposta4 = perguntaObjGet.respostas.all()[3]
            except:
                respostasObjGet = None

            if request.method == "POST" and request.POST.get('perguntaID') != None:
                perguntaID = request.POST.get('perguntaID')
                perguntaObj = perguntaModel.objects.get(id=perguntaID)
                pergunta = request.POST.get('pergunta')
                pontuacao = request.POST.get('pontuacao')
                
                #Resposta correta
                respostaCorretaID = request.POST.get('respostaCorretaID')
                respostaCorretaText = request.POST.get('respostaCorretaText')
                respostaCorretaObj = respostaModel.objects.get(id=respostaCorretaID)
                respostaCorretaObj.resposta = respostaCorretaText
                respostaCorretaObj.save()

                #Resposta errada 1
                respostasAlternativa1 = request.POST.get('respostasAlternativa1')
                respostaAlternativaText1 = request.POST.get('respostaAlternativaText1')
                respostaAlternativaObj1 = respostaModel.objects.get(id=respostasAlternativa1)
                respostaAlternativaObj1.resposta = respostaAlternativaText1
                respostaAlternativaObj1.save()

                #Resposta errada 2
                respostasAlternativa2 = request.POST.get('respostasAlternativa2')
                respostaAlternativaText2 = request.POST.get('respostaAlternativaText2')
                respostaAlternativaObj2 = respostaModel.objects.get(id=respostasAlternativa2)
                respostaAlternativaObj2.resposta = respostaAlternativaText2
                respostaAlternativaObj2.save()
                
                #Resposta errada 3
                respostasAlternativa3 = request.POST.get('respostasAlternativa3')
                respostaAlternativaText3 = request.POST.get('respostaAlternativaText3')
                respostaAlternativaObj3 = respostaModel.objects.get(id=respostasAlternativa3)
                respostaAlternativaObj3.resposta = respostaAlternativaText3
                respostaAlternativaObj3.save()

                perguntaObj.pergunta = pergunta
                perguntaObj.pontuacao = pontuacao              

                perguntaObj.save()
                respostasObj = perguntaObj.respostas.all()
            
                msgConfirmacao = "Pergunta editada com sucesso!"
                return render (request, 'gerencia/nivelamento/visualizar.html', {'title':'Visualizar Pergunta', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'msgConfirmacao':msgConfirmacao,
                                                            'perguntaObj':perguntaObj,
                                                            'respostasObj':respostasObj})
                
            return render (request, 'gerencia/nivelamento/editar.html', {'title':'Editar Pergunta', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'perguntaObj':perguntaObjGet,
                                                            'resposta1':resposta1,
                                                            'resposta2':resposta2,
                                                            'resposta3':resposta3,
                                                            'resposta4':resposta4})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
from django.shortcuts import render
from website.models import contato, registro, indicacao, testeNivelamento, respostaNivelamento, perguntasExecutadas
from evento.models import eventoModel
from gerencia.models import perguntaModel, respostaModel
from django.core.mail import EmailMessage
import random
from random import shuffle
import datetime
import os
from twilio.rest import Client

# Create your views here.

def paginaPrincipal(request):
    now = datetime.datetime.now().strftime('%H')
    now = int(now)
    try:
        eventoObj1 = eventoModel.objects.latest('id')
        tituloEvento1 = eventoObj1.titulo
        descBreveEvento1 = eventoObj1.descricao
        dataEvento1 = eventoObj1.data_evento
        diaEvento1 = dataEvento1.strftime("%d")
        mesEvento1 = dataEvento1.strftime("%B")
        evento2 = int(eventoObj1.id) - 1
    except:
        eventoObj1 = None
        tituloEvento1 = None
        descBreveEvento1 = None
        diaEvento1 = None
        mesEvento1 = None
        evento2 = None
    
    try:
        eventoObj2 = eventoModel.objects.get(id=evento2)
        tituloEvento2 = eventoObj2.titulo
        descBreveEvento2 = eventoObj2.descricao
        dataEvento2 = eventoObj2.data_evento
        diaEvento2 = dataEvento2.strftime("%d")
        mesEvento2 = dataEvento2.strftime("%B")
        evento3 = int(eventoObj2.id) - 1
    except:
        eventoObj2 = None
        tituloEvento2 = None
        descBreveEvento2 = None
        diaEvento2 = None
        mesEvento2 = None
        evento3 = None
    
    try:
        eventoObj3 = eventoModel.objects.get(id=evento2)
        tituloEvento3 = eventoObj3.titulo
        descBreveEvento3 = eventoObj3.descricao
        dataEvento3 = eventoObj3.data_evento
        diaEvento3 = dataEvento3.strftime("%d")
        mesEvento3 = dataEvento3.strftime("%B")
    except:
        eventoObj3 = None
        tituloEvento3 = None
        descBreveEvento3 = None
        diaEvento3 = None
        mesEvento3 = None
    return render(request, 'site/home.html', {'title': 'Home',
                                                'tituloEvento1': tituloEvento1,
                                                'descBreveEvento1': descBreveEvento1,
                                                'diaEvento1': diaEvento1,
                                                'mesEvento1': mesEvento1,
                                                'eventoObj1':eventoObj1,
                                                'tituloEvento2': tituloEvento2,
                                                'descBreveEvento2': descBreveEvento2,
                                                'diaEvento2': diaEvento2,
                                                'mesEvento2': mesEvento2,
                                                'eventoObj2':eventoObj2,
                                                'tituloEvento3': tituloEvento3,
                                                'descBreveEvento3': descBreveEvento3,
                                                'diaEvento3': diaEvento3,
                                                'mesEvento3': mesEvento3,
                                                'eventoObj3':eventoObj3})


def cursos(request):
    return render(request, 'site/cursos.html', {'title': 'Cursos'})

def kids(request):
    return render(request, 'site/cursos/kids.html', {'title': 'Kids'})

def adult(request):
    return render(request, 'site/cursos/adult.html', {'title': 'Adult'})

def business(request):
    return render(request, 'site/cursos/business.html', {'title': 'Business'})

def inCompany(request):
    return render(request, 'site/cursos/inCompany.html', {'title': 'In Company'})

def testPreparation(request):
    return render(request, 'site/cursos/testPreparation.html', {'title': 'Test Preparation'})

def vip(request):
    return render(request, 'site/cursos/vip.html', {'title': 'VIP'})

def unidades(request):
    return render(request, 'site/unidades.html', {'title': 'Unidades'})

def tresLagoas(request):
    return render(request, 'site/tresLagoas.html', {'title': 'Três Lagoas'})

def aguaClara(request):
    return render(request, 'site/aguaClara.html', {'title': 'Água Clara'})

def ribasRioPardo(request):
    return render(request, 'site/ribasRioPardo.html', {'title': 'Ribas do Rio Pardo'})

def parceiros(request):
    return render(request, 'site/parceiros.html', {'title': 'Parceiros'})

def indiqueParceiro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        empresa = request.POST.get('empresa')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        novaIndicacao = indicacao(nome=nome, empresa=empresa, sobrenome=sobrenome, email=email, telefone=telefone, mensagem=mensagem)
        novaIndicacao.save()

        msgEmail = "Contato recebido via website. \n\n\n NOME:\n" + nome +"\n\nEMPRESA:\n" + empresa + "\n\nTELEFONE:\n"+ telefone +"\n\nE-MAIL:\n"+ email + "\n\nMENSAGEM:\n" + mensagem + "\n\n\nEssa mensagem foi gerada automaticamente, não responta."
        testeEmail = EmailMessage('Contato website - INDICAÇÃO PARCEIRO', msgEmail, to=['winnercallan@uol.com.br'])
        testeEmail.send()

        #client = Client()        
        #from_whatsapp_number='whatsapp:+5567991865754'
        #to_whatsapp_number='whatsapp:+5567991865754'
        #message = client.messages.create(body='Check out this owl!',
        #               from_=from_whatsapp_number,
        #               to=to_whatsapp_number)

        msgConfirmação = "Indicação enviada com sucesso!"
        return render(request, 'site/home.html', {'title': 'Home', 'msgConfirmação':msgConfirmação})
    return render(request, 'site/indiqueParceiro.html', {'title': 'Indique Parceiros'})

def testeNivelamentoView(request):
    contador = 0
    if request.method == "POST" and request.POST.get('nome') != None:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        novoTesteNivelamento = testeNivelamento(nome=nome, email=email, telefone=telefone)
        novoTesteNivelamento.save()
        perguntaObj = perguntaModel.objects.filter(estado=1).order_by('?')[0]
        pergExecutadas = perguntasExecutadas(pergunta=perguntaObj.id)
        pergExecutadas.save()
        novoTesteNivelamento.executadas.add(pergExecutadas)
        novoTesteNivelamento.save()
        contador = contador + 1
        respostas = perguntaObj.respostas.all()
        respostasList = list(respostas)
        shuffle(respostasList)
        return render(request, 'site/finalNivelamento.html', {'title': 'Nivelamento',
                                                         'perguntaObj':perguntaObj,
                                                         'contador':contador,
                                                         'respostas':respostas,
                                                         'respostasList':respostasList,
                                                         'testeNivelamentoObj':novoTesteNivelamento})
    return render(request, 'site/nivelamento.html', {'title': 'Nivelamento'})


def PerguntasNivelamento(request):
    if request.method == "POST" and request.POST.get('contador') != None and request.POST.get('testeNivelamentoID') != None:
        contador = request.POST.get('contador')
        if int(contador) < 20:
            testeNivelamentoID = request.POST.get('testeNivelamentoID')
            perguntaID = request.POST.get('perguntaID')
            respostaID = request.POST.get('respostaID')
            testeNivelamentoObj = testeNivelamento.objects.get(id=testeNivelamentoID)
            perguntaObj = perguntaModel.objects.get(id=perguntaID)
            respostaObj = respostaModel.objects.get(id=respostaID)
            novaRespostaObj = respostaNivelamento(pergunta= perguntaObj, resposta=respostaObj)
            novaRespostaObj.save()
            testeNivelamentoObj.respostas.add(novaRespostaObj)
            testeNivelamentoObj.save()
            pergExecutadas = perguntasExecutadas(pergunta=perguntaObj.id)
            pergExecutadas.save()
            testeNivelamentoObj.executadas.add(pergExecutadas)
            testeNivelamentoObj.save()
            perguntasExecList = []
            for p in testeNivelamentoObj.executadas.all():
                perguntasExecList.append(p.pergunta)
            contador = int(contador) + 1
            perguntaObjeto = perguntaModel.objects.filter(estado=1).exclude(id__in=perguntasExecList).order_by('?')[0]

            respostas = perguntaObjeto.respostas.all()
            respostasList = list(respostas)
            shuffle(respostasList)
            return render(request, 'site/perguntas.html', {'title': 'Nivelamento',
                                                            'contador':contador,
                                                            'testeNivelamentoObj':testeNivelamentoObj,
                                                            'respostasList':respostasList,
                                                            'perguntaObj':perguntaObjeto})
        if int(contador) >= 20:
            testeNivelamentoID = request.POST.get('testeNivelamentoID')
            perguntaID = request.POST.get('perguntaID')
            respostaID = request.POST.get('respostaID')
            testeNivelamentoObj = testeNivelamento.objects.get(id=testeNivelamentoID)
            perguntaObj = perguntaModel.objects.get(id=perguntaID)
            respostaObj = respostaModel.objects.get(id=respostaID)
            novaRespostaObj = respostaNivelamento(pergunta= perguntaObj, resposta=respostaObj)
            novaRespostaObj.save()
            testeNivelamentoObj.respostas.add(novaRespostaObj)
            testeNivelamentoObj.save()
            pergExecutadas = perguntasExecutadas(pergunta=perguntaObj.id)
            pergExecutadas.save()
            testeNivelamentoObj.executadas.add(pergExecutadas)
            testeNivelamentoObj.save()
            perguntasExecList = []
            for p in testeNivelamentoObj.executadas.all():
                perguntasExecList.append(p.pergunta)
            contador = int(contador) + 1
            perguntaObjeto = perguntaModel.objects.filter(estado=1).order_by('?')[0]

            respostas = perguntaObjeto.respostas.all()
            respostasList = list(respostas)
            shuffle(respostasList)
            msgConfirmacao = "FINALIZAR AQUI MESMO"
            return render(request, 'site/finalNivelamento.html', {'title': 'Nivelamento',
                                                            'contador':contador,
                                                            'testeNivelamentoObj':testeNivelamentoObj,
                                                            'respostasList':respostasList,
                                                            'perguntaObj':perguntaObjeto,
                                                            'msgConfirmacao':msgConfirmacao})
    return render(request, 'site/nivelamento.html', {'title': 'Nivelamento'})

def viewContato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')
        novoContato = contato(nome=nome, sobrenome=sobrenome, email=email, telefone=telefone, mensagem=mensagem)
        novoContato.save()
        msgEmail = "Contato recebido via website. \n\n\n NOME:\n" + nome + " " + sobrenome +"\n\nTELEFONE:\n"+ telefone +"\n\nE-MAIL:\n"+ email + "\n\nMENSAGEM:\n" + mensagem + "\n\n\nEssa mensagem foi gerada automaticamente, não responta."
        testeEmail = EmailMessage('Contato website - CONTATO', msgEmail, to=['winnercallan@uol.com.br'])
        testeEmail.send()
        
        confirmacao = "Mensagem enviada com sucesso!"
        return render(request, 'site/contato.html', {'title': 'Contato', 'confirmacao': confirmacao})
    
    return render(request, 'site/contato.html', {'title': 'Contato'})

def entrar(request):
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
            
        return render (request, 'gerencia/home.html', {'title':'Home', 
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

def instituicao(request):
    return render(request, 'site/instituicao.html', {'title': 'Instituicao'})

def metodo(request):
    return render(request, 'site/metodo.html', {'title': 'Metodo'})

def colaboradores(request):
    return render(request, 'site/colaboradores.html', {'title': 'Colaboradores'})

def viewRegistro(request):
    if request.method == "POST" and request.POST.get('emailRegistro') != "":
        emailRegistro = request.POST.get('emailRegistro')
        novoRegistro = registro(email=emailRegistro)
        novoRegistro.save()
        return render(request, 'site/registro.html', {'title': 'Receber novidades...'})
    return render(request, 'site/registro.html', {'title': 'Receber novidades...'})

def error_404(request, exception):
    return render(request, 'site/404.html', {'title': 'Error'})

def error_500(request):
    return render(request, 'site/500.html', {'title': 'Error'})
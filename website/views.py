from django.shortcuts import render
from website.models import contato, registro, indicacao
from django.core.mail import EmailMessage
import datetime

# Create your views here.
def paginaPrincipal(request):
    return render(request, 'site/home.html', {'title': 'Home'})

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
        msgConfirmação = "Indicação enviada com sucesso!"
        return render(request, 'site/home.html', {'title': 'Home', 'msgConfirmação':msgConfirmação})
    return render(request, 'site/indiqueParceiro.html', {'title': 'Indique Parceiros'})

def nivelamento(request):
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
        testeEmail = EmailMessage('Contato website', msgEmail, to=['winnercallan@uol.com.br'])
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
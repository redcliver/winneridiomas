from django.shortcuts import render
from .models import eventoModel, imagensModel
import datetime

from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks      
from .models import eventoModel
from .forms import eventoForm

# Create your views here.

def upload(request):
    context = dict( backend_form = eventoForm())

    if request.method == 'POST':
        form = eventoForm(request.POST, request.FILES)
        context['posted/eventos'] = form.instance
        if form.is_valid():
            form.save()
    eventoObj = eventoModel.objects.all().latest('id')
    return render(request, 'gerenciaEvento/buscar.html',  {'eventoObj':eventoObj })

def eventoGeral(request):
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
            
        return render (request, 'gerenciaEvento/home.html', {'title':'Eventos', 
                                                        'msgTelaInicial':msgTelaInicial})
    return render (request, 'site/login.html', {'title':'Login'})

def eventoNovo(request):
    if request.user.is_authenticated:

        teste = request.user.pk
        today = datetime.datetime.now().strftime("%d/%m/%Y")
        now = datetime.datetime.now().strftime("%H")
        timeNow = datetime.datetime.now().strftime('%H:%MM')
        todayFormatado = datetime.datetime.now()
        now = int(now)
        msgTelaInicial = "Olá, " + request.user.get_short_name() 
        if now >= 4 and now <= 11:
            msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
        elif now > 11 and now < 18:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
        elif now >= 18 and now < 4:
            msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
        
        if request.method == 'GET':     
            return render (request, 'gerenciaEvento/novo.html', {'title':'Novo Evento', 
                                                        'msgTelaInicial':msgTelaInicial,
                                                        'teste':teste,
                                                        'today':today,
                                                        'timeNow': timeNow,
                                                        'todayFormatado':todayFormatado})
        if request.method == 'POST':
            tituloEvento = request.POST.get('tituloEvento')    
            descBreveEvento = request.POST.get('descBreveEvento')   
            dataEvento = request.POST.get('dataEvento')
            horaEvento = request.POST.get('horaEvento')
            localEvento = request.POST.get('localEvento')
            imagemCapa = request.FILES['imagemCapa']
            descCompletaEvento = request.POST.get('descCompletaEvento')
            eventoObj = eventoModel(titulo=tituloEvento, 
                                    descricao=descBreveEvento, 
                                    local_evento=localEvento, 
                                    conteudo=descCompletaEvento, 
                                    imagem_capa=imagemCapa,
                                    data_evento=dataEvento,
                                    hora_evento=horaEvento)
            eventoObj.save()
            dataEvento = datetime.datetime.strptime(dataEvento, '%Y-%m-%d')
            diaEvento = dataEvento.strftime("%d")
            mesEvento = dataEvento.strftime("%B")
            return render (request, 'gerenciaEvento/novo.html', {'title':'Novo Evento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'teste':teste,
                                                            'today':today,
                                                            'timeNow': timeNow,
                                                            'tituloEvento': tituloEvento,
                                                            'descBreveEvento': descBreveEvento,
                                                            'descCompletaEvento': descCompletaEvento,
                                                            'eventoObj':eventoObj,
                                                            'diaEvento':diaEvento,
                                                            'mesEvento':mesEvento})
    return render (request, 'site/login.html', {'title':'Login'})


def eventoVisualizar(request):
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
        try:
            eventoObj1 = eventoModel.objects.latest('id')
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
            eventoObj3 = eventoModel.objects.get(id=evento3)
            dataEvento3 = eventoObj3.data_evento
            diaEvento3 = dataEvento3.strftime("%d")
            mesEvento3 = dataEvento3.strftime("%B")
        except:
            eventoObj3 = None
            tituloEvento3 = None
            descBreveEvento3 = None
            diaEvento3 = None
            mesEvento3 = None
        return render (request, 'gerenciaEvento/visualizar.html', {'title':'Visualizar Eventos', 
                                                        'msgTelaInicial':msgTelaInicial,
                                                        'diaEvento1': diaEvento1,
                                                        'mesEvento1': mesEvento1,
                                                        'eventoObj1':eventoObj1,
                                                        'diaEvento2': diaEvento2,
                                                        'mesEvento2': mesEvento2,
                                                        'eventoObj2':eventoObj2,
                                                        'diaEvento3': diaEvento3,
                                                        'mesEvento3': mesEvento3,
                                                        'eventoObj3':eventoObj3})
    return render (request, 'site/login.html', {'title':'Login'})

def eventoDetalhes(request):
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
        try:
            eventoObj = eventoModel.objects.latest('id')
            tituloEvento = eventoObj.titulo
            descBreveEvento = eventoObj.descricao
            dataEvento = eventoObj.data_evento
            diaEvento = dataEvento.strftime("%d")
            mesEvento = dataEvento.strftime("%B")
            imagensAdicionais = eventoObj.imagem_adicional.all()
        except:
            eventoObj = None
            tituloEvento = None
            descBreveEvento = None
            diaEvento = None
            mesEvento = None

        if request.method == 'POST' and request.POST.get('eventoID') != None:
            eventoID = request.POST.get('eventoID')
            imagemAdicional = request.FILES['imagemAdicional']
            eventoObj = eventoModel.objects.get(id=eventoID)
            if imagemAdicional != None:
                novaImgAdicional = imagensModel(image=imagemAdicional)
                novaImgAdicional.save()
                eventoObj.imagem_adicional.add(novaImgAdicional)
                eventoObj.save()

            diaEvento = eventoObj.data_evento.strftime("%d")
            mesEvento = eventoObj.data_evento.strftime("%B")
            imagensAdicionais = eventoObj.imagem_adicional.all()
            return render (request, 'gerenciaEvento/visualizarDetalhes.html', {'title':'Visualizar Eventos', 
                                                                            'msgTelaInicial':msgTelaInicial,
                                                                            'diaEvento': diaEvento,
                                                                            'mesEvento': mesEvento,
                                                                            'eventoObj':eventoObj,
                                                                            'imagensAdicionais':imagensAdicionais})
        
        return render (request, 'gerenciaEvento/visualizarDetalhes.html', {'title':'Visualizar Eventos', 
                                                                            'msgTelaInicial':msgTelaInicial,
                                                                            'tituloEvento': tituloEvento,
                                                                            'descBreveEvento': descBreveEvento,
                                                                            'diaEvento': diaEvento,
                                                                            'mesEvento': mesEvento,
                                                                            'eventoObj':eventoObj,
                                                                            'imagensAdicionais':imagensAdicionais})
    return render (request, 'site/login.html', {'title':'Login'})
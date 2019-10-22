from django.shortcuts import render
from .models import imageEvento
import datetime

# Create your views here.

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
        todayFormatado = datetime.datetime.now().strftime("%Y-%m-%d")
        hourFormatado = datetime.datetime.now().strftime("%H:%M")
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
                                                        'todayFormatado':todayFormatado,
                                                        'hourFormatado':hourFormatado})
        if request.method == 'POST':
            tituloEvento = request.POST.get('tituloEvento')    
            descBreveEvento = request.POST.get('descBreveEvento')   
            dataEvento = request.POST.get('dataEvento')
            imageFile = request.FILES['imageFile']
            dataFormatadaEvento = datetime.datetime.strptime(dataEvento, "%Y-%m-%d").date()
            horaEvento = request.POST.get('horaEvento')                 
            descCompletaEvento = request.POST.get('descCompletaEvento')
            diaEvento = dataFormatadaEvento.strftime("%d")
            mesEvento = dataFormatadaEvento.strftime("%B")
            eventoObj = "aaaa"
            novaImg = imageEvento(name=tituloEvento, imagefile=imageFile)
            novaImg.save()
            imgFile= novaImg.imagefile
            return render (request, 'gerenciaEvento/novo.html', {'title':'Novo Evento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'teste':teste,
                                                            'today':today,
                                                            'timeNow': timeNow,
                                                            'tituloEvento': tituloEvento,
                                                            'descBreveEvento': descBreveEvento,
                                                            'diaEvento': diaEvento,
                                                            'mesEvento': mesEvento,
                                                            'descCompletaEvento': descCompletaEvento,
                                                            'eventoObj':eventoObj,
                                                            'imgFile':imgFile})
    return render (request, 'site/login.html', {'title':'Login'})
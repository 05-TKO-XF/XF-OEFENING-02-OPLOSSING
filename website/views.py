from django.shortcuts import render

from datetime import date

context = {
    'jaar': date.today().year
}

def index(request):
    context['titel'] = 'Fietsdokter'
    return render(request, 'index.html', context)

def aanhuis(request):
    context['titel'] = 'Reparatie aan huis'
    return render(request, 'aanhuis.html', context)

def winkel(request):
    context['titel'] = 'Winkel'
    return render(request, 'winkel.html', context)

# def contact(request):
#     context['titel'] = 'Contact'
#     return render(request, 'contact.html', context)

from .email import Email
import json

def contact(request):
    context['titel'] = 'Contact'

    if request.method == 'POST':
        formulier = Email(request.POST)
        context['formulierVariabelen'] = request.POST.dict()
        if formulier.is_valid():
            frmDta = formulier.cleaned_data
            if formulier.mail(frmDta):
                context['email_verstuurd'] = True
                context['fouten'] = []
            else:
                print('fout mail 1')
        else:
            fouten = []
            for key, val in json.loads(formulier.errors.as_json()).items():
                fouten.append(val[0]['message'])
            context['fouten'] = fouten
            # context['fouten'] = json.loads(formulier.errors.as_json())
            # print('fout items', json.loads(formulier.errors.as_json()))
            # print('fout items', formulier.errors.as_data())
    
    return render(request, 'contact.html', context)
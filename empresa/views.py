from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologia, Empresa
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def nova_empresa(request):
    if request.method == "GET":
        techs = Tecnologia.objects.all()
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        tecnologias = request.POST.getlist('tecnologias')
        caracteristicas = request.POST.get('caracteristicas')
        logo = request.FILES.get('logo')
        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or (not logo)):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos corretamente')
            return redirect('/home/nova_empresa')

        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR, 'Sua logo não pode ter mais de 10MB')
            return redirect('/home/nova_empresa')

        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido.')
            return redirect('/home/nova_empresa')

        #criando uma nova empresa e pegando os items  do form e atribuindo ao que foi definido
        empresa = Empresa(
            logo=logo,
            nome=nome,
            cidade=cidade,
            endereco=endereco,
            caracteristicas_empresa=caracteristicas,
            #tecnologias=tecnologias, errado não pode
            nicho_mercado=nicho,
        )
        empresa.save() #para salvar no banco de dados é só isso
        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
        return redirect('/home/nova_empresa')

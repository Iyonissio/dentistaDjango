from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user , allowed_users ,admin_only
from .forms import CreateUserForm

def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def pricing(request):
    return render(request,'pricing.html',{})

def services(request):
    return render(request,'services.html',{})

def contact(request):
    if request.method == "POST":
        cf_name = request.POST['cf-name']
        cf_email = request.POST['cf-email']
        cf_number = request.POST['cf-number']
        cf_message = request.POST['cf-message']

        #Enviar Email
        send_mail(
            cf_name,
            cf_message,
            cf_email,  # Origem
            ['mbryoyo01@gmail.com'],#Destino Emails
        )
        return render(request, 'contact.html', {'cf_name':cf_name})
    else:
        return render(request,'contact.html',{})

def consulta(request):
    if request.method == "POST":

        cf_name = request.POST['cf-name']
        cf_email = request.POST['cf-email']
        cf_number = request.POST['cf-number']
        cf_endereco = request.POST['cf-endereco']
        cf_message = request.POST['cf-message']
        cf_budgets = request.POST['cf-budgets']

        return render(request,'consulta.html',{
            'cf_name':cf_name,
            'cf_email':cf_email,
            'cf_number':cf_number,
            'cf_endereco':cf_endereco,
            'cf_message':cf_message,
            'cf_budgets':cf_budgets,
        })
    else:
        return render(request,'contact.html',{})

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Conta criada com Sucesso para ' + username)
            return redirect('base')

    context = {'form': form}
    return render(request, 'base.html', context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Nome de usuario ou password incorrecto!')

    context = {}
    return render(request, 'base.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
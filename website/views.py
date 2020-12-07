from django.shortcuts import render
from django.core.mail import send_mail

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
            cf_email,#Origem
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
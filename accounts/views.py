from django.shortcuts import render,redirect
from .forms import RegisterForm
from .models import Account
from django.contrib.auth import authenticate ,login,logout
#Activatetion Account
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode ,urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponse


# Create your views here.
def register(request):

    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            phone_number=form.cleaned_data['phone_number']
            country=form.cleaned_data['country']
            password=form.cleaned_data['password']
            username=email.split('@')[0]
            user=Account.objects.create_user(first_name=first_name,last_name=last_name,user_name=username,email=email,country=country ,password=password)
            user.phone_number=phone_number
            user.save()

            #User Activat
            doman_name=get_current_site(request)
            mail_subject='please activate your account'
            message=render_to_string('accounts/account_verification_email.html',{
                'user':user,
                'domain':doman_name,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email=email
            send_mail=EmailMessage(mail_subject,message,to=[to_email])
            send_mail.send()
            return redirect('login'+f'?command=verification&mail={email}')
    else:
        form=RegisterForm()

    context={
        'form':form


    }    
    return render(request,"accounts/register.html",context)

def login_(request):
     if request.method == 'POST':
         email=request.POST['email']
         password=request.POST['password']
         user=authenticate(email=email,password=password)
         if user is not None:
             login(request,user)
             return redirect('')
         else:
             return redirect('accounts:login')
     return render(request,'accounts/login.html')        

def activate(request ,uidb64,token):
    pass
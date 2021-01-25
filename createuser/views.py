from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import registerForm
from django.contrib import messages
from .models import unverified_user,CustomUser
from  django.contrib.auth.hashers import make_password
import random
from django.conf import settings 
from django.core.mail import send_mail 
from django.http import JsonResponse
import datetime



def send_otp(emailid,otp):
    subject = 'you otp verification code is here'
    message = f'Hi {emailid}, your otp is {otp}.'
    email_from = settings.EMAIL_HOST_USER 
    reciever = [emailid, ] 
    print(email_from,'host')
    print(reciever,'recv')
    send_mail( subject, message, email_from, reciever )
    return True



def unverified_email(request):
    if request.POST:
        form=registerForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
            req=request.POST
            email=req.get('email')
            number = random.randint(1000,9999)
            print('otp',number)
            print('email unvar',email)
            #if user try to resister again who is not verified user
            try:
            # if True:
                print('try')
                unvar_email=unverified_user.objects.get(email=email)
                print(unvar_email)
                unvar_email.first_name=req.get('first_name')
                unvar_email.last_name=req.get('last_name')
                unvar_email.password=make_password(req.get('password'))
                unvar_email.otp=number


                
                extime=datetime.datetime.now()+ datetime.timedelta(minutes = 5)
                print(datetime.datetime.now())
                print(extime)
                unvar_email.expire_time=extime



                unvar_email.save()
            #if user try to register 1st time
            except:
                print('except')
                data = form.save(commit = False)

                print(data.password)
                print(make_password(data.password))
                print(number)
                data.otp=number
                data.password=make_password(data.password)


       
                extime=datetime.datetime.now()+ datetime.timedelta(minutes = 5)
                print(datetime.datetime.now())
                print(extime)
                data.expire_time=extime
                data.save() 
            #send massege
            send_otp(email,number)

            
            return redirect('createuser:verify_otp',email=request.POST.get('email')) #createuser.verify_otp
        else:
            return render(request, "createuser/resistration1.html", {'form':form}) 
    form=registerForm()
    return render(request,'createuser/resistration1.html',{'form':form})




def check_email(request):
    response={}
    if request.method == 'GET':
        data=request.GET.get('email')
        print(data)
        if data:
            ql=CustomUser.objects.filter(email=data).first()
            print(ql)
            if ql:
                response['massege']='exist'
            else:
                response['massege']='not exist'
        
    return JsonResponse(response)



def verify_otp(request,email):
    if request.POST:
        print('email otp',email)
        print(request.POST.get('otp'))
        
        check_otp=request.POST.get('otp')
        unvar_email=unverified_user.objects.get(email=request.POST.get('email'))
        if unvar_email.otp == check_otp:
            
            from django.utils import timezone
            now = timezone.now()

            print(now)
            print(datetime.datetime.now())
            if now < unvar_email.expire_time:
                createuser=CustomUser.objects.create(email=unvar_email.email,first_name=unvar_email.first_name,last_name=unvar_email.last_name,password=unvar_email.password)
                print(createuser)
                unvar_email.delete()
                return redirect('index')
            else:
                massege='otp is expired'
        else:
                massege='given otp is not valid, please give valid otp'
        return render(request,'createuser/otp_varification.html',{'email':request.POST.get('email'),'massege':massege})


        print(email_data.otp)
    return render(request,'createuser/otp_varification.html',{'email':email})




import pytz

utc=pytz.UTC

def regenrate_otp(request):
    response={}
    if request.method == 'GET':
        email=request.GET.get('email')
        print(email)
        if email:
            unvar_email=unverified_user.objects.get(email=email)
            # generate otp
            number = random.randint(1000,9999)
            unvar_email.otp=number
            extime=datetime.datetime.now()+ datetime.timedelta(minutes = 5)
            print(datetime.datetime.now())
            print(extime)
            
            unvar_email.expire_time=extime.replace(tzinfo=utc)
            
            if send_otp(email,number):
                unvar_email.save()

                response['massege']='otp re-genrated'              
    return JsonResponse(response)




@login_required(login_url='createuser:login')
def user_logout(request):
    
    logout(request)
    return redirect('index')


                         })

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'createuser/login.html')
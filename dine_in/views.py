from django.shortcuts import render,redirect

from .models import table_booking
import random
# Create your views here.
from django.conf import settings 
from django.core.mail import send_mail 
from django.http import JsonResponse




def send_otp(emailid,otp):
    subject = 'you otp verification code is here'
    message = f'Hi {emailid}, your otp is {otp}.'
    email_from = settings.EMAIL_HOST_USER 
    reciever = [emailid, ] 
    print(email_from,'host')
    print(reciever,'recv')
    send_mail( subject, message, email_from, reciever )
    return True



def dine_in(request):
    # time=request.GET.get('time')
    if request.method =='POST':
        date=request.POST.get('date')
        updat_date=date.replace('/','-')
        email=request.POST.get('email')
        people=request.POST.get('people')
        print(updat_date)
        print(email)
        print(people)
        number = random.randint(1000,9999)
        try:
            is_Available=table_booking.objects.get(booking_time=updat_date,email=email,booked=False)
            is_Available.booking_time=updat_date
            is_Available.people=people
            is_Available.otp=number
            is_Available.save()
            print(is_Available,'avail')
        except:
            table_booking.objects.create(booking_time=updat_date,email=email,people=people,booked=False,otp=number)
        send_otp(email,number)
        return redirect('dine_in:otp_page',email=email)

    
    return render(request,'dine_in/dine_in.html')


def otp_verification_page(request,email):
    print('email')
    return render(request,'dine_in/otp_varification.html',{'email':email})


from django.utils import timezone
           

def verify_otp(request):
    if request.POST:
        print('email otp',request.POST.get('email'))
        print(request.POST.get('otp'))
        
        check_otp=request.POST.get('otp')
        email_booking=table_booking.objects.filter(email=request.POST.get('email')).last()
        if email_booking.otp == check_otp:
            
            email_booking.booked=True

            email_booking.save()
            
            return JsonResponse({'massege':'otp verified'})
            
    return None



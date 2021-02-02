from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import blog,subscribed_email

def blog_list(request):
    blogs=blog.objects.all()

    return render(request,'blogt/blog_page.html',{'blogs':blogs})


def single_blog(request,id):
    sblog=blog.objects.get(id=id)
    return render(request,'blogt/single-blog.html',{'singleblog':sblog})


def subscribe(request):
    email=request.GET.get('email')
    if email:
        try:
            subscribed_email.objects.get_or_create(email=email)
            print(email)
            return JsonResponse({'massege':'subscribed'})
        except:
            return JsonResponse({'massege':'something went wrong'})
    return JsonResponse({'massege':'please send mail'})
    
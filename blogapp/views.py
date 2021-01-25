from django.shortcuts import render

# Create your views here.
from .models import blog

def blog_list(request):
    blogs=blog.objects.all()

    return render(request,'blogt/blog_page.html',{'blogs':blogs})


def single_blog(request,id):
    sblog=blog.objects.get(id=id)
    return render(request,'blogt/single-blog.html',{'singleblog':sblog})



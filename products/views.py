from django.shortcuts import render
from .models import product,cart,category
from django.http import JsonResponse
from django.db.models import Q
from blogapp.models import blog

# Create your views here.


def index(request):
    products=product.objects.all()
    # request.COOKIES['ada']='ggggggggggggrrrrrrrr'
    # print(request.COOKIES)
    responce={'food':products}
    blogs=blog.objects.all().order_by('-id')[:2]
    responce['blogs']=blogs
    if request.user:
        value= cart.objects.filter(user=request.user).distinct().count()
        responce['items']=value

    return render(request,'index2.html',responce)




def all_food(request):
    products=product.objects.all()
    print(request.COOKIES)
    print(request.user,'user')
    responce={}
   
    cat=category.objects.all()
    responce['categories']=cat
    if request.user:
        value= cart.objects.filter(user=request.user).distinct().count()
        responce['items']=value
  
    return render(request,'products1.html',responce)


def base(request):
    return render(request,'base.html')


############## add product to cart######


def updatecart(request):
    responce={}
    if request.method == 'POST':
        data=request.POST
        print(request.user,data)
        if data.get('productid') != '' and request.user :
            print(data,'pre')
            if data.get('query')=='add':
                print(data,'post')

                ql=cart.objects.get_or_create(productid=data.get('productid'),user=data.get('user'))
                print(ql)
                responce={'resp':'success'}
                print(request.POST)
                print(request) 

            if data.get('query')=='delete':
                print(data)
                ql=cart.objects.get(productid=data.get('productid'),user=data.get('user'))
                print(ql)
                ql.delete()
                responce={'resp':'removed'}

       
        else:
            print(request.POST)
          
            responce={'resp':'data is empty'}

        if data.get('query'):
                print(data.get('query'))

    if request.user:
        value= cart.objects.filter(user=request.user).distinct().count()
        responce['items']=value
    return JsonResponse(responce)
################################################




def search(request):
    search=request.GET.get('search')
    print(search,'sera')
    data=search.split(' ')
    
    query = Q()
    cat_query=Q()
    for i in data:
        query |= Q(pname__icontains = i)
        print(i)

    for i in data:
        cat_query |= Q(name__icontains = i)
        print(cat_query,'cat')        
    cat_name=category.objects.filter(cat_query)

    for i in cat_name:
        query |= Q(categories = i)
    print(query,'query')
    allfood=product.objects.filter(query)
    print(allfood)
    return render(request,'search.html',{'food':allfood,'searchitem':search})


    #######################################


def order_cart(request):
    if request.user:
        response={}
        carts=cart.objects.filter(user=request.user).values_list('productid')
        response['cart']=product.objects.filter(id__in=carts)
        print(carts)

        
        value= cart.objects.filter(user=request.user).distinct().count()
        response['items']=value
        return render(request,'cart&checkout/cart.html',response)
    else:
        return redirect('login')


# incomplte
# def checkout(request):
#     return render(request,'checkout.html')
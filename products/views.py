from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Brand, Sub_Cat, Comment
from django.http import HttpResponseRedirect
from order.models import ShopCart

def light(request):
    product = Product.objects.filter(category= 2)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    count = shopcart.count()
   
    subcategory = Sub_Cat.objects.all()
    brands= Brand.objects.all()
    context= {
        'products' : product,
        'brands' : brands,
        'subcategory': subcategory,
        'count' : count, 

    }
    if request.method == "POST":
            sea= request.POST.get('brandvalueall')
            print(sea)


    return render(request, 'products/lights.html', context) 

def switch(request):
    product = Product.objects.filter(category= 1)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    count = shopcart.count()
   
    context= {
        'products' : product,
        'count' : count, 
    }
    return render(request, 'products/switchs.html', context)

def cable(request): 
    product = Product.objects.filter(category= 3)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    count = shopcart.count()
   
    context= {
        'products' : product,
        'count' : count, 
    }
    return render(request, 'products/cables.html', context)

def gadget(request):
    product = Product.objects.filter(category= 4)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    count = shopcart.count()
   
    
    
    context= {
        'products' : product,
        'count' : count, 
        
    }
    return render(request, 'products/gadgets.html', context)

def productview(request, product_id):
    current_user = request.user
    product= Product.objects.get(id= product_id)
    comments= Comment.objects.filter(product= product)

    
    division= product.category
    top_product= Product.objects.filter(category= division )
    
  
    
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    count = shopcart.count()
    if request.method == "POST":
        comment= Comment()
        comment.user= request.user
        comment.product = product
        comment.comment= request.POST.get("comment_box")
        comment.save()
        url = request.META.get('HTTP_REFERER')
        return HttpResponseRedirect(url) 
    context = {
        'product' : product,
        'shopcart' : shopcart, 
        'count' : count, 
        'top_product' : top_product, 
        'comments' : comments, 
        
      
    }
    url = request.META.get('HTTP_REFERER')
    return render(request, 'products/productview.html' , context)

def cate(request):
    return render(request, 'products/category.html')


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q= None
    if q:
        products= Product.objects.filter(title__icontains= q)
        productsAdd = Product.objects.filter(details__icontains= q)
        context = {'query': q, 'products': products, 'productsAdd': productsAdd}
    else:
        context = {}
    return render(request, 'products/result.html', context)



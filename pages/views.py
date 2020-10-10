from django.shortcuts import render
from products.models import Product, Category
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from order.models import ShopCart, Order , OrderProduct



def index(request):
    products= Product.objects.order_by('-list_date').filter(is_published= True)
    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    count = shopcart.count()
    context= {
        'products': products,
        'count' : count,  
        
    }
    return render(request, 'pages/index.html', context)
 

def cart(request):

    current_user = request.user
    shopcart = ShopCart.objects.filter(user_id = current_user.id)
    whole_total = 0
    count = shopcart.count()
    for each in shopcart: 
        whole_total+=each.price * each.quantity # add the total price of cart items

    context={
          
             'count':count,
             'shopcart':shopcart,
             'whole_total': whole_total

             }

    return render(request, 'order/cart.html' , context)



def addtocart(request , id):
    current_user = request.user
    qty = 0 
    
    checkproduct = ShopCart.objects.filter(user_id = current_user.id , product_id = id)
    if checkproduct: # if product exist in cart
        if request.method == 'POST':  # if there is a post
            qty = request.POST.get('qty')
            shopcart = ShopCart.objects.get(user_id = current_user.id , product_id = id )

            shopcart.quantity += int(qty)

            shopcart.save()
    else: # if doesnot exist
        if request.method == 'POST':  # if there is a post
            qty = request.POST.get('qty')
            shopcart = ShopCart()
            shopcart.user = current_user
            shopcart.product = Product.objects.get(id = id )
            shopcart.quantity = qty
            shopcart.save() 
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)


def removecart(request, id):
    url = request.META.get('HTTP_REFERER')
    shopcart= ShopCart.objects.filter(id= id)
    ShopCart.objects.filter(id= id).delete()

    
    return HttpResponseRedirect(url)
   
def checkout(request):
    current_user= request.user
    qty= 0
    whole_total = 0
    shopcart = ShopCart.objects.filter(user_id= current_user.id)
    count = shopcart.count()
    for each in shopcart:
        whole_total+=each.price * each.quantity # add the total price of cart items

    
    context={
          
             'count':count,
             'shopcart':shopcart,
             'whole_total' : whole_total

             }


    return render(request, 'order/checkout.html', context)


def order(request, id):
    if request.method == "POST":
        current_user = request.user
 
        whole_total = 0
        shopcart = ShopCart.objects.filter(user_id= current_user.id)
        for each in shopcart:
            whole_total+=each.price * each.quantity # add the total price of cart items
        #for order model
        order= Order()
        order.user= current_user
        order.code = "oppps"
        order.first_name = request.POST.get('first_name')
        order.last_name = request.POST.get('last_name')
        order.phone = request.POST.get('phone')
        order.email = request.POST.get('email')
        order.address = request.POST.get('address')
        order.address_desc = request.POST.get('address_desc')
        order.city = request.POST.get('city')
        order.total = whole_total
        order.status = request.POST.get('status')
        order.save()

        # for order product model
        for items in shopcart:
            orderproduct = OrderProduct()
            orderproduct.user = current_user
            # orderproduct.user = items.user
            orderproduct.order = Order.objects.get(id= order.id)
            # cart_items = ShopCart.objects.filter(user_id= current_user.id)
            
            # orderproduct.product = Product.objects.get(id = items.product.id)
            orderproduct.product = items.product
            orderproduct.quantity = items.quantity
            orderproduct.amount = 5
            orderproduct.price = 1200
            orderproduct.save()
    url = request.META.get('HTTP_REFERER')
    return HttpResponseRedirect(url)



















def about(request): 
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def termscondition(request):
    return render(request, 'pages/termscondition.html')


def returnpolicy(request): 
    return render(request, 'pages/returnpolicy.html')

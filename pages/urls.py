from django.urls import path
from . import views

urlpatterns= [
    
    path('', views.index, name= 'index'),

    path('cart', views.cart, name= 'cart'),
    path('addtocart/<int:id>/', views.addtocart, name= 'addtocart'),
    path('removecart/<int:id>/', views.removecart, name= 'removecart'),
    path('checkout/', views.checkout, name= 'checkout'),
    path('order/<int:id>/', views.order, name= 'order'),
    


    path('termscondition', views.termscondition, name= 'termscondition'),
    path('returnpolicy', views.returnpolicy, name= 'returnpolicy'),
    path('about', views.about, name= 'about'),
    path('contact', views.contact, name= 'contact'),

]  


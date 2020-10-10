from django.urls import path
from . import views

urlpatterns= [
    path('lights', views.light, name= 'light'),
    path('cables', views.cable, name= 'cable'),
    path('switchs', views.switch, name= 'switch'),
    path('gadgets', views.gadget, name= 'gadget'),
    # path('productview/', views.productview, name= 'dummy'),
    path('productview/<int:product_id>/', views.productview, name= 'productview'),
    path('cate', views.cate, name= 'cate'), 
    path('s/', views.search, name= 'search'),

  

      
 
]   
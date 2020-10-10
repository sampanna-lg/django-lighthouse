from django.contrib import admin
from .models import ShopCart, Order , OrderProduct

# Register your models here.
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'quantity', 'product')
    # list_editable = ('quantity',)
    list_display_link = ('id')
    
    list_per_page = 20

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email', 'address', 'city', 'phone', 'code')
    
    list_display_link = ('id', 'user')
    
    list_per_page = 20

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
    
    list_display_link = ('id', 'user')
    
    list_per_page = 20

admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)


from django.contrib import admin

from .models import Category, Product, Brand, Sub_Cat, Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price', 'is_published', 'is_topselling','is_new')
    list_editable = ('is_published', 'is_topselling', 'is_new' )
    list_display_link = ('id', 'title', 'category')
    search_fields = ('name', 'email')
    list_per_page = 20



class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_editable = ('slug',)
    list_display_link = ('name')
    search_fields = ('name', 'email')
    list_per_page = 20


class SubCatAdmin(admin.ModelAdmin):
    list_display = ('sub',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment',)


admin.site.register(Category, CatAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sub_Cat, SubCatAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Comment, CommentAdmin)
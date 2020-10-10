from django.db import models
from datetime import datetime
from SampannaLighthouse.utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

BRANDS= [
    ('Samsung', 'Samsung'),
    ('LG', 'LG'),
    ('Sony', 'Sony'),

]

CATEGORIES = [
    ('LED', 'LED'),
    ('Ceiling Lights', 'Ceiling Lights'),
    ('Pannel Lights', 'Pannel Lights'),
    ('Lightbulb', 'Lightbulb'),
    ('Smart Controller', 'Smart Controller'),
]


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length= 250, unique= True) 

    def __str__(self):
        return str(self.name)
 
class Brand(models.Model):
    brand = models.CharField(max_length=200, choices=BRANDS, default="")

    def __str__(self):
        return str(self.brand)

class Sub_Cat(models.Model):
    main_category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    sub = models.CharField(max_length=200, choices=CATEGORIES, default="")

    def __str__(self):
        return str(self.sub)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING)
    brand_name = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    sub_category = models.ForeignKey(Sub_Cat, on_delete=models.SET_NULL, blank=True, null= True)

    
    title = models.CharField(max_length= 200)
    description= models.CharField(max_length=200) 
    details= models.TextField()
    price = models.IntegerField()
    # slug = models.SlugField(max_length= 250, unique= True) 
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
   
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank= True)
    list_date = models.DateTimeField(default= datetime.now, blank= True)
    is_published = models.BooleanField(default=True)
    is_topselling = models.BooleanField(default=False)
    
 
    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("productview", args= [self.id]) 


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment= models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment



































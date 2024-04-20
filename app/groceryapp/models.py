from typing import Any
from django.db import models

# Create your models here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

class category(models.Model):
     name = models.CharField(max_length = 255,default="Default value for q1" )
     image = models.ImageField(upload_to='img/')

     def __str__(self):
         return self.name  

     
class product(models.Model):
    category = models.ForeignKey(category,on_delete= models.CASCADE,null = False,default= '')
   
    image = models.ImageField(upload_to='img/')
    name = models.CharField(max_length = 255 )
    price = models.IntegerField(default = 0)
    date = models.DateField(auto_now_add = True)
    q1 = models.CharField(max_length = 255 , default="Default value for q1")
    q2 = models.CharField(max_length = 255,default="Default value for q1")
    q3 = models.CharField(max_length = 255,default="Default value for q1")
    
    description_features = models.TextField(default="Not provided")
    shelflife = models.CharField(max_length = 255,default="Default value for q1")
    manufacture_detail = models.TextField(default="Not provided")
    FSSAI = models.IntegerField(default=0)
    description = models.TextField(default="Not provided")
    seller = models.CharField(max_length = 255,default="Default value for q1")

   
    def __str__(self):
       return self.name
 
    
class product2(models.Model):
    category = models.ForeignKey(category,on_delete= models.CASCADE,null = False,default= '')
   
    image = models.ImageField(upload_to='img/')

    name = models.CharField(max_length = 255,default="Default value for q1" )
    price = models.IntegerField(default = 0)
    image2 =  models.ImageField(upload_to='img/')
    q1 = models.CharField(max_length = 255,default="Default value for q1")
    quantity = models.IntegerField(default = 1)

   
    description_features = models.TextField(default="Not provided")
    shelflife = models.CharField(max_length = 255,default="Default value for q1")
    manufacture_detail = models.TextField(default="Not provided")
    FSSAI = models.IntegerField(default = 0)
    description = models.TextField(default="Not provided")
    seller = models.CharField(max_length = 255,default="Default value for q1")

   
    def __str__(self):
       return self.name
    

class Usercreateform(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'exists' : 'this already exists'})

    class Meta:
        model = User
        fields = {'email','username','password1','password2'}
   
          

    def save(self,commit= True):
        user = super(UserCreationForm,self).save(commit=False)
        user .email = self.cleaned_data['email']
        if commit:
            user.save()
        return user  
    def clean_email(self):
        if User.objects.filter(email= self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']
    

class contact_us(models.Model):
    name=models.CharField(max_length = 255)
    email=models.EmailField(max_length = 100)
    message=models.TextField()
    def __str__(self):
       return self.name
import datetime    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(product2)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    landmark = models.CharField(max_length=255)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(default=datetime.datetime.today)
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('returned', 'Returned'),
    )
    delivery_boy = models.CharField(max_length=100,default = 'not allotted')
    delivery_boy_number = models.IntegerField(default = '0')
    order_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')


    def __str__(self):
        return str(self.user)
    
       
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class details(models.Model):
   
   
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    )
    
    delivery_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    
    delivery_boy = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ram')
    
    def __str__(self):
        return str(self.delivery_status)

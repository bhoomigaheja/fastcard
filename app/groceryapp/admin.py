from django.contrib import admin

# Register your models here.
from . models import category,product,product2,contact_us,Order,details




admin.site.register(category)

admin.site.register(product)

admin.site.register(product2)

admin.site.register(contact_us)
admin.site.register(Order)
admin.site.register(details)


















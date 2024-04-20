from django import forms
from groceryapp.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'address', 'city', 'state', 'pincode', 'landmark']

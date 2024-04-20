
from django import forms
from groceryapp.models import Order

from django import forms

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'required': True}),
            'last_name': forms.TextInput(attrs={'required': True}),
            'phone_number': forms.TextInput(attrs={'required': True}),
            'address': forms.TextInput(attrs={'required': True}),
            'city': forms.TextInput(attrs={'required': True}),
            'state': forms.TextInput(attrs={'required': True}),
            'pincode': forms.TextInput(attrs={'required': True}),
            'landmark': forms.TextInput(attrs={'required': True}),
        }

from django import forms

from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('origin', 'destination', 'weight', 'length', 'width', 'height',  'special_instructions')

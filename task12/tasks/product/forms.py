from django import forms
from .models import product

class productform(forms.ModelForm):
    class Meta:
        model = product
        fields = ['title','descr','price']


class rawform(forms.Form):
    title = forms.CharField(required=False)
    descr = forms.CharField(label='type here ')
    price = forms.DecimalField(initial=0.00)
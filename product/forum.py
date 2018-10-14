from django import forms
from .models import productModel

class productForm(forms.ModelForm):
    class Meta:
        model=productModel
        fields=['description','price','quantity']
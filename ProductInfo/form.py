from django import forms
from django.forms import ModelForm
from .models import ProductDetail

class ProductDetailForm(ModelForm):
    class Meta:
        model = ProductDetail
        fields = '__all__'
from django import forms



class ProductForm(forms.Form):
    title = forms.CharField()
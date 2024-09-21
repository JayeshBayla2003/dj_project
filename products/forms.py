from django import forms

from .models import Products


# class ProductForm(forms.Form):
#     title = forms.CharField() 

class ProductModelForm(forms.ModelForm):
    # title = forms.CharField() 
    class Meta:
        model = Products
        fields = [
            'title',
            'content',
        ]
    
    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data)<4:
            raise forms.ValidationError("This is not long enough")

        return data
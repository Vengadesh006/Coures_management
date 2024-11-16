from django import forms
from .models import Coures , Card


class Coures_form(forms.ModelForm) :

    class Meta : 
        
        model = Coures

        fields = ['coures','duration','fees','gst','final_fees']

        widgets = {
                "coures": forms.TextInput(attrs={'class': 'form-control'}),
                "duration":forms.TextInput(attrs={'class': 'form-control'}),
                "fees":forms.NumberInput(attrs={'class': 'form-control'}),
                "gst":forms.NumberInput(attrs={'class': 'form-control'}),
                "final_fees":forms.NumberInput(attrs={'class': 'form-control'})
                }

class Cart_form(forms.ModelForm) :

    class Meta : 
        
        model = Card

        fields = '__all__'

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),

            "content":forms.TextInput(attrs={'class': 'form-control'}),
            
            "image":forms.FileInput(attrs={'class': 'form-control'}),
             }




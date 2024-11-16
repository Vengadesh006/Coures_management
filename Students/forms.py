from django import forms 
from .models import Student , FeedBack


class Student_Forms(forms.ModelForm) :

    class Meta : 
        
        model = Student
        
        fields = ['name' , 'address' , 'moblie', 'selected_coures','paid_fees','pictuer','placement']

        widgets = {
                "name":forms.TextInput(attrs={'class': 'form-control'}) ,
                "address":forms.TextInput(attrs={'class': 'form-control'}),
                "moblie" : forms.TextInput(attrs={'class': 'form-control'}),
                "selected_coures" : forms.Select(attrs={'class': 'form-control code'}) ,
                # "placement" : forms.Select(attrs={'class': 'form-control code'}) ,
                "paid_fees" : forms.NumberInput(attrs={'class': 'form-control'}) , 
                'pictuer' : forms.FileInput(attrs={'class': 'form-control'})
                }


class FeedBack_Form(forms.ModelForm) : 
    
    class Meta : 
        
        model = FeedBack
        
        fields = '__all__'

        
        widgets = {
                "Title":forms.TextInput(attrs={'class': 'form-control'}) ,
                "Body":forms.Textarea(attrs={'class': 'form-control'}),
                "slug" : forms.TextInput(attrs={'class': 'form-control'}),
        }
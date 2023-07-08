from django import forms
from .models import Car

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
    date_of_birth = forms.DateField()
    address = forms.CharField(max_length=200, label='Street Name')
    pincode = forms.CharField(max_length=6)
    city = forms.CharField(max_length=20)
    state = forms.CharField(max_length=20)
    country_code = forms.CharField(max_length=2)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField()

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model_name', 'manufacturer', 'color', 'manufacturing_date']

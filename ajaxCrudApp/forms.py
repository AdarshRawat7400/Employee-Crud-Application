from cProfile import label
from unicodedata import name
from django  import forms
from .models import Employee

class EmployeeRegistration(forms.ModelForm):
    class Meta:
        model = Employee
        labels = {
            'employee_name': 'Name',
            'employee_email': 'Email',
            'employee_location': 'Location',
            'employee_phone': 'Phone',
        }
        fields = ('id',
                  'employee_name',
                  'employee_email',
                  'employee_location',
                  'employee_phone')

        widgets = { 
            'employee_name': forms.TextInput(attrs={'class': 'form-control',
                                                    'id':'nameid'}),
            'employee_email': forms.EmailInput(attrs={'class': 'form-control'
                                                     , 'id':'emailid'}),
            'employee_location': forms.TextInput(attrs={'class': 'form-control'
                                                         , 'id':'locationid'}),
            'employee_phone': forms.TextInput(attrs={'class': 'form-control'
                                                        , 'id':'phoneid'}),
            }                                     
                       
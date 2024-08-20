from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Employee
from .models import Document


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Please enter you password'}))

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'salary', 'bonus', 'phone', 'role', 'dept', 'hire_date']
        widgets = {
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }


class InternalMessageForm(forms.Form):
    email_address = forms.EmailField(label='To Email Address', required=True)
    cc = forms.EmailField(label='CC Email Address', required=False)
    subject = forms.CharField(label='Subject', max_length=100)
    reason = forms.CharField(label='Reason', widget=forms.Textarea)



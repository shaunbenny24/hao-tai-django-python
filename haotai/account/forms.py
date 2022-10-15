
from django import forms

# Create your models here.

class LoginForm(forms.Form):
  
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"  username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"  password"}))
 


class SignUpForm(forms.Form):
  
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"  username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"  email address"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"  password"}))
    passwordre = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":" confirm  password"}))

# class login(forms.Form):
  
#     username = forms.CharField(max_length = 200)
#     password = forms.CharField(widgets=forms.PasswordInput())
 




    





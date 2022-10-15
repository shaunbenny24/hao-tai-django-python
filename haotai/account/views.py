from django.shortcuts import render
from .forms import LoginForm,SignUpForm
# Create your views here.
def login(request):
    form = LoginForm()
    return render(request,'account/login.html',{'form':form})

def signup(request):
    sign = SignUpForm()
    return render(request,'account/signup.html',{'sign':sign})


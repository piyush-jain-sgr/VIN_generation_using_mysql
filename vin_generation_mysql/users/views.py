from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterform


def register(request):
    if request.method=="POST":
        form=UserRegisterform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login')
    else:
        form=UserRegisterform()
    return render(request,'users/register.html',{'form':form})

def login_signup(request):
    return render(request, 'users/home.html')
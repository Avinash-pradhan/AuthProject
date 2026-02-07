from django.shortcuts import render,redirect
from authapp.forms import SignUpForm
from authapp.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def signup_view(request):
    signup_form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'user is created Successfully...')
            return redirect('login')
    return render(request,'signup.html',{'form':signup_form})
def about_view(request):
    return render(request,'about.html')

@login_required() #@login_required(login_url='signup')
def home_view(request):
    return render(request,'home.html')
def recent_view(request):
    return render(request,'recent.html')
def login_view(request):                                      
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            u=form.cleaned_data['username']
            p=form.cleaned_data['password']
            user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            messages.success(request,'Logged in successfully....')
            return redirect('home')
        else:
            messages.warning(request,'invalid username or password....!!')
    return render(request,'login.html',{'form':form})
def logout_view(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('login')
from django.shortcuts import render,redirect
from authapp.forms import SignUpForm
from authapp.forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,'user is created Successfully...')
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request,'signup.html',{'form':form})
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

@login_required
def new_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important! Keeps the user logged in
            messages.success(request, "Password has Changed Successfully")
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
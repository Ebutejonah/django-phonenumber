from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser, Profile
from .forms import ProfileForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def indexpage(request):
    pass

def register(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.info(request,'Passwords must match!')
            return redirect('/')
        elif len(password1) < 8:
            messages.info(request,'Password must be at least 8 characters')
            return redirect('/')
        elif CustomUser.objects.filter(email=email).exists():
            messages.info(request,'An account with the email you provided already exists')
            return redirect('/')
        else:
            user = CustomUser.objects.create_user(email=email,password=password1)
            user.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            return redirect('/login')    
    return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            account = CustomUser.objects.get(email=email)
            if password != account.password:
                messages.error(request,'Invalid Email or Password')
        except:
            CustomUser.DoesNotExist()
            messages.error(request,'Invalid Email or Password')
        user = auth.authenticate(email=email,password=password) 
        if user is not None:
            auth.login(request,user)
            return redirect('/profile')
    return render(request,'login.html')

@login_required()
def profile(request):
    email = request.user.email
    user = CustomUser.objects.filter(email=email).first()
    profile = Profile.objects.filter(user=user).first()
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/checkout')
        else:
            messages.error(request,'Error in form')
            return redirect('/profile')
    return render(request,'profile.html',{'form':form})

@login_required()
def checkout(request):
    email = request.user.email
    user = CustomUser.objects.filter(email=email).first()
    profile = Profile.objects.filter(user=user).first()
    context= {'user':user,'profile':profile}
    return render(request,'checkout.html',context)

@login_required()
def success(request):
    return HttpResponse(request,'Payment Successful')

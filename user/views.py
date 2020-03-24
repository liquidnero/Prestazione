
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request,"user/login.html")

def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f"Your account has been created! You are now able to login")
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request,"user/registration.html",{"form": form})
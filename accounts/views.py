from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ticket submitted successfully.')
        else:
            messages.error(request, 'Ticket didnt submit.')
    form = ContactForm()
    return render(request, 'accounts/contact.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(**cd)
            if user:
                login(request, user)
                return redirect('blog:home')
            messages.error(request, 'Wrong credentials')
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_user(request):
    return render(request, 'accounts/logout.html')


def signup_user(request):
    return render(request, 'accounts/signup.html')

from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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
    if not request.user.is_authenticated:
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
    return redirect('blog:home')


@login_required(login_url='accounts:login')
def logout_user(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))


def signup_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Signup completed, please Login')
                return redirect('accounts:login')
            messages.error(request, 'Wrong Credentials')
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})
    return redirect('blog:home')

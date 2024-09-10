from django.shortcuts import render, redirect
from.models import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def home_view(request):
    items = Item.objects.all()
    return render(request, 'app/home.html', {'items' : items})

def login_view(request):
    
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'app/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'app/register.html', {'form': form})
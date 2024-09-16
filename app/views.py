from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AuthenticationForm, ItemForm

# Create your views here.
def home_view(request):
    items = Item.objects.all()
    return render(request, 'app/home.html', {'items' : items})


def dashboard_view(request):
    user_count = User.objects.count()
    item_count = Item.objects.count()
    items_requests_count = ItemRequest.objects.count()
    
    context = {
        'user_count': user_count,
        'item_count': item_count,
        'items_requests_count': items_requests_count
    }
    return render(request, 'app/dashboard.html', context)
    

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'account/login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'account/login.html', {'form': form, 'error': 'Invalid form data'})
    else:
        form = AuthenticationForm()

    return render(request, 'account/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'account/register.html', {'form': form})


@login_required
def some_form_view(request):
    if request.method == 'POST':
        form = SomeForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('success_url')  
    else:
        form = SomeForm()
    return render(request, 'form_template.html', {'form': form})


def users_view(request):
    return render(request, 'app/users.html')

def items_view(request):
    return render(request, 'app/items.html')

def items_requests_view(request):
    return render(request, 'app/item_requests.html')

def restocks_view(request):
    return render(request, 'app/restocks.html')

def create_items_view(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = ItemForm()
        
    return render(request, 'app/create_items.html', {'form': form})
    
    
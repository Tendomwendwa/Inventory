from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, AuthenticationForm, ItemForm, StaffForm, ItemRequestForm, RestockForm

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


def staff_view(request):
    staff_list = Staff.objects.all()
    return render(request, 'app/staff.html', {'staff': staff_list})

def items_view(request):
    item_list = Item.objects.all()
    return render(request, 'app/items.html', {'items': item_list})

def items_requests_view(request):
    items_requests_list = ItemRequest.objects.all()
    return render(request, 'app/item_requests.html', {'items_requests': items_requests_list})

def restocks_view(request):
    restock_list = Restock.objects.all()
    return render(request, 'app/restocks.html', {'restocks': restock_list})

def create_items_view(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('items')
            
    else:
        form = ItemForm()
        
    return render(request, 'app/create_items.html', {'form': form})

def create_staff_view(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('staff')
        
    else:
        form = StaffForm()
        
    return render(request, 'app/create_staff.html', {'form': form})


def create_item_requests_view(request):
    if request.method == "POST":
        form = ItemRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_requests')
    else:
        form = ItemRequestForm()
    return render(request, 'app/create_item_requests.html', {'form': form})

def create_restocks_view(request):
    if request.method == "POST":
        form = RestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restocks')
    else:
        form = RestockForm()
    return render(request, 'app/create_restocks.html', {'form': form})
    

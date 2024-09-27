from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import *


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label="username",
        help_text=None
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Password",
        help_text=None
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password'].help_text = None


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field for the user

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Fields for registration

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'item_status', 'quantity']
        

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'department']     

class ItemRequestForm(forms.ModelForm):
    class Meta:
        model = ItemRequest
        fields = ['staff', 'item', 'request_status']
        
class RestockForm(forms.ModelForm):
    class Meta:
        model = Restock
        fields = ['item', 'quantity']
        
        
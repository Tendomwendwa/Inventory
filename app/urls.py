from django.urls import path
from .views import home_view, login_view, register_view
from .views import RegisterUserView, UserProfileView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('api/register/', RegisterUserView.as_view(), name='register'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('api/login/', obtain_auth_token, name='login'),
    
    
]
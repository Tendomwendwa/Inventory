from django.urls import path
from .views import home_view
from .views import login_view, register_view, users_view, items_view, items_requests_view, dashboard_view, restocks_view

urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('users/', users_view, name='users'),
    path('items/', items_view, name='items'),
    path('item_requests/', items_requests_view, name='item_requests'),
    path('restocks/', restocks_view, name='restocks'),
]
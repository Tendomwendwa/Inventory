from django.urls import path
from .views import home_view, login_view, register_view, staff_view, items_view, items_requests_view, dashboard_view, restocks_view
from .views import items_requests_view, dashboard_view, restocks_view, create_items_view, create_staff_view
urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('staff/', staff_view, name='staff'),
    path('items/', items_view, name='items'),
    path('item_requests/', items_requests_view, name='item_requests'),
    path('restocks/', restocks_view, name='restocks'),
    path('create_items/', create_items_view, name='create_items'),
    path('create_staff/', create_staff_view, name='create_staff'),
]
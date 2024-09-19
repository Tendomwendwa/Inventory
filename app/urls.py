from django.urls import path
from .views import home_view, login_view, register_view, staff_view, items_view, items_requests_view, dashboard_view, restocks_view
from .views import items_requests_view, dashboard_view, restocks_view, reports_view
from .views import create_items_view, create_staff_view, create_item_requests_view, create_restocks_view
from .views import edit_staff_view, delete_staff_view, edit_items_view, delete_items_view, edit_restocks_view, delete_restocks_view, edit_items_requests_view, delete_items_requests_view

urlpatterns = [
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('staff/', staff_view, name='staff'),
    path('items/', items_view, name='items'),
    path('item_requests/', items_requests_view, name='item_requests'),
    path('restocks/', restocks_view, name='restocks'),
    path('reports/', reports_view, name='reports'),
    path('create_items/', create_items_view, name='create_items'),
    path('create_staff/', create_staff_view, name='create_staff'),
    path('create_item_requests/', create_item_requests_view, name='create_item_requests'),
    path('create_restocks/', create_restocks_view, name='create_restocks'),
    
    path('staff/edit/<int:staff_id>/', edit_staff_view, name='edit_staff'),
    path('staff/delete/<int:staff_id>/', delete_staff_view, name='delete_staff'),
    path('items/edit/<int:item_id>/', edit_items_view, name='edit_items'),
    path('items/delete/<int:item_id>/', delete_items_view, name='delete_items'),
    path('restocks/edit/<int:restock_id>/', edit_restocks_view, name='edit_restocks'),
    path('restocks/delete/<int:restock_id>/', delete_restocks_view, name='delete_restocks'),
    path('items_requests/edit/<int:item_request_id>/', edit_items_requests_view, name='edit_items_requests'),
    path('items_requests/delete/<int:item_request_id>/', delete_items_requests_view, name='delete_items_requests'),
    

]
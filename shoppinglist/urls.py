from django.urls import path
from . import views
from .views import register

urlpatterns = [
    path('shopping_list/<int:list_id>/', views.shopping_list_view, name='shopping_list_view'),
    path('add_item/<int:list_id>/', views.add_list_item, name='add_list_item'),
    path('edit_item/<int:item_id>/', views.edit_list_item, name='edit_list_item'),
    path('delete_item/<int:item_id>/', views.delete_list_item, name='delete_list_item'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', register, name='register'),
]

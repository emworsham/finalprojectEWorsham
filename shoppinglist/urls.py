from django.urls import path
from . import views
from .views import register, create_store, custom_logout, nutritional_information
from django.contrib.auth.views import LogoutView
from django.urls import path, include

urlpatterns = [
    path('shopping_list/<int:list_id>/', views.shopping_list_view, name='shopping_list_view'),
    path('add_item/<int:list_id>/', views.add_list_item, name='add_list_item'),
    path('edit_item/<int:item_id>/', views.edit_list_item, name='edit_list_item'),
    path('delete_item/<int:item_id>/', views.delete_list_item, name='delete_list_item'),
    path('register/', register, name='register'),
    path('create_store/', create_store, name='create_store'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),
    path('delete_store/<int:store_id>/', views.delete_store, name='delete_store'),
    path('create_shopping_list/<int:store_id>/', views.create_shopping_list, name='create_shopping_list'),
    path('view_shopping_list/<int:shopping_list_id>/', views.view_shopping_list, name='view_shopping_list'),
    path('delete_shopping_list/<int:list_id>/', views.delete_shopping_list, name='delete_shopping_list'),
    path('logout/', custom_logout, name='logout'),
    path('nutritional-information/', nutritional_information, name='nutritional_information'),
]

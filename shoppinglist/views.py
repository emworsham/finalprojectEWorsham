from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Store, ShoppingList, ListItem, ShoppingListItem, Profile
from .forms import ListItemForm, StoreForm, UserRegisterForm, ShoppingListItemForm
from django.forms.models import inlineformset_factory
from django.conf import settings
from .forms import ShoppingListForm
import requests


def home(request):
    return render(request, 'home.html')
@login_required
def dashboard(request):
    # Assuming each Store is linked to a User
    stores = Store.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'stores': stores})


@login_required
def shopping_list_view(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, id=list_id, user=request.user)
    items = ListItem.objects.filter(shopping_list=shopping_list)
    return render(request, 'shopping_list.html', {'shopping_list': shopping_list, 'items': items})


@login_required
def add_list_item(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, id=list_id, user=request.user)

    if request.method == 'POST':
        form = ListItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.shopping_list = shopping_list
            new_item.save()
            return redirect('shopping_list_view', list_id=shopping_list.id)
    else:
        form = ListItemForm()

    return render(request, 'add_list_item.html', {'form': form, 'shopping_list': shopping_list})


@login_required
def edit_list_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id, shopping_list__user=request.user)

    if request.method == 'POST':
        form = ListItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('shopping_list_view', list_id=item.shopping_list.id)
    else:
        form = ListItemForm(instance=item)

    return render(request, 'edit_list_item.html', {'form': form, 'item': item})


@login_required
def delete_list_item(request, item_id):
    item = get_object_or_404(ListItem, id=item_id, shopping_list__user=request.user)
    list_id = item.shopping_list.id
    item.delete()
    return redirect('shopping_list_view', list_id=list_id)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user,
                              street_address=form.cleaned_data['street_address'],
                              address_2=form.cleaned_data['address_2'],
                              city=form.cleaned_data['city'],
                              state=form.cleaned_data['state'],
                              zip_code=form.cleaned_data['zip_code'],
                              phone_number=form.cleaned_data['phone_number'])
            profile.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def create_store(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.user = request.user  # Set the store's user to the current user
            store.save()
            return redirect('dashboard')  # Redirect to the dashboard after creating the store
    else:
        form = StoreForm()

    return render(request, 'shoppinglist/create_store.html', {'form': form})

@login_required
def edit_store(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StoreForm(instance=store)

    return render(request, 'shoppinglist/edit_store.html', {'form': form})

@login_required
def delete_store(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    if request.method == 'POST':
        store.delete()
        return redirect('dashboard')
    return render(request, 'shoppinglist/delete_store.html', {'store': store})

@login_required
def create_shopping_list(request, store_id):
    store = get_object_or_404(Store, id=store_id, user=request.user)
    shopping_list = ShoppingList(store=store)  # Create a new ShoppingList instance
    ShoppingListItemFormSet = inlineformset_factory(ShoppingList, ShoppingListItem, form=ShoppingListItemForm, extra=1)

    if request.method == 'POST':
        formset = ShoppingListItemFormSet(request.POST, instance=shopping_list)

        if formset.is_valid():
            shopping_list.save()  # First, save the ShoppingList instance
            formset.save()  # Now save the formset
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        formset = ShoppingListItemFormSet(instance=shopping_list)

    return render(request, 'shoppinglist/create_shopping_list.html', {'formset': formset, 'store': store})

@login_required
def view_shopping_list(request, shopping_list_id):
    shopping_list = get_object_or_404(ShoppingList, id=shopping_list_id)

    # Ensure the user has permission to view this shopping list
    if shopping_list.store.user != request.user:
        return redirect('dashboard')

    items = ShoppingListItem.objects.filter(shopping_list=shopping_list)
    return render(request, 'shoppinglist/view_shopping_list.html', {'shopping_list': shopping_list, 'items': items})

@login_required
def delete_shopping_list(request, list_id):
    shopping_list = get_object_or_404(ShoppingList, id=list_id)

    # Check if the current user is allowed to delete this shopping list
    if request.user != shopping_list.store.user:
        return redirect('some_error_page')  # Redirect to an error page or the dashboard

    if request.method == 'POST':
        shopping_list.delete()
        return redirect('dashboard')  # Redirect to the dashboard after deletion

    return render(request, 'shoppinglist/confirm_delete.html', {'shopping_list': shopping_list})

def custom_logout(request):
    logout(request)
    return redirect('login')

def nutritional_information(request):
    nutrition_data = None
    query = None

    if request.method == 'POST':
        query = request.POST.get('food_item')
        api_url = f'https://api.api-ninjas.com/v1/nutrition?query={query}'
        response = requests.get(api_url, headers={'X-Api-Key': settings.API_NINJAS_API_KEY})

        if response.status_code == 200:
            nutrition_data = response.json()
        

    return render(request, 'nutritional_information.html', {'nutrition_data': nutrition_data, 'query': query})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Store
from django.contrib.auth.decorators import login_required
from .models import ShoppingList, ListItem
from .forms import ListItemForm
from .forms import UserRegisterForm
from .models import Profile

def home(request):
    return render(request, 'home.html')
def dashboard(request):
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


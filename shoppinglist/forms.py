# shoppinglist/forms.py

from django import forms
from .models import ListItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Store
from .models import ShoppingList
from .models import ShoppingListItem
from .models import Profile

class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ['content', 'is_completed']  # Adjust fields as per your ListItem model



class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    street_address = forms.CharField()
    address_2 = forms.CharField(required=False)
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.CharField()
    phone_number = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'street_address', 'address_2', 'city', 'state', 'zip_code', 'phone_number']

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name']


class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingList
        fields = ['name', 'items']

class ShoppingListItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingListItem
        fields = ['name']

    name = forms.CharField(label='Item')
# shoppinglist/forms.py

from django import forms
from .models import ListItem

class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields = ['content', 'is_completed']  # Adjust fields as per your ListItem model

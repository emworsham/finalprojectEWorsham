from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Store(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ShoppingList(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def current_date():
        return datetime.now().strftime("%m-%d-%Y")

    name = models.CharField(max_length=100, default=current_date)
    items = models.TextField(default="")

class ShoppingListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, related_name='shopping_list_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Example field

    def __str__(self):
        return self.name

class ListItem(models.Model):
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

# Generated by Django 5.0 on 2023-12-13 20:00

import shoppinglist.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0006_alter_shoppinglist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(default=shoppinglist.models.ShoppingList.current_date, max_length=100),
        ),
    ]

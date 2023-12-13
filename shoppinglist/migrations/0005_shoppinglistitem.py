# Generated by Django 5.0 on 2023-12-13 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoppinglist', '0004_alter_shoppinglist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('shopping_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_list_items', to='shoppinglist.shoppinglist')),
            ],
        ),
    ]

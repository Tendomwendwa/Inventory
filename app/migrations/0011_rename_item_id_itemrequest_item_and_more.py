# Generated by Django 5.1 on 2024-09-18 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_restock_alter_item_item_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemrequest',
            old_name='item_id',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='itemrequest',
            old_name='user_id',
            new_name='staff',
        ),
    ]

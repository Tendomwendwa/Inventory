# Generated by Django 5.1 on 2024-09-21 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_item_item_status_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
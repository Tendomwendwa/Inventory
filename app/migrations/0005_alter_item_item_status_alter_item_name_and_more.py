# Generated by Django 5.1 on 2024-08-29 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_status',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.CharField(max_length=10),
        ),
    ]

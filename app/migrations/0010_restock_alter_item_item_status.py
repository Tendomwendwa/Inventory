# Generated by Django 5.1 on 2024-09-18 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_user_staff_alter_item_item_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('restock_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='item_status',
            field=models.CharField(choices=[('available', 'Available'), ('out_of_stock', 'Out of Stock')], default='available', max_length=20),
        ),
    ]

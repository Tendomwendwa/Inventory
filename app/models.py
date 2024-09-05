from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=20)
    item_status = models.CharField(max_length=15)
    quantity = models.CharField(max_length=10)
   
    def __str__(self):
        return str(self.name)


class User (models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


class ItemRequest (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    request_status = models.CharField(max_length=20)
    requested_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now_add=True)    
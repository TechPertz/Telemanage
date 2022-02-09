from django.db import models

# Create your models here.

class Store(models.Model):
    # store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    store_state = models.CharField(max_length=100)
    store_pincode = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name

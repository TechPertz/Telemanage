from pyexpat import model
from django.db import models

# Create your models here.

class Ticket(models.Model):
    ticket_nos = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=255, default="")
    user_name = models.CharField(max_length=255, default="")
    issue = models.CharField(max_length=255, default="")
    ticket_status = models.CharField(max_length=255, default="Active")

    def __str__(self):
        return self.user_name + "/" + str(self.ticket_nos)

class Vouch(models.Model):
    user_id = models.CharField(max_length=255, default="")
    user_name = models.CharField(max_length=255, default="")
    vouch = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.user_name + "/" + str(self.id)

class Form(models.Model):
    user_id = models.CharField(max_length=255, default="")
    user_name = models.CharField(max_length=255, default="")
    store = models.ForeignKey('home.Store', default=None, on_delete=models.CASCADE)
    enquiry = models.CharField(max_length=255, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name + "/" + str(self.store.id) + "/" + str(self.created_at) 

class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_address = models.CharField(max_length=100)
    store_state = models.CharField(max_length=100)
    store_pincode = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name

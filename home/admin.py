from ast import For
from django.contrib import admin
from .models import *
# Register your models here.

class StoresAdmin(admin.ModelAdmin):
    list_display = ["store_name", "id", "store_state", "store_pincode"]

admin.site.register(Store, StoresAdmin)
admin.site.register(Form)
admin.site.register(Ticket)
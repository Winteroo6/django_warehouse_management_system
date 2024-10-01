from django.contrib import admin

# Register your models here.

from .models import *



admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Inventory)
admin.site.register(Inbound)
admin.site.register(Outbound)
admin.site.register(Tag)
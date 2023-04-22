from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product, Order, Gallery

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'quantity', 'Type', 'Brand')
    list_filter = ['category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product','staff', 'order_quantity', 'date',)

admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'Inventory Dashboards'
admin.site.register(Order, OrderAdmin)
admin.site.register(Gallery)



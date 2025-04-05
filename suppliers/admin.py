from django.contrib import admin

from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name','description','created_at','updated_at']

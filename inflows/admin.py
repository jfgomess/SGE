from django.contrib import admin
from inflows.models import Inflow

@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = ['supplier','product','quantity','description']

from django.contrib import admin
from .models import Address

class AddressAdmin(admin.ModelAdmin):
    list_display = ('member', 'name', 'address', 'created')
    list_filter = ('created',)
    list_per_page = 20
    search_fields = ['name', 'address']

admin.site.register(Address, AddressAdmin)

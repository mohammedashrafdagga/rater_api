from django.contrib import admin
from .models import Product, Rater
# Register your models here.


class RaterAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'starts']
    list_filter = ['user', 'product']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'descriptions']
    search_fields = ['name', 'descriptions']
    list_filter = ['name', 'descriptions']


admin.site.register(Rater, RaterAdmin)
admin.site.register(Product, ProductAdmin)

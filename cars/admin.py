from django.contrib import admin
from .models import Car, Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'model', 'brand',
        'factory_year', 'model_year',
        'plate', 'value',
    )
    search_fields = ('name', 'brand',)

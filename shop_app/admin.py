from django.contrib import admin
from shop_app.models import Category, Product

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    list_display_links = ['id']
    list_filter = ['name']
    search_fields = ['name']
    fields = ['id', 'name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'date', 'price', 'product_category']
    list_display_links = ['id', 'name']
    list_filter = ['date']
    search_fields = ['date', 'product_category']
    fields = ['id', 'name', 'description', 'date', 'price', 'product_category']

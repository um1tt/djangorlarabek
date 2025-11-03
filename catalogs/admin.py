from django.contrib import admin
from .models import Restaurant, MenuItem, Category, ItemCategory, Option, ItemOption

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'is_deleted', 'deleted_at', 'created_at')
    list_filter = ('is_deleted', 'is_active')
    search_fields = ('name',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'restaurant', 'base_price', 'is_available', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted', 'is_available', 'restaurant')
    search_fields = ('name', 'description')
    autocomplete_fields = ('restaurant', 'categories', 'options')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted',)
    search_fields = ('name', 'slug')

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted',)
    search_fields = ('name',)

@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'category', 'position', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted',)
    search_fields = ('item__name', 'category__name')
    autocomplete_fields = ('item', 'category')

@admin.register(ItemOption)
class ItemOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'option', 'price_delta', 'is_default', 'is_deleted', 'deleted_at')
    list_filter = ('is_deleted', 'is_default')
    search_fields = ('item__name', 'option__name')
    autocomplete_fields = ('item', 'option')

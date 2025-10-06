from django.contrib import admin
from .models import Restaurant, MenuItem, Category, ItemCategory, Option, ItemOption

admin.site.register(Restaurant)
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(ItemCategory)
admin.site.register(Option)
admin.site.register(ItemOption)

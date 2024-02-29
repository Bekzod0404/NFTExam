from django.contrib import admin

from .models import Product, Author


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'current_bid', 'end_time']
    search_fields = ['title', 'author']
    list_filter = ['title', 'author']


@admin.register(Author)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'like_count']
    search_fields = ['first_name', 'last_name']
    list_filter = ['first_name', 'last_name']

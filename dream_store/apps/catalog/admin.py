from django.contrib import admin
from apps.catalog.models import Category, Product, ProductCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ProductCategoryInLine(admin.TabularInline):
    model = Product.categories.through
    extra = 1


class ImageInLine(admin.TabularInline):
    model = Product.images.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    fields = ("name", "description", "price", "quantity")
    readonly_fields = ("created_at", "updated_at")
    inlines = [ProductCategoryInLine, ImageInLine]

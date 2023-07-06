from django.contrib import admin

from .models import Category, Brand, Product, ProductLine

class ProductLineInline(admin.TabularInline):
    model = ProductLine

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
#admin.site.register(ProductLine)

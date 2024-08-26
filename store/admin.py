from django.contrib import admin
from .models import Category, SubCategory, Product, Review, Order, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'subcategory', 'price')
    list_filter = ('subcategory',)
    search_fields = ('name', 'description')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)

admin.site.register(Category)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Cart)

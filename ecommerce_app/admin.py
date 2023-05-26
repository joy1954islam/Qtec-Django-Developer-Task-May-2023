from django.contrib import admin
from .models import Category, SubCategory, Brand, Warranty, Seller, Product, ProductType


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('id', 'name', 'slug')


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    search_fields = ('id', 'name', 'slug', 'category')


admin.site.register(SubCategory, SubCategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('id', 'name', 'slug')


admin.site.register(Brand, BrandAdmin)


class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('id', 'name', 'slug')


admin.site.register(Warranty, WarrantyAdmin)


class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('id', 'name', 'slug')


admin.site.register(Seller, SellerAdmin)


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('id', 'name', 'slug')


admin.site.register(ProductType, ProductTypeAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'sku',
        'description',
        'stock',
        'price',
        'discount_price',
        'image',
        'slug',
        'category',
        'brand',
        'warranty',
        'seller',
        'product_type',
    )
    search_fields = (
        'id',
        'name',
        'sku',
        'description',
        'stock',
        'price',
        'discount_price',
        'image',
        'slug',
        'category',
        'brand',
        'warranty',
        'seller',
        'product_type',
    )


admin.site.register(Product, ProductAdmin)




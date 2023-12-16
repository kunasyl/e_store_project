from django.contrib import admin
from . import models


class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category', 'sale')
    search_fields = ('title', )
    inlines = (ProductImageInline,)


admin.site.register(models.ProductImage)
admin.site.register(models.Product, ProductAdmin)

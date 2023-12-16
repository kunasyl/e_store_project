from django.contrib import admin

from . import models


class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    # list_display = ('title', 'category', 'price')
    # list_filter = ('category', 'sale')
    # search_fields = ('title', )
    inlines = (OrderItemInline,)


admin.site.register(models.OrderItem)
admin.site.register(models.Order, OrderAdmin)

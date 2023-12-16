from django.contrib import admin

from . import models


class UserCartInline(admin.TabularInline):
    model = models.Cart
    extra = 1


class UserAdmin(admin.ModelAdmin):
    inlines = (UserCartInline, )


admin.site.register(models.Cart)
admin.site.register(models.User, UserAdmin)

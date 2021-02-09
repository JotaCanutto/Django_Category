from django.contrib import admin

from Category.models import Category, BannedCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class BannedCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(BannedCategory, BannedCategoryAdmin)

from django.contrib import admin

from trainer.models.category import Category


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'order'
    )

    search_fields = (
        'id',
        'name'
    )


admin.site.register(Category, CategoryAdmin)
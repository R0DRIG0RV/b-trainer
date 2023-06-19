from django.contrib import admin

from trainer.models.plan import Plan


class PlanAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'price',
        'duration',
        'discount',
        'price_discount',
        'created_at'
    )

    search_fields = (
        'id',
        'name'
    )


admin.site.register(Plan, PlanAdmin)
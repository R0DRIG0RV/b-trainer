from django.contrib import admin

from trainer.models.template_email import TemplateEmail


class TemplateEmailAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'created_at'
    )

    search_fields = (
        'id',
        'name'
    )


admin.site.register(TemplateEmail, TemplateEmailAdmin)
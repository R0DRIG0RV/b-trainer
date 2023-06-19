from django.contrib import admin

from trainer.models.document import Document


class DocumentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'url_file',
        'created_at'
    )

    search_fields = (
        'id',
        'name'
    )


admin.site.register(Document, DocumentAdmin)
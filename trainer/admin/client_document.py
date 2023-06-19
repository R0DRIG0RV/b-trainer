from django.contrib import admin

from trainer.models.client_document import ClientDocument


class ClientDocumentAdmin(admin.ModelAdmin):
    pass


admin.site.register(ClientDocument, ClientDocumentAdmin)
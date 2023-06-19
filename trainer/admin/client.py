from django.contrib import admin

from trainer.models.client import Client


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'dni',
        'firstname',
        'lastname',
        'email',
        'created_at'
    )

    search_fields = (
        'id',
        'dni',
        'firstname',
        'lastname',
    )


admin.site.register(Client, ClientAdmin)
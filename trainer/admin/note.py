from django.contrib import admin

from trainer.models.note import Note


class NoteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)